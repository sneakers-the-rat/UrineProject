##LIBRARIES
import numpy as np
import os
import math
import matplotlib.pyplot as plt
from ctypes import *
import nidaqmx

#Type Definitions -- how to speak C in Python (NIDAQ uses MATLAB stuff)
int32 = c_long #32 bit integer
uInt64 = c_ulonglong #64 bit positive integer
float64 = c_double #64 bit float

#Subject/Experiment Preferences
experiment = "DARCIN EXPERIMENT"
#max_sessions = 10
session_of_interest = 10

#Variable Initiation
too_small = 'none'

#Plotting Options
chosenfont = {'fontname':'Arial'}
color_list = ['k','b','g','r','magenta','y','purple','cyan','lightpink','darkolivegreen','chartreuse']
axes_font_size = 20
title_font_size = 26
scatter_point_size = 140
histogram_bin_number = 80

#Standard Pathways
datadir = "C:/darcin/data/"
savingdir = "C:/darcin/analysis/"

#Rolling Averages Options
rollingwindow = 21 #binning variable for rolling average calculation

#Low Pass Filter Options 
lowpassfilter_frequency_range = 800 # 1 ns -> 1 GHz
lowpassfilter_cutoff_frequency = 50 # 10 MHz

#Down Sample Options 
down_sample = 10 #downsample data 10x

#Local Minima/Maxima Options
argrel_peakwindow = 21 #binning variable for local maxima/minima calculations

#Time Limits
trial_time_limit = 15

#NIDAQ Sampling and Channel Options
samplingrate = 800
buffersize = 25
channel_num = 1 #number of channels, also change this if you're using more than one channel
channels = 'Dev1/ai0' #+ str(channel_num-1) #channels used for NIDAQ (if you're using more than just the one channel, Ex: 'Dev1/ai0:5' for 6 channels, 0 thru 5)
ni_data = nidaqmx.Task()

#Coordinates
#box_edges = [[],[],[],[]]
#urinesample = [,]

