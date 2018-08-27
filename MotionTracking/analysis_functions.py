##LIBRARIES
import numpy as np, os, math, sys
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.patches as patches
import scipy.signal as spysig
from matplotlib.pyplot import subplots
from pylab import *
#sys.path.insert(0,'C:\\Users\\Teresa\\workspace\\OlfactoryNavigation\\data_analysis\\')
from analysis_preferences import *


###SIGNAL PROCESSING
'''
Rejects outliers from a dataset
Input: dataset, # of standard deviations of acceptance
Output: dataset without outliers
'''
def reject_outliers(data,standard_deviations):
    data = data[abs(data - np.mean(data)) < standard_deviations * np.std(data)]
    return data

'''
Low-Pass filter a dataset
Input: data array, range of frequencies in data, high cut-off frequency
Output: filtered data array
'''
def low_pass_filter(data,frequency_range,cutoff_frequency):
    B, A = spysig.butter(1, cutoff_frequency / (frequency_range / 2), btype='low') # 1st order Butterworth low-pass
    data = spysig.lfilter(B, A, data, axis=0)
    return data

'''
Down-Sample a dataset
Input: data array, multiple to down-sample by
Output: down-sampled data array
'''
def down_sample(data,downsample):
    data = data[0:len(data):downsample]
    return data

'''
Rolling Average over dataset
Input: data array, window size
Output: smoothed data array
'''
def rolling_average(data,rolling_window):
    data = np.convolve(data, np.ones((rolling_window,))/rolling_window, mode='valid')
    return data

'''
Smooths a voltage signal using a median filter window
Input: dataset, filter window
Output: smoothed dataset
'''
def median_filter(data,med_filter_window):
    data = spysig.medfilt(data,med_filter_window)
    return data

##SIGNAL CALCULATIONS
'''
Calculates local maxima of a signal (finds inhalations)
Input: data array, window to find local maxima in
Output: data array of frames where local maxima)
'''
def local_maxima(data,peakwindow):
    localmaxima = spysig.argrelmax(data,order = peakwindow)
    localmaxima = localmaxima[0]
    return localmaxima

'''
Calculates local minima of a signal (finds inhalations)
Input: data array, window to find local minima in
Output: data array of frames where local minima)
'''
def local_minima(data,peakwindow):
    localminima = spysig.argrelmax(data,order = peakwindow)
    localminima = localminima[0]
    return localminima
'''
Calculates frequency of local maxima array (sniff frequency) 
Input: data array, data point of interest, sampling rate
Output: instantaneous frequency
'''
def instantaneous_frequency(data,inhalation_point,sampling_rate):
    frequency = 1/((data[inhalation_point+1] - data[inhalation_point])/sampling_rate)
    return frequency

'''
Function: gives velocity over a 2D array of xy coordinates
Input: x values array, y values array, and smoothing window size (even #)
Output: dataset the same length (minus length of window) of velocities
'''
def calculate_velocity(datax,datay,bin):
    datalength = len(datax)
    velocity = np.zeros([datalength-bin,1])
    for i in range (bin/2,datalength - (bin/2)):
        if i < bin/2:
            pass
        else: 
            nosevel = np.sqrt(np.square(datax[i] - datax[i-(bin/2)+1]) + np.square(datay[i] - datay[i-(bin/2)+1]))
            velocity[i-(bin/2),0] = nosevel
    return velocity

'''
Function: gives acceleration over a 2D array of xy coordinates
Input: x values array, y values array, and smoothing window size (even #)
Output: dataset the same length (minus length of window) of accelearations
'''
def calculate_acceleration(datax,datay,bin):
    datalength = len(datax)
    acceleration = np.zeros([datalength-bin,1]) 
    for i in range (bin/2,datalength - bin/2):  
        if i < bin/2: 
            pass
        else: 
            nosevel = np.sqrt(np.square(datax[i] - datax[i-1]) + np.square(datay[i] - datay[i-1]))
            prevnosevel = np.sqrt(np.square(datax[i-(bin/2)+1] - datax[i-(bin/2)]) + np.square(datay[i-(bin/2)+1] - datay[i-(bin/2)]))
            acceleration[i,0] = nosevel - prevnosevel
    return acceleration

