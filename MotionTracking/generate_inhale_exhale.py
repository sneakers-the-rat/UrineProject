#Import Standard Libraries
#from __future__ import division
import numpy as np
import math, os, sys

#Stats & Plotting Libraries
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import matplotlib.lines as lines
import scipy.signal as spysig
#import peakutils

#Add Local Path for Custom Modules & Import Custom Modules
#sys.path.insert(0,'C:\\Users\\"Rebekah Castillo"\\desktop\\"Smear Lab"\\MouseTracking\\data_analysis')
import analysis_functions as functions
from analysis_preferences import *

session_dir = "C:/darcin/data/Mouse_test/Session_test/"
analysis_dir = "C:/darcin/analysis/Mouse_test/Session_test/"

def generate_inhale_exhale(session_dir,analysis_dir):

    def low_pass_filter(data,frequency_range,cutoff_frequency):
        B, A = spysig.butter(1, cutoff_frequency / (frequency_range / 2), btype='low') # 1st order Butterworth low-pass
        data = spysig.lfilter(B, A, data, axis=0)
        return data

    inhale_onset2 = np.zeros((0,1))
    inhalation_point = np.zeros((1,1)); exhalation_point = np.zeros((1,1));

    #Set save location for generated inhale exhale files
    save_inhales = session_dir + 'inhalation_frames.dat'
    save_exhales = session_dir + 'exhalation_frames.dat'
    
    # inhalations = np.fromfile(save_inhales,dtype = float)
    
    # #Deletes files that are too small
    # if len(inhalations) < 10: 
    #     os.remove(save_inhales)
    
    # exhalations = np.fromfile(save_exhales,dtype = float);
    
    # if len(exhalations) < 10: 
    #     os.remove(save_exhales)      #won't this delete any directories made in previous lines?   

    sniff_file = session_dir + 'sniff.dat';

    sniff = np.fromfile(sniff_file,dtype = float) 

    #Low-pass filter sniff signal
    sniff = low_pass_filter(sniff,lowpassfilter_frequency_range,lowpassfilter_cutoff_frequency)

    #Smooth sniff signal using a rolling average
    sniff = functions.rolling_average(sniff,rollingwindow)

    #Identify inhalations & exhalations
    inhale_onset = functions.local_maxima(sniff, argrel_peakwindow)
    exhale_onset = functions.local_minima(sniff, argrel_peakwindow)
    global too_small

    ###INHALATIONS
    #Loop through each inhalation point of the signal
    for inhalationpoint in range(0,len(inhale_onset)):
        # if  math.floor(inhale_onset[inhalationpoint]/10) < len(nx):
            # skip_loop = functions.remove_nosepoke_sniffing(inhale_onset,nx,ny,inhalationpoint)
            # if skip_loop == True: 
            #     continue
        if too_small == 'remove next inhalation': #if the previous 2 inhalations were too close, skip this inhalation
            too_small = 'none'; continue   
        too_small = functions.exclude_small_amplitude_inhalations(sniff,inhale_onset,inhalationpoint,0.3333,10)
                           
        #If inhalation point is not eliminated, add it to your array
        if too_small == 'none':
            inhalation_point[0,0] = inhale_onset[inhalationpoint]
            inhale_onset2 = np.append(inhale_onset2,inhalation_point,axis = 0)
            # inhale_handle = file(save_inhales,'ab')
            inhale_handle = open(save_inhales,'ab')
            inhalation_point.tofile(inhale_handle)
            inhale_handle.close()
          
    ###EXHALATIONS
    #Loop through each exhalation point of the signal
    for exhalationpoint in range(0,len(exhale_onset)-1): 
        # if math.floor(exhale_onset[exhalationpoint]/10) < len(nx):
        #     skip_loop = functions.remove_nosepoke_sniffing(exhale_onset,nx,ny,exhalationpoint)
        #     if skip_loop == True: 
        #         continue
        if too_small == 'remove next exhalation': #if the previous 2 exhalations were too close, skip this exhalation
            too_small = 'none'; continue   
        too_small = functions.exclude_small_amplitude_exhalations(sniff,exhale_onset,exhalationpoint,0.3333,10)
        #If exhalation point is not eliminated, add it to your array
        if too_small == 'none':
            exhalation_point[0,0] = exhale_onset[exhalationpoint]
            #exhale_handle = file(save_exhales,'ab')
            exhale_handle = open(save_exhales,'ab')
            exhalation_point.tofile(exhale_handle)
            exhale_handle.close()

    print("DONE!")