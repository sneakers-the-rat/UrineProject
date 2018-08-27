'''
MouseTracker 750
A tracking program for live recording and heatmapping of freely-moving mouse nose location and sniff signal
Goal: to make a simple, usable GUI for location and sniff data acquisition and processing

Written: Ian Jackson (Contact: orbitalhybridization@gmail.com)

Last Updated: 7/26/18
'''

'''
Note: when i was running this, all stdout (command line output) only printed after closing GUI. this may lead to future issues on other systems.
please let me know if errors like this or others come about.

*Note: to close the program, hit close twice (still working on fixing this hehe)

'''

#Import Standard Modules
#from __future__ import division
from tkinter import *
import argparse
import random
import time
import math, os, sys
import numpy as np
import datetime

#Server Running Modules
from pythonosc import dispatcher
from pythonosc import osc_server
import threading

#NIDAQ Interfacing Modules
import nidaqmx, time
from ctypes import *
import numpy as np
from nidaqmx.constants import AcquisitionType, Edge
from nidaqmx.stream_readers import AnalogMultiChannelReader

#Import Stats & Plotting Modules

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import matplotlib.lines as lines
import scipy.signal as spysig
#import peakutils
from mpl_toolkits.mplot3d import Axes3D

#Import Custom Modules
import analysis_functions as functions
from analysis_preferences import *
import generate_inhale_exhale as generate_inhale_exhale
from handle_data import DataHandler
from generate_figures import FigureGenerator
from notifications import PopUp

'''
A function for combining multiple functions. Used for multi-command buttons.
'''

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

'''
MouseTracker Main
'''

