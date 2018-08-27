from analysis_preferences import *
import nidaqmx, time
from nidaqmx.constants import AcquisitionType, Edge
from nidaqmx.stream_readers import AnalogMultiChannelReader
from pythonosc import dispatcher
from pythonosc import osc_server
import threading
import time
import datetime

'''
A Class for creating obejcts that handle All Incoming Data/Information from GUI, OSC Server, and NIDAQ

These objects have four functions: 1) make folders for mouse's session in data and analysis folder 2) write coordinate info to an XY file 3) write sniff info to a .DAT file
4) close files at the end of session.
'''


class DataHandler():

    def __init__(self,mouseID,name,version,session,sniffing,notes):

        self.mouseID = mouseID
        self.name = name
        self.version = version
        self.session = session
        self.sniffing = sniffing
        self.notes = notes
        self.session_start = None
        self.reader = AnalogMultiChannelReader(ni_data.in_stream)
        self.data = np.zeros((channel_num,buffersize),dtype=np.float64) #buffersize.value


    def makeFiles(self):

        #Make all necessary data and analysis folders for this mouse and the current session if there aren't already

        if (os.path.exists(datadir + "Mouse_" + self.mouseID + "/") == False):  
            os.makedirs(datadir + "Mouse_" + self.mouseID + "/")

        if (os.path.exists(savingdir + "Mouse_" + self.mouseID + "/") == False):  
            os.makedirs(savingdir + "Mouse_" + self.mouseID + "/")

        if (os.path.exists(datadir + "Mouse_" + self.mouseID + "/" + "Session_" + self.session) == False):  
            os.makedirs(datadir + "Mouse_" + self.mouseID + "/" + "Session_" + self.session)

        if (os.path.exists(savingdir + "Mouse_" + self.mouseID + "/" + "Session_" + self.session) == False):  
            os.makedirs(savingdir + "Mouse_" + self.mouseID + "/" + "Session_" + self.session)

        #Set directories to save data and analysis output to particular session
        self.session_dir = datadir + "Mouse_" + self.mouseID + "/" + "Session_" + self.session + "/" #session data folder
        self.analysis_dir = savingdir + "Mouse_" + self.mouseID + "/" + "Session_" + self.session + "/" #session analysis folder
        self.ch0_file = self.session_dir + '/sniffing.dat' #sniff data file location
        self.sniff_time_file = self.session_dir + '/snifftimes.csv' #sniff timestamp data location

        #Create and open csv and txt files for saving data. Write information to these files.
        os.chdir(self.session_dir) #change the current working directory to whatever session we're working with
        self.ch0_handle = open(self.ch0_file,'ab')
        self.sniff_time_handle = open(self.sniff_time_file,'w+')
        self.XYFile = open("NoseLocationLog.csv","w+")
        self.XYFile.write("x, y\n")
        InfoFile = open("ExperimentInfo.txt","w+")
        note = experiment + '\n\n\n'
        InfoFile.write(note)
        note = "Mouse ID: " + self.mouseID + '\n\n'
        InfoFile.write(note)
        note = "Experimenter: " + self.name + '\n\n'
        InfoFile.write(note)
        localtime = datetime.datetime.now()
        note = "Date/Time: " + localtime.strftime('%Y-%m-%d, %H:%M:%S') + '\n\n'
        InfoFile.write(note)
        note = "Experiment Version: " + self.version + '\n\n'
        InfoFile.write(note)
        note = "Session: " + self.session + '\n\n'
        InfoFile.write(note)
        note = "Sniffing: " + self.sniffing + '\n\n'
        InfoFile.write(note)
        note = "Notes: \n" + self.notes
        InfoFile.write(note)
        InfoFile.close()

    def location_handler(self,unused_addr,args,locationx,locationy):
        '''
        Called by startServer to write receieved coordinates to CSV file.
        '''
        self.XYFile.write("{0}, {1}\n".format(locationx,locationy))
    
    def ni_handler(self):
        '''
        Function for reading and saving data to a fie from multiple channels (this is all analog input)
        Also saves timestamps throughout the experiment
        '''
        self.reader.read_many_sample(self.data,number_of_samples_per_channel=buffersize, timeout=10.0)
        self.data[0,:].tofile(self.ch0_handle); 
        self.sniff_time_handle.write(str(time.time() - self.session_start))

    def closeFiles(self):

        self.ch0_handle.close()
        self.sniff_time_handle.close()
        self.XYFile.close()