###DATA MANIPULATIONS SPECIFIC TO EXPERIMENTS
'''
Removes inhalations from previously identified high-density areas
Input: inhalations array, nose position x array, nose position y array, and inhalation point being considered
Output: inhalations array without inhalations in those high-density areas
'''
def remove_nosepoke_sniffing(inhale_onset,nx,ny,inhalationpoint):
    skip_loop = False
    if math.floor(inhale_onset[inhalationpoint]/10) <= len(nx):
        if nx[math.floor(inhale_onset[inhalationpoint]/10)] <= 421:
            skip_loop = True
        if nx[math.floor(inhale_onset[inhalationpoint]/10)] >= 1047 and ny[math.floor(inhale_onset[inhalationpoint]/10)] <= 394 and ny[math.floor(inhale_onset[inhalationpoint]/10)] >= 314:
            skip_loop = True
    return skip_loop

'''
Removes inhalation points that are too small in amplitude to be a sniff 
Input: data array, maxima array, data point of interest, fraction of amplitude acceptable, # of inhalations to average over
Output: decision to remove or keep data point
'''
def exclude_small_amplitude_inhalations(data,local_maxima,inhalation_point,threshold,averaging_window):
    global too_small
    #Calculate sniff amplitudes for a window of 10 inhalation points around point of interest
    if inhalation_point > (averaging_window//2) and inhalation_point < len(local_maxima) - (averaging_window//2):
        avg_sniff_amplitude = []
        for window in range (inhalation_point-(averaging_window//2),inhalation_point+(averaging_window//2)):
            sniff_amplitude = np.max(data[local_maxima[window]:local_maxima[window+1]]) - np.min(data[local_maxima[window]:local_maxima[window+1]])
            avg_sniff_amplitude.append(sniff_amplitude)
        
        #If sniff amplitude of current sniff is less than a third of the avg amplitude
        if np.mean(avg_sniff_amplitude)*threshold > np.max(data[local_maxima[inhalation_point]:local_maxima[inhalation_point+1]]) - np.min(data[local_maxima[inhalation_point]:local_maxima[inhalation_point+1]]):
            if data[local_maxima[inhalation_point]] > data[local_maxima[inhalation_point+1]]:
                too_small = 'remove next inhalation'
            if data[local_maxima[inhalation_point]] <= data[local_maxima[inhalation_point+1]]:
                too_small = 'remove current inhalation'
        else: too_small = 'none'
    else: too_small = 'none'
    return too_small

'''
Removes exhalation points that are too small in amplitude to be a sniff 
Input: data array, maxima array, data point of interest, fraction of amplitude acceptable, # of exhalations to average over
Output: decision to remove or keep data point
'''
def exclude_small_amplitude_exhalations(data,local_maxima,exhalation_point,threshold,averaging_window):
    global too_small
    #Calculate sniff amplitudes for a window of 10 exhalation points around point of interest
    if exhalation_point > (averaging_window//2) and exhalation_point < len(local_maxima) - (averaging_window//2):
        avg_sniff_amplitude = []
        for window in range (exhalation_point-(averaging_window//2),exhalation_point+(averaging_window//2)):
            sniff_amplitude = np.max(data[local_maxima[window]:local_maxima[window+1]]) - np.min(data[local_maxima[window]:local_maxima[window+1]])
            avg_sniff_amplitude.append(sniff_amplitude)
        
        #If sniff amplitude of current sniff is less than a third of the avg amplitude
        if np.mean(avg_sniff_amplitude)*threshold > np.max(data[local_maxima[exhalation_point]:local_maxima[exhalation_point+1]]) - np.min(data[local_maxima[exhalation_point]:local_maxima[exhalation_point+1]]):
            if data[local_maxima[exhalation_point]] < data[local_maxima[exhalation_point+1]]:
                too_small = 'remove next exhalation'
            if data[local_maxima[exhalation_point]] >= data[local_maxima[exhalation_point+1]]:
                too_small = 'remove current exhalation'
        else: too_small = 'none'
    else: too_small = 'none'
    return too_small

