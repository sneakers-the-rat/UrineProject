'''
Function called by GUI that takes raw data Draws and displays mouse path in two figures via matplotlib. Figure 1 is a heatmap,
Figure 2 draws a line between the (x,y) coordinates, which superimpose another heatmap.
Also enters metadata (average overall mouse location) to a file with all mouse information
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from analysis_preferences import *


class FigureGenerator():

    def __init__(self,session_dir,analysis_dir,sniffing):

        self.session_dir = session_dir
        self.analysis_dir = analysis_dir
        self.sniffing = sniffing
        self.frequencies = []
        self.inhales = np.fromfile(session_dir + 'inhalation_frames.dat',dtype=float)
        self.locdata = np.nan_to_num(np.loadtxt(open(self.session_dir + "NoseLocationLog.csv", "rb"), dtype=float, delimiter=",", skiprows=1))


    #A Function for Making a 3D Histogram (Adopted from https://stackoverflow.com/questions/14002480/2d-and-3d-scatter-histograms-from-arrays-in-python)
    # def hist3d_bubble(self,x_data, y_data, z_data, bins=10):
    #     ax1 = np.histogram2d(x_data, y_data, bins=bins)
    #     ax2 = np.histogram2d(x_data, z_data, bins=bins)
    #     ax3 = np.histogram2d(z_data, y_data, bins=bins)
    #     xs, ys, zs = ax1[1], ax1[2], ax3[1]
    #     smart = np.zeros((bins, bins, bins),dtype=int)
    #     for (i1, j1), v1 in np.ndenumerate(ax1[0]):
    #         if v1 == 0:
    #             continue
    #         for k2, v2 in enumerate(ax2[0][i1]):
    #             v3 = ax3[0][k2][j1]
    #             if v1 == 0 or v2 == 0 or v3 == 0:
    #                 continue
    #             num = min(v1, v2, v3)
    #             smart[i1, j1, k2] += num
    #             v1 -= num
    #             v2 -= num
    #             v3 -= num
    #     points = []
    #     for (i, j, k), v in np.ndenumerate(smart):
    #         points.append((xs[i], ys[j], zs[k], v))
    #     points = np.array(points)
    #     fig = plt.figure()
    #     sub = fig.add_subplot(111, projection='3d')
    #     sub.scatter(points[:, 0], points[:, 1], points[:, 2],
    #                 color='black', marker='o', s=128*points[:, 3])
    #     sub.axes.set_xticks(xs)
    #     sub.axes.set_yticks(ys)
    #     sub.axes.set_zticks(zs)
    #     return points, sub, fig

    # points, sub, fig = self.hist3d_bubble(self.locx,self.locy,self.frequencies,bins=4)
    # axes3 = plt.gca()
    # axes3.set_xlabel('x')
    # axes3.set_ylabel('y')
    #fig.savefig(self.analysis_dir + "xysniff_heatmap.png")


    def AnalyzeSniff(self):
        
        #Calculate sniff frequency from inhalation data
        #for i in range(0,len(self.inhales)-1):
        for i in range(0,297):
            j = i+1
            num_samples = self.inhales[j] - self.inhales[i]
            sniff_freq = (num_samples / samplingrate)**(-1)
            self.frequencies.append(sniff_freq)

        #Prepare metadata for sniff frequency
        self.meta_sniff_freq = np.average(self.frequencies)

        #Loops through x,y values to create bins with averaged frequency values

        #we need to find the number of pixels taken per frame by the camera. to do this, connect the camera to the comuter
        #then open bonsai and start the script with the play button. make sure the CameraCapture screen pops up. if it does
        #not, double click the pink module called "CameraCapture". next, right click on the screen so that you can see the
        # cursor coordinates and colour values on the bottom. use the cursor coordinates to find the max x and max y values
        #this should work as our xmax and ymax values!

        xmax = 1200 #max number of x pixels taken per frame by camera
        xbins = 20
        ymax = 800 #max number of y pixels taken per frame by camera
        ybins = 20
        maxavg_freq = 0
        minavg_freq = 0

        heatmap_array = np.zeros((ymax//ybins,xmax//xbins))
        
        ycounter = 0

        while ycounter < ymax//ybins:

            #set range for current y bin
            ybins_high = ybins * (ycounter + 1); ybins_low = ybins * (ycounter)

            xcounter = 0

            while xcounter < xmax//xbins:

                #set range for current x bin
                xbins_high = xbins * (xcounter + 1); xbins_low = xbins * (xcounter)

                frequencies_to_average = []

                for index in range(0,len(self.locdata)):

                    #check for x and y values within bin range, add time-corresponding frequencies to a list to be averaged 
                    if ((self.locy[index] < ybins_high) and (self.locy[index] >= ybins_low)) and ((self.locx[index] < xbins_high) and (self.locx[index] >= xbins_low)):

                        frequencies_to_average.append(self.frequencies[index])

                        if self.frequencies[index] > maxavg_freq:

                            maxavg_freq = self.frequencies[index]

                        if self.frequencies[index] < minavg_freq:

                            minavg_freq = self.frequencies[index]

                #add averaged frequencies to array at coordinates of corresponding x,y bin and go to next bin
                if len(frequencies_to_average) == 0:
                    heatmap_array[ycounter,xcounter] = 0
                else: heatmap_array[ycounter,xcounter] = np.average(frequencies_to_average)
                xcounter = xcounter + 1

            ycounter = ycounter + 1

        plt.figure()
        plt.imshow(heatmap_array,cmap='hot',interpolation='gaussian',aspect="auto",vmin = minavg_freq,vmax = maxavg_freq)
        plt.axis('off')
        plt.savefig(self.analysis_dir + "xysniff_heatmap.png")


    def AnalyzeLocation(self):

        #Initialize X and Y coordinates from experimental location data.
        self.locx = self.locdata[:,0]
        self.locy = self.locdata[:,1]
        
        #Generate metadata from experiment by averaging all X and all Y values
        self.metadatax = np.average(self.locx)
        self.metadatay = np.average(self.locy)
        
        #Create and save plots for histograms

        #plt.xlim(xmin,xmax) in case we need to set the graph limits to the coordinates of the box edges!
        #plt.ylim(ymin,ymax)
        
        plt.figure(1)
        plt.hist2d(self.locx,self.locy,bins=30,cmap='hot')
        axes = plt.gca()
        axes.set_xlabel('x')
        axes.set_ylabel('y')
        plt.savefig(self.analysis_dir + "heatmap.png")
        plt.clf()

        plt.figure(2)
        plt.hist2d(self.locx, self.locy, bins=30,cmap='hot'),
        plt.plot(self.locx, self.locy,'w-')
        axes2 = plt.gca()
        axes2.set_xlabel('x')
        axes2.set_ylabel('y')
        plt.savefig(self.analysis_dir + "trailing_heatmap.png")
        plt.clf()

    def doMeta(self):

        #Update Experimental Metadata by writing averages to metadata file. 

        if sniffing == 'Y':
            with open(datadir + "metadata.csv",'a') as meta:
                meta.write(self.mouseID + "," + str(self.metadatax) + "," + str(self.metadatay) + "," + str(self.meta_sniff_freq))

        else:
            with open(datadir + "metadata.csv",'a') as meta:
                meta.write(self.mouseID + "," + str(self.metadatax) + "," + str(self.metadatay) + "," + "No Sniff")

# session_dir = "C:/darcin/data/Mouse_test/Session_test/"
# analysis_dir = "C:/darcin/analysis/Mouse_test/Session_test/"
# test = FigureGenerator(session_dir,analysis_dir,"Y")
# test.AnalyzeLocation()
# test.AnalyzeSniff()

# locdata = np.nan_to_num(np.loadtxt(open(session_dir + "NoseLocationLog.csv", "rb"), delimiter=",", skiprows=1))
# test.locx = locdata[:,0]
# test.locy = locdata[:,1]