class MouseTracker:

    def __init__(self,master):

        #GUI WINDOW SETUP
        self.master = master
        master.title("MouseTracker 750")

        self.server_active = False

        #EXPERIMENTAL INFO INITIATION
        self.mouseID = "" #default ID

        self.name = ""

        self.version = ""

        self.session = ""

        self.sniffing = ""

        self.notes = ""

        ###BUTTONS
        self.getID = Button(self.master,text="Experiment Info",command=self.EnterInfo).grid(row=0,column=0)

        self.startSession_button = Button(self.master,text="Start Session",command=self.startSession).grid(row=1,column=0)

        self.endSession_button = Button(self.master,text="End Session",command=self.endSession).grid(row=2,column=0)

        self.analyze_button = Button(self.master,text="Analyze Data",command=self.analyze).grid(row=3,column=0)

        self.yeet_button = Button(self.master,text="Yeet!",command=self.yeet).grid(row=4,column=0)

        self.close_button = Button(self.master,text="Close", command=self.closeGUI).grid(row=5,column=0)


    ###GUI FUNCTIONALITIES (CALLED BY BUTTONS)###

    def yeet(self):

        yeet = Label(self.master,text="Yeet!").grid(row=6,sticky=W)

    def EnterInfo(self):
        '''
        Opens a window that allows user to enter experiment info.
        '''
        top = Toplevel()
        top.title("Experiment Information")
        top.lift()

        EnterID = Label(top, text="Mouse ID: ").grid(row=0, sticky=W)
        self.entry = Entry(top)
        self.entry.grid(row=0,column=1)

        EnterName = Label(top, text="Your Name: ").grid(row=1, sticky=W)
        self.entry2 = Entry(top)
        self.entry2.grid(row=1,column=1)

        EnterExpVer = Label(top, text="Enter Experiment Version: ").grid(row=2, sticky=W)
        self.entry3 = Entry(top)
        self.entry3.grid(row=2,column=1)

        EnterSession = Label(top,text="Session Number: ").grid(row=3,sticky=W)
        self.entry4 = Entry(top)
        self.entry4.grid(row=3,column=1)

        EnterSniffing = Label(top, text="Sniffing? (Y/N): ").grid(row=4, sticky=W)
        self.entry5 = Entry(top)
        self.entry5.grid(row=4,column=1)        

        EnterNotes = Label(top, text="Notes: ").grid(row=5, sticky=W)
        self.entry6 = Text(top,height=5)
        self.entry6.grid(row=5,column=1)


        confirm = Button(top,text="Confirm", command=combine_funcs(self.setInfo,top.destroy)).grid(row=8,column=1)

        dismiss = Button(top, text="Dismiss", command=top.destroy).grid(row=9,column=1)

        top.mainloop()


    def setInfo(self):
        '''
        Called by EnterInfo to set self.mouseID to entered ID. Subsequently creates 1) a CSV file with the coordinates information
        and 2) a txt file with all experimental information entered by the user
        '''
        self.mouseID = self.entry.get()
        self.name = self.entry2.get()
        self.version = self.entry3.get()
        self.session = self.entry4.get().strip()
        self.sniffing = self.entry5.get().strip()
        self.notes = self.entry6.get(0.0,END)

        #Create data handler object
        self.dataq = DataHandler(self.mouseID,self.name,self.version,self.session,self.sniffing,self.notes)
        self.dataq.makeFiles()


    def startSession(self):
        '''
        Initialises and runs an OSC server with default address and port, opens channel for incoming messages.
        Contains one handler that calls self.location_handler.
        '''

        if len(self.mouseID) == 0:

            #Error Popup If Information Hasn't Been Entered
            IDError = PopUp("ERROR","Must Enter a Mouse ID!")
            IDError.show()

        else:

            ###SERVER AND NIDAQ START-UP

            ###SERVER INITIATION: runs osc server to receive location information from Bonsai

            # parser = argparse.ArgumentParser()
            # parser.add_argument("--ip",default="127.0.0.1",help="The ip of the OSC server")
            # parser.add_argument("--port",type=int,default=5005, help="The port the OSC server is listening on")
            #args = parser.parse_args()
            
            dispatch = dispatcher.Dispatcher()
            #Sets incoming data from server to go to the data handler's location_handler function
            dispatch.map("/data",self.dataq.location_handler,"Location")
            #Iniates Server Without Running It
            self.server = osc_server.ThreadingOSCUDPServer(('127.0.0.1',5005),dispatch)
            self.server.daemon = True
            self.server_active = True

            ###NIDAQ AND SESSION INITIATION: USB-6009 interfacing to receive sniff information from NIDAQ

            threading.Thread(target=self.server.serve_forever).start()

            #Session Running PopUp Notification
            StartNotification = PopUp("NOTIFICATION","Session started! Writing to CSV file...")
            StartNotification.show()


    def endSession(self):
        '''
        Shuts down OSC server and NIDAQ Communication.
        '''

        if self.server_active == False:
            EndError = PopUp("ERROR","Session not running!")
            EndError.show()

        else:

            self.server.shutdown()
            self.server_active = False
            self.dataq.closeFiles()
            EndNotification = PopUp("NOTIFICATION","Hell yeah, session ended! Data saved in folders for this mouse!")
            EndNotification.show()


    def closeGUI(self):
        '''
        Closes GUI if experiment is no longer running. Creates an error message if server is still running.
        '''
        if self.server_active:
            CloseError = PopUp("ERROR","Cannot 'Close' while session is still running!")
            CloseError.show()
        else: self.master.quit()

    def analyze(self):
        '''
        Draws and displays mouse path in two figures via matplotlib. Figure 1 is a heatmap,
        Figure 2 draws a line between the (x,y) coordinates, which superimpose another heatmap.
        Also enters metadata (average overall mouse location) to a file with all mouse information
        '''
        if self.server_active:
            AnalyzeError = PopUp("ERROR","Cannot 'Analyze' while session is still running!")
            AnalyzeError.show()
        
        elif self.server_active == False and len(self.mouseID) == 0:
            NoIDAnalyzeError = PopUp("ERROR","Nothing to analyze! Try entering mouse ID, then starting session.")
            NoIDAnalyzeError.show()
        else:
            '''
            Draws heatmaps for mouse location and sniff frequency throughout experiment and updates metadata file
            '''
            figures = FigureGenerator(self.dataq.session_dir,self.dataq.analysis_dir,self.sniffing)

            figures.AnalyzeLocation()
            figures.AnalyzeSniff()
            figures.doMeta()

            AnalyzedNotification = PopUp("NOTIFICATION","Analysis complete! Files saved in session folder for this mouse!")
            AnalyzedNotification.show()

if __name__ == "__main__":

    '''
    Initialises and opens main GUI window.
    '''
    root = Tk()
    mt = MouseTracker(root)
    root.mainloop()


'''
For auto-ending if our experiment has a timer

    if time.time() - session_start >= session_length:
        fmon_serial.close_all_valves()
        reasonforend = "Auto Session End"
        break
'''