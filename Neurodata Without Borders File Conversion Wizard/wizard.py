from PyQt5 import QtCore
#from PyQt5 import QtGui
#from PyQt5.QtCore import *
from PyQt5 import QtWidgets
#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QLineEdit, QFileDialog, QPushButton, QTreeWidget, QScrollArea
from PyQt5.QtCore import QDate, QTime, QDateTime
#from PyQt5.QtCore import pyqtSlot
#import scipy as sio
import scipy.io
import pynwb 
#from pynwb import NWBFile
from pynwb import NWBHDF5IO
#from datetime import datetime
import datetime
from dateutil.tz import tzlocal
import numpy as np
import h5py
import hdmf
#For error handling:
from designfiles.file_verify import Ui_file_verify_dialog

#class for the QT Combo Box
class QIComboBox(QtWidgets.QComboBox):
    def __init__(self,parent=None):
        super(QIComboBox, self).__init__(parent)

#class for the QT Line Edit Box
class QLineEdit(QtWidgets.QLineEdit):
    def __init__(self,parent=None):
        super(QLineEdit, self).__init__(parent)

#class for the QT Line Edit Box
class QPushButton(QtWidgets.QPushButton):
    def __init__(self,parent=None):
        super(QPushButton, self).__init__(parent)

#class for the window
class QWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(QWidget, self).__init__(parent)


#class for the tree widget

class QTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(QTreeWidget,self).__init__(parent)

#Class for file upload error handling:
class file_upload_error(object):
    def file_upload_error(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(265, 162)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 231, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.data_verify_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.data_verify_grid.setContentsMargins(0, 0, 0, 0)
        self.data_verify_grid.setObjectName("data_verify_grid")
        self.data_verify_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.data_verify_pte.setMinimumSize(QtCore.QSize(200, 100))
        self.data_verify_pte.setObjectName("data_verify_pte")
        self.data_verify_grid.addWidget(self.data_verify_pte, 0, 0, 1, 1)
        self.data_verify_btn = QtWidgets.QPushButton(Dialog)
        self.data_verify_btn.setGeometry(QtCore.QRect(100, 130, 75, 23))
        self.data_verify_btn.setObjectName("data_verify_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.data_verify_pte.setPlainText(_translate("Dialog", "The translator expected headerfile.mat"))
        self.data_verify_btn.setText(_translate("Dialog", "PushButton"))

#class for the NWB Generator wizard
class MagicWizard(QtWidgets.QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        
        #add all the pages to the wizard
        self.addPage(Welcome(self))
        self.addPage(HeaderScreen(self))
        self.addPage(SubjectTable(self))
        self.addPage(Welcome2(self))
        self.addPage(WidefieldStep1(self))
        self.addPage(WidefieldStep2(self))
        self.addPage(WidefieldStep3(self))
        self.addPage(MatlabStep1(self))
        self.addPage(MatlabStep2(self))
        
        
        #set window title
        self.setWindowTitle("NWB converter")
        
        #set window size        
        self.resize(1800,1400)

        #global variable goes here?  This was necessary when saving nwbfile in 2PhotonStep2
        global nwbfile
      

#code for the Welcome page
class Welcome(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)

        #create text entry box
        self.QLineEdit = QLineEdit('filename')   

        # create push button 
        self.fileName = 'file'   
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Select Header File", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            print(self.fileName)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Load Header"))
                
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.QLineEdit)
        layout.addWidget(self.pushButton)
        #layout.addWidget(self.datetime)   
        self.setLayout(layout)

    #This code creates the file select dialog and saves it in a global variable
    def on_click(self):
        self.openFileNameDialog()                
        print(self.fileName)        
        
        if 'Headerfile.mat' not in self.fileName:
            file_verify_dialog = QtWidgets.QDialog()
            ui = Ui_file_verify_dialog()
            ui.setupUi(file_verify_dialog)
            file_verify_dialog.show()                 
            rsp = file_verify_dialog.exec_() #The exec statement prevents window closing immediately
            if 'Headerfile.mat' not in self.fileName:
                return
            else:
                print('File name verified')
        else:
            global headerfilename
            headerfilename = self.fileName        
            global identifier
            identifier = self.QLineEdit.text()
            identifier = identifier
            print(identifier)

        
        

#code for the Header Screen
class HeaderScreen(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(HeaderScreen, self).__init__(parent)
        
        self.setObjectName("Dialog")
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setSizeIncrement(QtCore.QSize(1, 4))
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.setToolTipDuration(0)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1600, 1200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(370, 10, 16, 551))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 15, 341, 541))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.column_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.column_1.setContentsMargins(0, 0, 0, 0)
        self.column_1.setObjectName("column_1")
        self.keywords_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.keywords_le.setObjectName("keywords_le")
        self.column_1.addWidget(self.keywords_le, 3, 1, 1, 1)
        self.experimenter_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.experimenter_lbl.setObjectName("experimenter_lbl")
        self.column_1.addWidget(self.experimenter_lbl, 0, 0, 1, 1)
        self.related_publications_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.related_publications_le.setObjectName("related_publications_le")
        self.column_1.addWidget(self.related_publications_le, 5, 1, 1, 1)
        self.protocol_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.protocol_le.setObjectName("protocol_le")
        self.column_1.addWidget(self.protocol_le, 4, 1, 1, 1)
        self.institution_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.institution_le.setObjectName("institution_le")
        self.column_1.addWidget(self.institution_le, 1, 1, 1, 1)
        self.experimenter_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.experimenter_le.setObjectName("experimenter_le")
        self.column_1.addWidget(self.experimenter_le, 0, 1, 1, 1)
        self.protocol_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.protocol_lbl.setObjectName("protocol_lbl")
        self.column_1.addWidget(self.protocol_lbl, 4, 0, 1, 1)
        self.institution_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.institution_lbl.setObjectName("institution_lbl")
        self.column_1.addWidget(self.institution_lbl, 1, 0, 1, 1)
        self.lab_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.lab_lbl.setObjectName("lab_lbl")
        self.column_1.addWidget(self.lab_lbl, 2, 0, 1, 1)
        self.related_publications_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.related_publications_lbl.setObjectName("related_publications_lbl")
        self.column_1.addWidget(self.related_publications_lbl, 5, 0, 1, 1)
        self.keywords_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.keywords_lbl.setObjectName("keywords_lbl")
        self.column_1.addWidget(self.keywords_lbl, 3, 0, 1, 1)
        self.lab_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lab_le.setObjectName("lab_le")
        self.column_1.addWidget(self.lab_le, 2, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(400, 10, 401, 541))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.column_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.column_2.setContentsMargins(0, 0, 0, 0)
        self.column_2.setObjectName("column_2")
        self.notes_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.notes_pte.setObjectName("notes_pte")
        self.column_2.addWidget(self.notes_pte, 0, 1, 1, 1)
        self.notes_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.notes_lbl.setObjectName("notes_lbl")
        self.column_2.addWidget(self.notes_lbl, 0, 0, 1, 1)
        self.experiment_description_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.experiment_description_lbl.setObjectName("experiment_description_lbl")
        self.column_2.addWidget(self.experiment_description_lbl, 1, 0, 1, 1)
        self.experiment_description_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.experiment_description_pte.setObjectName("experiment_description_pte")
        self.column_2.addWidget(self.experiment_description_pte, 1, 1, 1, 1)
        self.line_1 = QtWidgets.QFrame(self.frame)
        self.line_1.setGeometry(QtCore.QRect(810, 10, 16, 541))
        self.line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(820, 10, 571, 521))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.column_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.column_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.column_3.setContentsMargins(0, 0, 0, 0)
        self.column_3.setObjectName("column_3")
        self.session_id_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.session_id_lbl.setObjectName("session_id_lbl")
        self.column_3.addWidget(self.session_id_lbl, 0, 0, 1, 1)
        self.pharmacology_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.pharmacology_lbl.setObjectName("pharmacology_lbl")
        self.column_3.addWidget(self.pharmacology_lbl, 4, 0, 1, 1)
        self.timestamps_reference_time_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.timestamps_reference_time_lbl.setObjectName("timestamps_reference_time_lbl")
        self.column_3.addWidget(self.timestamps_reference_time_lbl, 1, 0, 1, 1)
        self.surgery_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.surgery_lbl.setObjectName("surgery_lbl")
        self.column_3.addWidget(self.surgery_lbl, 2, 0, 1, 1)
        self.session_id_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.session_id_le.setObjectName("session_id_le")
        self.column_3.addWidget(self.session_id_le, 0, 1, 1, 1)
        self.surgery_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.surgery_le.setObjectName("surgery_le")
        self.column_3.addWidget(self.surgery_le, 2, 1, 1, 1)
        self.virus_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.virus_le.setObjectName("virus_le")
        self.column_3.addWidget(self.virus_le, 3, 1, 1, 1)
        self.pharmacology_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.pharmacology_le.setObjectName("pharmacology_le")
        self.column_3.addWidget(self.pharmacology_le, 4, 1, 1, 1)
        self.virus_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.virus_lbl.setObjectName("virus_lbl")
        self.column_3.addWidget(self.virus_lbl, 3, 0, 1, 1)
        self.timestamps_reference_time_dte = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_2)
        self.timestamps_reference_time_dte.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.timestamps_reference_time_dte.setTimeSpec(QtCore.Qt.TimeZone)
        self.timestamps_reference_time_dte.setObjectName("timestamps_reference_time_dte")
        self.column_3.addWidget(self.timestamps_reference_time_dte, 1, 1, 1, 1)
        self.session_description_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.session_description_pte.setObjectName("session_description_pte")
        self.column_3.addWidget(self.session_description_pte, 6, 1, 1, 1)
        self.session_start_time_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.session_start_time_lbl.setObjectName("session_start_time_lbl")
        self.column_3.addWidget(self.session_start_time_lbl, 5, 0, 1, 1)
        self.session_start_time_dte = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_2)
        self.session_start_time_dte.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.session_start_time_dte.setTimeSpec(QtCore.Qt.TimeZone)
        self.session_start_time_dte.setObjectName("session_start_time_dte")
        self.column_3.addWidget(self.session_start_time_dte, 5, 1, 1, 1)
        self.session_description_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.session_description_lbl.setObjectName("session_description_lbl")
        self.column_3.addWidget(self.session_description_lbl, 6, 0, 1, 1)
        self.column_3.setColumnMinimumWidth(0, 200)
        self.column_3.setColumnMinimumWidth(1, 200)
        self.update_btn = QtWidgets.QPushButton(self.frame)
        self.update_btn.setGeometry(QtCore.QRect(1260, 540, 150, 32))
        self.update_btn.setMinimumSize(QtCore.QSize(0, 11))
        self.update_btn.setObjectName("update_btn")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.experimenter_lbl.setText(_translate("Dialog", "Experimenter"))
        self.protocol_lbl.setText(_translate("Dialog", "Protocol"))
        self.institution_lbl.setText(_translate("Dialog", "Institution"))
        self.lab_lbl.setText(_translate("Dialog", "Lab"))
        self.related_publications_lbl.setText(_translate("Dialog", "Related \n"
        "publications"))
        self.keywords_lbl.setText(_translate("Dialog", "Keywords"))
        self.notes_lbl.setText(_translate("Dialog", "Notes"))
        self.experiment_description_lbl.setText(_translate("Dialog", "Experiment \n"
        "Description"))
        self.session_id_lbl.setText(_translate("Dialog", "Session ID"))
        self.pharmacology_lbl.setText(_translate("Dialog", "Pharmacology"))
        self.timestamps_reference_time_lbl.setText(_translate("Dialog", "Timestamps Reference Time"))
        self.surgery_lbl.setText(_translate("Dialog", "Surgery"))
        self.virus_lbl.setText(_translate("Dialog", "Virus"))
        self.timestamps_reference_time_dte.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd h:mm AP"))
        self.session_start_time_lbl.setText(_translate("Dialog", "Session Start Time"))
        self.session_start_time_dte.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd h:mm AP"))
        self.session_description_lbl.setText(_translate("Dialog", "Session\n"
        "Description"))
        self.update_btn.setText(_translate("Dialog", "Update/Verify"))

        

    
    def initializePage(self):

        #Passing Matlab Headerfile
        global headerfilename
        headerinformation = scipy.io.loadmat(headerfilename)
        #scipy.io.whosmat(headerinformation)
        headerdictionary = headerinformation['headerfile']
        
        print(headerdictionary.item(0))

        #loading values from the headerfile
        experimenter = headerdictionary[0,0]['Experimenter']
        experimenter = experimenter[0]
        institution = headerdictionary[0,0]['Institution']
        institution = institution[0]
        lab = headerdictionary[0,0]['Lab']
        lab = lab[0]
        keywords = headerdictionary[0,0]['Keywords']
        keywords = keywords[0]
        protocol = headerdictionary[0,0]['Protocol']
        protocol = protocol[0]
        related_publications = headerdictionary[0,0]['Related_Publications']
        related_publications = related_publications[0]
        notes = headerdictionary[0,0]['Notes']
        notes = notes[0]
        experiment_description = headerdictionary[0,0]['Experiment_Description']
        experiment_description = experiment_description[0]
        session_description = headerdictionary[0,0]['Session_Description']
        session_description = session_description[0]
        session_id = headerdictionary[0,0]['Session_ID']
        session_id = session_id[0]
        
        timestamps_reference_time = headerdictionary[0,0]['timestamps_reference_time']
        timestamps_reference_time = str(timestamps_reference_time)
        timestamps_reference_time = timestamps_reference_time[2:-2]
        timestamps_reference_time_object = datetime.datetime.strptime(timestamps_reference_time,'%Y-%m-%d %H:%M:%S.%f%z')
        self.timestamps_reference_time_dte.setDisplayFormat('yyyy-MM-dd hh:mm:ss.zzzzzz t')

        
        session_start_time = headerdictionary[0,0]['session_start_time']
        session_start_time = str(session_start_time)
        session_start_time = session_start_time[2:-2]
        session_start_time_object = datetime.datetime.strptime(session_start_time,'%Y-%m-%d %H:%M:%S.%f%z')        
        self.session_start_time_dte.setDisplayFormat('yyyy-MM-dd hh:mm:ss.zzzzzz t')
        print(session_start_time)

        surgery = headerdictionary[0,0]['Surgery']
        surgery = surgery[0]
        virus = headerdictionary[0,0]['Virus']
        virus = virus[0]
        pharmacology = headerdictionary[0,0]['Pharmacology']
        pharmacology = pharmacology[0]


        #print(timestamps_reference_time)

        #Adding text from file to lineedits
        self.experimenter_le.setText(str(experimenter))
        self.institution_le.setText(str(institution))
        self.lab_le.setText(str(lab))
        self.keywords_le.setText(str(keywords))
        self.protocol_le.setText(str(protocol))
        self.related_publications_le.setText(str(related_publications))
        self.notes_pte.setPlainText(str(notes))
        self.experiment_description_pte.setPlainText(str(experiment_description)) 
        self.session_description_pte.setPlainText(str(session_description))
        self.session_id_le.setText(str(session_id))
        self.timestamps_reference_time_dte.setDateTime(timestamps_reference_time_object)
        self.session_start_time_dte.setDateTime(session_start_time_object)
        self.surgery_le.setText(str(surgery))
        self.virus_le.setText(str(virus))
        self.pharmacology_le.setText(str(pharmacology))    

        #Hook up the button
        self.update_btn.clicked.connect(self.on_click)


    def on_click(self):
        global nwbfile
        global identifier
        global session_description
        global session_start_time
        global timestamps_reference_time

        #coercing start time format     
        session_start_time = self.session_start_time_dte.dateTime()
        session_start_time = session_start_time.toPyDateTime()
        #print(session_start_time)

        timestamps_reference_time = self.timestamps_reference_time_dte.dateTime()
        timestamps_reference_time = timestamps_reference_time.toPyDateTime()
        print(type(timestamps_reference_time))

        #Setting the value of session_descriptoin inside the nwbfile class didn't work.  Putting it here does.
        session_description = self.session_description_pte.toPlainText()

        nwbfile = pynwb.NWBFile(
            session_description,
            identifier,
            session_start_time,
            file_create_date = datetime.datetime.now(tzlocal()),
            #timestamps_reference_time = timestamps_reference_time,
            experimenter = str(self.experimenter_le.text()),
            institution = str(self.institution_le.text()), 
            lab = str(self.lab_le.text()),
            keywords = list(self.keywords_le.text()),
            protocol = str(self.protocol_le.text()),
            related_publications = str(self.related_publications_le.text()),
            notes = str(self.notes_pte.toPlainText()),
            experiment_description = str(self.experiment_description_pte.toPlainText()),
            session_id = str(self.session_id_le.text()),
            surgery = str(self.surgery_le.text()),
            virus = str(self.virus_le.text()),
            pharmacology = str(self.pharmacology_le.text())) #Add timestamps reference time and experiment start time
        
        self.update_btn.setText("Updated")
        self.update_btn.clicked.disconnect()
        print(nwbfile)
        print(nwbfile.session_description)
        print(session_description)


#code for the SUBJECT TABLE
class SubjectTable(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(SubjectTable, self).__init__(parent)

        #add some labels
       
        self.age_lbl = QtWidgets.QLabel()
        self.desription_lbl = QtWidgets.QLabel()
        self.genotype_lbl = QtWidgets.QLabel()
        self.sex_lbl = QtWidgets.QLabel()
        self.species_lbl = QtWidgets.QLabel()
        self.subject_id_lbl = QtWidgets.QLabel()
        self.weight_lbl = QtWidgets.QLabel()
        self.label8 = QtWidgets.QLabel()

        #Adding single-line text boxes

        self.age_le = QtWidgets.QLineEdit()
        self.description_le = QtWidgets.QLineEdit()
        self.genotype_le = QtWidgets.QLineEdit()
        self.sex_le = QtWidgets.QLineEdit()
        self.species_le = QtWidgets.QLineEdit()
        self.subject_id_le = QtWidgets.QLineEdit()
        self.weight_le = QtWidgets.QLineEdit()
        self.lineedit8 = QtWidgets.QLineEdit()

        #Adding buttons
        self.update_btn = QtWidgets.QPushButton()
        self.update_btn.setObjectName("update_btn")
        self.update_btn.clicked.connect(self.on_click)
        self.update_btn.setText("Update/Verify Values")    

       #Adding Labels, button, and Line edits to the layout
    
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.age_lbl)
        layout.addWidget(self.age_le)
        layout.addWidget(self.desription_lbl)
        layout.addWidget(self.description_le)
        layout.addWidget(self.genotype_lbl)
        layout.addWidget(self.genotype_le)   
        layout.addWidget(self.sex_lbl)
        layout.addWidget(self.sex_le)        
        layout.addWidget(self.species_lbl)
        layout.addWidget(self.species_le)
        layout.addWidget(self.subject_id_lbl)
        layout.addWidget(self.subject_id_le)
        layout.addWidget(self.weight_lbl)
        layout.addWidget(self.weight_le)
        layout.addWidget(self.update_btn)   
  
        self.update_btn.clicked.connect(self.on_click)
        self.setLayout(layout)

    #Do stuff that happens when the page loads
    def initializePage(self):
        #loading data from subject table in headerfile
        global headerfilename
        headerinformation = scipy.io.loadmat(headerfilename)
        subjectdictionary = headerinformation['subjectTable']

        #extracting subject table variables
        age = subjectdictionary[0,0]['age']
        age = age[0]
        description = subjectdictionary[0,0]['description']
        description = description[0]
        genotype = subjectdictionary[0,0]['genotype']
        genotype = genotype[0]
        sex = subjectdictionary[0,0]['sex']
        sex = sex[0]
        species = subjectdictionary[0,0]['species']
        species = species[0]
        subject_id = subjectdictionary[0,0]['subject_id']
        subject_id = subject_id[0]
        weight = subjectdictionary[0,0]['weight']
        weight = weight[0]

       
        #add words to the labels
        self.age_lbl.setText("Age:")
        self.desription_lbl.setText("Description:")
        self.genotype_lbl.setText("Genotype:")
        self.sex_lbl.setText("Sex:")
        self.species_lbl.setText("Species:")
        self.subject_id_lbl.setText("Subject ID:")
        self.weight_lbl.setText("Weight:")
        #consider adding DOB here

        #add words to button
        self.update_btn.setText("Update/Verify")

        #Adding text from file
        self.age_le.setText(str(age))
        self.description_le.setText(str(description))
        self.genotype_le.setText(str(genotype))
        self.sex_le.setText(str(sex))
        self.species_le.setText(str(species))
        self.subject_id_le.setText(str(subject_id))
        self.weight_le.setText(str(weight))
        
        
    
    #Update values from edit fields, populate the subject table, add to the nwbfile
    def on_click(self):
        self.update_btn.clicked.connect(self.on_click)
        global subject
        subject = pynwb.file.Subject(
            age = str(self.age_le.text()), 
            description = str(self.description_le.text()), 
            genotype = str(self.genotype_le.text()), 
            sex = str(self.sex_le.text()), 
            subject_id = str(self.subject_id_le.text()), 
            weight = str(self.weight_le.text())
            )
        global nwbfile
        #We include the first three fields because NWB validates for them
        nwbfile = pynwb.NWBFile(
            session_description = session_description,
            identifier = identifier,
            session_start_time = datetime.datetime(2017, 4, 3, 11, tzinfo=tzlocal()), #Fix this placeholder
            subject = subject)
        print(nwbfile.subject)
        self.update_btn.setText("Updated")
        self.update_btn.clicked.disconnect()
        

#code for the Wecome Page 2
class Welcome2(QtWidgets.QWizardPage):
    def __init__(self, parent=None):        
        super(Welcome2, self).__init__(parent)

        self.setObjectName("Dialog")
        self.resize(300, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 9, 400, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.HeaderDataAdded = QtWidgets.QLabel(self.gridLayoutWidget)
        self.HeaderDataAdded.setObjectName("HeaderDataAdded")
        self.gridLayout.addWidget(self.HeaderDataAdded, 1, 0, 1, 1)
        self.SelectNextDataType = QtWidgets.QLabel(self.gridLayoutWidget)
        self.SelectNextDataType.setObjectName("SelectNextDataType")
        self.gridLayout.addWidget(self.SelectNextDataType, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.DataTypeSelector = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.DataTypeSelector.setObjectName("DataTypeSelector")
        self.DataTypeSelector.addItem("")
        self.DataTypeSelector.addItem("")
        self.gridLayout.addWidget(self.DataTypeSelector, 4, 0, 1, 1)
        self.SaveBtn = QtWidgets.QPushButton(self)
        self.SaveBtn.setGeometry(QtCore.QRect(200, 210, 100, 75))
        self.SaveBtn.setObjectName("SaveBtn")
        self.SaveBtn.clicked.connect(self.on_click)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.HeaderDataAdded.setText(_translate("Dialog", "Header data added!"))
        self.SelectNextDataType.setText(_translate("Dialog", "Select next data type:"))
        self.DataTypeSelector.setItemText(0, _translate("Dialog", "Widefield and 2P data"))
        self.DataTypeSelector.setItemText(1, _translate("Dialog", "Matlab file with multiple timeseries"))
        self.SaveBtn.setText(_translate("Dialog", "Save File"))


    def on_click(self):
        self.SaveBtn.clicked.connect(self.on_click)        
     
        #create global variable for NWB file and populate the filename
        global nwbfile
        with NWBHDF5IO(identifier + '.nwb', 'w') as io:
            io.write(nwbfile)
        print(nwbfile)
        print(nwbfile.identifier)

#code for WideField/2p page 1
class WidefieldStep1(QtWidgets.QWizardPage):
    def __init__(self, parent=None):        
        super(WidefieldStep1, self).__init__(parent)

        self.setObjectName("Dialog")
        self.resize(1147, 668)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1111, 800))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(450, 20, 20, 551))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 100, 361, 271))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.column_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.column_1.setContentsMargins(0, 0, 0, 0)
        self.column_1.setObjectName("column_1")
        self.description_le2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.description_le2.setObjectName("description_le2")
        self.column_1.addWidget(self.description_le2, 1, 1, 1, 1)
        self.emission_lambda_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.emission_lambda_lbl.setObjectName("emission_lambda_lbl")
        self.column_1.addWidget(self.emission_lambda_lbl, 2, 0, 1, 1)
        self.description_lbl2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.description_lbl2.setObjectName("description_lbl2")
        self.column_1.addWidget(self.description_lbl2, 1, 0, 1, 1)
        self.name_le2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.name_le2.setObjectName("name_le2")
        self.column_1.addWidget(self.name_le2, 0, 1, 1, 1)
        self.emission_lambda_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.emission_lambda_le.setObjectName("emission_lambda_le")
        self.column_1.addWidget(self.emission_lambda_le, 2, 1, 1, 1)
        self.name_lbl2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.name_lbl2.setObjectName("name_lbl2")
        self.column_1.addWidget(self.name_lbl2, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(590, 120, 441, 461))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.column_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.column_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.column_2.setContentsMargins(0, 0, 0, 0)
        self.column_2.setObjectName("column_2")
        self.location_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.location_lbl.setObjectName("location_lbl")
        self.column_2.addWidget(self.location_lbl, 9, 0, 1, 1)
        self.location_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.location_le.setObjectName("location_le")
        self.column_2.addWidget(self.location_le, 9, 1, 1, 1)
        self.indicator_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.indicator_lbl.setObjectName("indicator_lbl")
        self.column_2.addWidget(self.indicator_lbl, 6, 0, 1, 1)
        self.unit_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.unit_le.setObjectName("unit_le")
        self.column_2.addWidget(self.unit_le, 7, 1, 1, 1)
        self.unit_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.unit_lbl.setObjectName("unit_lbl")
        self.column_2.addWidget(self.unit_lbl, 7, 0, 1, 1)
        self.reference_frame_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.reference_frame_lbl.setObjectName("reference_frame_lbl")
        self.column_2.addWidget(self.reference_frame_lbl, 8, 0, 1, 1)
        self.device_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.device_le.setObjectName("device_le")
        self.column_2.addWidget(self.device_le, 2, 1, 1, 1)
        self.conversion_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.conversion_le.setObjectName("conversion_le")
        self.column_2.addWidget(self.conversion_le, 5, 1, 1, 1)
        self.reference_frame_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.reference_frame_le.setObjectName("reference_frame_le")
        self.column_2.addWidget(self.reference_frame_le, 8, 1, 1, 1)
        self.conversion_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.conversion_lbl.setObjectName("conversion_lbl")
        self.column_2.addWidget(self.conversion_lbl, 5, 0, 1, 1)
        self.indicator_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.indicator_le.setObjectName("indicator_le")
        self.column_2.addWidget(self.indicator_le, 6, 1, 1, 1)
        self.imaging_rate_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.imaging_rate_le.setObjectName("imaging_rate_le")
        self.column_2.addWidget(self.imaging_rate_le, 4, 1, 1, 1)
        self.excitation_lambda_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.excitation_lambda_lbl.setObjectName("excitation_lambda_lbl")
        self.column_2.addWidget(self.excitation_lambda_lbl, 3, 0, 1, 1)
        self.name_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.name_lbl.setObjectName("name_lbl")
        self.column_2.addWidget(self.name_lbl, 0, 0, 1, 1)
        self.device_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.device_lbl.setObjectName("device_lbl")
        self.column_2.addWidget(self.device_lbl, 2, 0, 1, 1)
        self.excitation_lambda_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.excitation_lambda_le.setObjectName("excitation_lambda_le")
        self.column_2.addWidget(self.excitation_lambda_le, 3, 1, 1, 1)
        self.description_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.description_le.setObjectName("description_le")
        self.column_2.addWidget(self.description_le, 1, 1, 1, 1)
        self.description_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.description_lbl.setObjectName("description_lbl")
        self.column_2.addWidget(self.description_lbl, 1, 0, 1, 1)
        self.imaging_rate_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.imaging_rate_lbl.setObjectName("imaging_rate_lbl")
        self.column_2.addWidget(self.imaging_rate_lbl, 4, 0, 1, 1)
        self.name_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.name_le.setObjectName("name_le")
        self.column_2.addWidget(self.name_le, 0, 1, 1, 1)
        self.update_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.update_btn.setObjectName("update_btn")
        self.column_2.addWidget(self.update_btn, 11, 1, 1, 1)
        self.manifold_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.manifold_le.setObjectName("manifold_le")
        self.column_2.addWidget(self.manifold_le, 10, 1, 1, 1)
        self.manifold_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.manifold_lbl.setObjectName("manifold_lbl")
        self.column_2.addWidget(self.manifold_lbl, 10, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 302, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.optical_channe_lbl_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.optical_channe_lbl_grid.setContentsMargins(0, 0, 0, 0)
        self.optical_channe_lbl_grid.setObjectName("optical_channe_lbl_grid")
        self.optical_channel_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.optical_channel_lbl.setEnabled(False)
        self.optical_channel_lbl.setMinimumSize(QtCore.QSize(300, 0))
        self.optical_channel_lbl.setMaximumSize(QtCore.QSize(16777211, 189))
        self.optical_channel_lbl.setObjectName("optical_channel_lbl")
        self.optical_channe_lbl_grid.addWidget(self.optical_channel_lbl, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(590, 20, 441, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.imaging_plane_lbl_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.imaging_plane_lbl_grid.setContentsMargins(0, 0, 0, 0)
        self.imaging_plane_lbl_grid.setObjectName("imaging_plane_lbl_grid")
        self.optical_channel_lbl_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.optical_channel_lbl_2.setEnabled(False)
        self.optical_channel_lbl_2.setMaximumSize(QtCore.QSize(16777215, 189))
        self.optical_channel_lbl_2.setObjectName("optical_channel_lbl_2")
        self.imaging_plane_lbl_grid.addWidget(self.optical_channel_lbl_2, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.emission_lambda_lbl.setText(_translate("Dialog", "Emission Lamda"))
        self.description_lbl2.setText(_translate("Dialog", "Description"))
        self.name_lbl2.setText(_translate("Dialog", "Name"))
        self.location_lbl.setText(_translate("Dialog", "Location"))
        self.indicator_lbl.setText(_translate("Dialog", "Indicator"))
        self.unit_lbl.setText(_translate("Dialog", "Unit"))
        self.reference_frame_lbl.setText(_translate("Dialog", "Reference Frame"))
        self.conversion_lbl.setText(_translate("Dialog", "Conversion"))
        self.excitation_lambda_lbl.setText(_translate("Dialog", "Excitation Lamda"))
        self.name_lbl.setText(_translate("Dialog", "Name"))
        self.device_lbl.setText(_translate("Dialog", "Device"))
        self.description_lbl.setText(_translate("Dialog", "Description"))
        self.imaging_rate_lbl.setText(_translate("Dialog", "Imaging Rate"))
        self.update_btn.setText(_translate("Dialog", "Update/Verify"))
        self.manifold_lbl.setText(_translate("Dialog", "Manifold"))
        self.optical_channel_lbl.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Optical Channel</span></p></body></html>"))
        self.optical_channel_lbl_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Imaging Plane</span></p></body></html>"))


    #Do stuff that happens when the page loads  <It's important that this comes before retranslateUI()
    def initializePage(self):
        #Passing NWBfile info
        global nwbfile
        self.openFileNameDialog()

        #File name verification error handling

        if 'TwoPhotonMetaData.mat' not in self.fileName:
            file_verify_dialog = QtWidgets.QDialog()
            ui = Ui_file_verify_dialog()
            ui.setupUi(file_verify_dialog)
            file_verify_dialog.show()                 
            rsp = file_verify_dialog.exec_() #The exec statement prevents window closing immediately
            self.initializePage()
            
        else:
            print('File name verified')

        global two_photon_metadata
        two_photon_metadata = self.fileName
        #print(two_photon_metadata) 
        meta_data = scipy.io.loadmat(two_photon_metadata)
        imaging_plane_dictionary = meta_data['imaging_plane']
        optical_channel_dictionary = meta_data['optical_channel']
        print(imaging_plane_dictionary)
        print(optical_channel_dictionary)

        #Unpacking the Optical Channel values 
        name2  = optical_channel_dictionary[0,0]['name']
        name2 = name2[0]
        description2 = optical_channel_dictionary[0,0]['description']
        description2 = description2[0]
        emission_lambda = optical_channel_dictionary[0,0]['emission_lambda']
        emission_lambda = emission_lambda[0]
                
        #Populate line edit fields from metdata file
        self.name_le2.setText(str(name2))
        self.description_le2.setText(str(description2))
        self.emission_lambda_le.setText(str(emission_lambda))

        #Unpacking the Imaging Plane values and storing them in the NWB Imaging plane class
        name = imaging_plane_dictionary[0,0]['name']
        name = name[0]
        description = imaging_plane_dictionary[0,0]['description']
        description = description[0]
        device = imaging_plane_dictionary[0,0]['device']
        device = device[0]
        excitation_lambda = imaging_plane_dictionary[0,0]['excitation_lambda']
        excitation_lambda = excitation_lambda[0]
        imaging_rate = imaging_plane_dictionary[0,0]['imaging_rate']
        imaging_rate = imaging_rate[0]
        indicator = imaging_plane_dictionary[0,0]['indicator']
        indicator = indicator[0]
        location = imaging_plane_dictionary[0,0]['location']
        location = location[0]
        manifold = imaging_plane_dictionary[0,0]['manifold']
        manifold = manifold[0]
        conversion  = imaging_plane_dictionary[0,0]['conversion']
        conversion = conversion[0]
        unit = imaging_plane_dictionary[0,0]['unit']
        unit = unit[0]
        reference_frame = imaging_plane_dictionary[0,0]['reference_frame']
        reference_frame = reference_frame[0]

        #Populate line edit fields from metdata file
        self.name_le.setText(str(name))
        self.description_le.setText(str(description))
        self.device_le.setText(str(device))
        self.excitation_lambda_le.setText(str(excitation_lambda))   
        self.imaging_rate_le.setText(str(imaging_rate))
        self.indicator_le.setText(str(indicator))
        self.location_le.setText(str(location))
        self.manifold_le.setText(str(manifold))
        self.conversion_le.setText(str(conversion))
        self.unit_le.setText(str(unit))
        self.reference_frame_le.setText(str(reference_frame)) 

    #Connect the button here
        self.update_btn.clicked.connect(self.on_click)     


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Load Imaging Metadata", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            print(self.fileName)


    def on_click(self):
              
        global optical_channel
        global imaging_plane
        optical_channel = pynwb.ophys.OpticalChannel(
            str(self.name_le2.text()),
            description = str(self.description_le2.text()),
            emission_lambda = float(self.emission_lambda_le.text()),
            )
            
        imaging_plane = nwbfile.create_imaging_plane(
            name = str(self.name_le.text()),
            optical_channel = optical_channel,
            description = str(self.description_le.text()),
            device =  nwbfile.create_device(self.device_le.text()), #NWB api  wants to create the device field
            excitation_lambda = float(self.excitation_lambda_le.text()),
            imaging_rate = float(self.imaging_rate_le.text()),
            indicator = str(self.indicator_le.text()),
            location = str(self.location_le.text()),
            manifold = self.manifold_le.text().split(","),
            conversion = float(self.conversion_le.text()),
            unit = str(self.unit_le.text()),
            reference_frame = str(self.reference_frame_le.text())
            )

        self.update_btn.setText("Updated")
        self.update_btn.clicked.disconnect()
        #self.update_btn.clicked.connect(self.add_another_nwb)
        print(optical_channel)
        print(imaging_plane.name)


#code for Widefield/2p page 2
class WidefieldStep2(QtWidgets.QWizardPage):
    def __init__(self, parent=None):        
        super(WidefieldStep2, self).__init__(parent)

        self.setObjectName("Dialog")
        self.left_Frame = QtWidgets.QFrame(self)
        self.left_Frame.setGeometry(QtCore.QRect(20, 10, 721, 900))
        self.left_Frame.setMinimumSize(QtCore.QSize(0, 900))
        self.left_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_Frame.setObjectName("left_Frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.left_Frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 341, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.two_photon_series_grid_1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.two_photon_series_grid_1.setContentsMargins(0, 0, 0, 0)
        self.two_photon_series_grid_1.setObjectName("two_photon_series_grid_1")
        self.two_photon_series_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.two_photon_series_lbl.setObjectName("two_photon_series_lbl")
        self.two_photon_series_grid_1.addWidget(self.two_photon_series_lbl, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.left_Frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 671, 651))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.two_photon_series_part1_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.two_photon_series_part1_grid.setContentsMargins(0, 0, 0, 0)
        self.two_photon_series_part1_grid.setObjectName("two_photon_series_part1_grid")
        self.bits_per_pixel_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.bits_per_pixel_le.setObjectName("bits_per_pixel_le")
        self.two_photon_series_part1_grid.addWidget(self.bits_per_pixel_le, 5, 1, 1, 1)
        self.unit_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.unit_lbl.setObjectName("unit_lbl")
        self.two_photon_series_part1_grid.addWidget(self.unit_lbl, 3, 0, 1, 1)
        self.bits_per_pixel_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bits_per_pixel_lbl.setObjectName("bits_per_pixel_lbl")
        self.two_photon_series_part1_grid.addWidget(self.bits_per_pixel_lbl, 5, 0, 1, 1)
        self.field_of_view_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.field_of_view_lbl.setObjectName("field_of_view_lbl")
        self.two_photon_series_part1_grid.addWidget(self.field_of_view_lbl, 4, 0, 1, 1)
        self.dimension_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.dimension_lbl.setObjectName("dimension_lbl")
        self.two_photon_series_part1_grid.addWidget(self.dimension_lbl, 7, 0, 1, 1)
        self.pmt_gain_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.pmt_gain_lbl.setObjectName("pmt_gain_lbl")
        self.two_photon_series_part1_grid.addWidget(self.pmt_gain_lbl, 6, 0, 1, 1)
        self.comments_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.comments_pte.setMaximumSize(QtCore.QSize(16777215, 170))
        self.comments_pte.setObjectName("comments_pte")
        self.two_photon_series_part1_grid.addWidget(self.comments_pte, 2, 1, 1, 1)
        self.comments_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.comments_lbl.setObjectName("comments_lbl")
        self.two_photon_series_part1_grid.addWidget(self.comments_lbl, 2, 0, 1, 1)
        self.name_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.name_lbl.setObjectName("name_lbl")
        self.two_photon_series_part1_grid.addWidget(self.name_lbl, 0, 0, 1, 1)
        self.name_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.name_le.setObjectName("name_le")
        self.two_photon_series_part1_grid.addWidget(self.name_le, 0, 1, 1, 1)
        self.field_of_view_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.field_of_view_le.setObjectName("field_of_view_le")
        self.two_photon_series_part1_grid.addWidget(self.field_of_view_le, 4, 1, 1, 1)
        self.description_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.description_pte.setMaximumSize(QtCore.QSize(16777215, 146))
        self.description_pte.setObjectName("description_pte")
        self.two_photon_series_part1_grid.addWidget(self.description_pte, 1, 1, 1, 1)
        self.unit_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.unit_le.setObjectName("unit_le")
        self.two_photon_series_part1_grid.addWidget(self.unit_le, 3, 1, 1, 1)
        self.description_le = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.description_le.setObjectName("description_le")
        self.two_photon_series_part1_grid.addWidget(self.description_le, 1, 0, 1, 1)
        self.pmt_gain_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.pmt_gain_le.setObjectName("pmt_gain_le")
        self.two_photon_series_part1_grid.addWidget(self.pmt_gain_le, 6, 1, 1, 1)
        self.dimension_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.dimension_le.setObjectName("dimension_le")
        self.two_photon_series_part1_grid.addWidget(self.dimension_le, 7, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(850, 30, 1200, 900))
        self.frame_2.setMinimumSize(QtCore.QSize(1200, 900))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 60, 491, 451))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.two_photon_part2_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.two_photon_part2_grid.setContentsMargins(0, 0, 0, 0)
        self.two_photon_part2_grid.setObjectName("two_photon_part2_grid")
        self.starting_frame_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.starting_frame_le.setObjectName("starting_frame_le")
        self.two_photon_part2_grid.addWidget(self.starting_frame_le, 3, 1, 1, 1)
        self.conversion_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.conversion_le.setObjectName("conversion_le")
        self.two_photon_part2_grid.addWidget(self.conversion_le, 1, 1, 1, 1)
        self.starting_time_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.starting_time_le.setObjectName("starting_time_le")
        self.two_photon_part2_grid.addWidget(self.starting_time_le, 2, 1, 1, 1)
        self.rate_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.rate_le.setObjectName("rate_le")
        self.two_photon_part2_grid.addWidget(self.rate_le, 4, 1, 1, 1)
        self.conversion_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.conversion_lbl.setObjectName("conversion_lbl")
        self.two_photon_part2_grid.addWidget(self.conversion_lbl, 1, 0, 1, 1)
        self.control_description_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.control_description_le.setObjectName("control_description_le")
        self.two_photon_part2_grid.addWidget(self.control_description_le, 7, 1, 1, 1)
        self.scan_line_rate_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.scan_line_rate_le.setObjectName("scan_line_rate_le")
        self.two_photon_part2_grid.addWidget(self.scan_line_rate_le, 5, 1, 1, 1)
        self.control_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.control_le.setObjectName("control_le")
        self.two_photon_part2_grid.addWidget(self.control_le, 6, 1, 1, 1)
        self.rate_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.rate_lbl.setObjectName("rate_lbl")
        self.two_photon_part2_grid.addWidget(self.rate_lbl, 4, 0, 1, 1)
        self.scan_line_rate = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.scan_line_rate.setObjectName("scan_line_rate")
        self.two_photon_part2_grid.addWidget(self.scan_line_rate, 5, 0, 1, 1)
        self.starting_time_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.starting_time_lbl.setObjectName("starting_time_lbl")
        self.two_photon_part2_grid.addWidget(self.starting_time_lbl, 2, 0, 1, 1)
        self.control_description_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.control_description_lbl.setObjectName("control_description_lbl")
        self.two_photon_part2_grid.addWidget(self.control_description_lbl, 7, 0, 1, 1)
        self.resolution_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.resolution_le.setObjectName("resolution_le")
        self.two_photon_part2_grid.addWidget(self.resolution_le, 0, 1, 1, 1)
        self.resolution_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.resolution_lbl.setObjectName("resolution_lbl")
        self.two_photon_part2_grid.addWidget(self.resolution_lbl, 0, 0, 1, 1)
        self.control_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.control_lbl.setObjectName("control_lbl")
        self.two_photon_part2_grid.addWidget(self.control_lbl, 6, 0, 1, 1)
        self.starting_frame_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.starting_frame_lbl.setObjectName("starting_frame_lbl")
        self.two_photon_part2_grid.addWidget(self.starting_frame_lbl, 3, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 520, 251, 51))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.objects_in_file_grid_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.objects_in_file_grid_2.setContentsMargins(0, 0, 0, 0)
        self.objects_in_file_grid_2.setObjectName("objects_in_file_grid_2")
        self.objects_in_file_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.objects_in_file_lbl.setObjectName("objects_in_file_lbl")
        self.objects_in_file_grid_2.addWidget(self.objects_in_file_lbl, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 441, 41))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.two_photon_series_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.two_photon_series_grid.setContentsMargins(0, 0, 0, 0)
        self.two_photon_series_grid.setObjectName("two_photon_series_grid")
        self.two_photon_series2_grid = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.two_photon_series2_grid.setObjectName("two_photon_series2_grid")
        self.two_photon_series_grid.addWidget(self.two_photon_series2_grid, 0, 0, 1, 1)
        self.update_btn = QtWidgets.QPushButton(self.frame_2)
        self.update_btn.setGeometry(QtCore.QRect(10, 700, 150, 30))
        self.update_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.update_btn.setObjectName("update_btn")
        self.save_btn = QtWidgets.QPushButton(self.frame_2)
        self.save_btn.setGeometry(QtCore.QRect(310, 700, 150, 30))
        self.save_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.save_btn.setObjectName("save_btn")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 590, 521, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.objects_in_file_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.objects_in_file_grid.setContentsMargins(0, 0, 0, 0)
        self.objects_in_file_grid.setObjectName("objects_in_file_grid")
        self.path_to_image_stack_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.path_to_image_stack_lbl.setObjectName("path_to_image_stack_lbl")
        self.objects_in_file_grid.addWidget(self.path_to_image_stack_lbl, 1, 0, 1, 1)
        self.path_to_stack_updates_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.path_to_stack_updates_lbl.setObjectName("path_to_stack_updates_lbl")
        self.objects_in_file_grid.addWidget(self.path_to_stack_updates_lbl, 1, 1, 1, 1)
        self.imaging_plane_updates_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.imaging_plane_updates_lbl.setObjectName("imaging_plane_updates_lbl")
        self.objects_in_file_grid.addWidget(self.imaging_plane_updates_lbl, 0, 1, 1, 1)
        self.imaging_plane_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.imaging_plane_lbl.setObjectName("imaging_plane_lbl")
        self.objects_in_file_grid.addWidget(self.imaging_plane_lbl, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.two_photon_series_lbl.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Two Photon Series</span></p></body></html>"))
        self.unit_lbl.setText(_translate("Dialog", "Unit"))
        self.bits_per_pixel_lbl.setText(_translate("Dialog", "Bits Per Pixel"))
        self.field_of_view_lbl.setText(_translate("Dialog", "Field of View"))
        self.dimension_lbl.setText(_translate("Dialog", "Dimension"))
        self.pmt_gain_lbl.setText(_translate("Dialog", "PhotoMultiplier Gain"))
        self.comments_lbl.setText(_translate("Dialog", "Comments"))
        self.name_lbl.setText(_translate("Dialog", "Name"))
        self.description_le.setText(_translate("Dialog", "Description"))
        self.conversion_lbl.setText(_translate("Dialog", "Conversion"))
        self.rate_lbl.setText(_translate("Dialog", "Rate"))
        self.scan_line_rate.setText(_translate("Dialog", "Scan Line Rate"))
        self.starting_time_lbl.setText(_translate("Dialog", "Starting Time"))
        self.control_description_lbl.setText(_translate("Dialog", "Control Description"))
        self.resolution_lbl.setText(_translate("Dialog", "Resolution"))
        self.control_lbl.setText(_translate("Dialog", "Control"))
        self.starting_frame_lbl.setText(_translate("Dialog", "Starting Frame"))
        self.objects_in_file_lbl.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Objects in File</span></p></body></html>"))
        self.two_photon_series2_grid.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Two Photon Series</span></p></body></html>"))
        self.update_btn.setText(_translate("Dialog", "Update/Verify"))
        self.save_btn.setText(_translate("Dialog", "Save"))
        self.path_to_image_stack_lbl.setText(_translate("Dialog", "Path to Image Stack:"))
        self.path_to_stack_updates_lbl.setText(_translate("Dialog", "path_to_stack_updates"))
        self.imaging_plane_updates_lbl.setText(_translate("Dialog", "imaging_plane_updates"))
        self.imaging_plane_lbl.setText(_translate("Dialog", "Imaging Plane:"))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Select Image Stack", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            print(self.fileName)

    #Do stuff that happens when the page loads
    def initializePage(self):
        self.openFileNameDialog()
        
        if '.tif' not in self.fileName:
            file_verify_dialog = QtWidgets.QDialog()
            ui = Ui_file_verify_dialog()
            ui.setupUi(file_verify_dialog)
            file_verify_dialog.show()                 
            rsp = file_verify_dialog.exec_() #The exec statement prevents window closing immediately
            self.initializePage()
            
        else:
            print('file .tif verified')

        global tiff_stack
        tiff_stack = self.fileName
        print(tiff_stack)

        #Bringing in the two photon series metadata
        global two_photon_metadata
        global starting_time
        global imaging_plane
        meta_data = scipy.io.loadmat(two_photon_metadata)
        two_photon_series_dictionary = meta_data['two_photon_series']

        #Extracting dictionary values
        name = two_photon_series_dictionary[0,0]['name']
        name = name [0]
        description = two_photon_series_dictionary[0,0]['description']
        description = description[0]
        comments = two_photon_series_dictionary[0,0]['comments']
        comments = comments[0]
        unit = two_photon_series_dictionary[0,0]['unit']
        unit = unit[0]
        field_of_view = two_photon_series_dictionary[0,0]['field_of_view']
        field_of_view = field_of_view[0]
        pmt_gain = two_photon_series_dictionary[0,0]['pmt_gain']
        pmt_gain = pmt_gain[0]
        scan_line_rate = two_photon_series_dictionary[0,0]['scan_line_rate']
        scan_line_rate = scan_line_rate[0]
        starting_frame = two_photon_series_dictionary[0,0]['starting_frame']
        starting_frame = starting_frame[0]
        bits_per_pixel = two_photon_series_dictionary[0,0]['bits_per_pixel']
        bits_per_pixel = bits_per_pixel[0]
        dimension = two_photon_series_dictionary[0,0]['dimension']
        dimension = dimension[0]
        resolution = two_photon_series_dictionary[0,0]['resolution']
        resolution = resolution[0]
        conversion = two_photon_series_dictionary[0,0]['conversion']
        conversion = conversion[0]
        starting_time = two_photon_series_dictionary[0,0]['starting_time']
        starting_time = starting_time[0]
        rate = two_photon_series_dictionary[0,0]['rate']
        rate = rate[0]
        control = two_photon_series_dictionary[0,0]['control']
        control = control[0]
        control_description = two_photon_series_dictionary[0,0]['control_description']
        control_description = control_description[0]

        #Populate line edit fields from metdata file
        self.name_le.setText(str(name))
        self.description_pte.setPlainText(str(description))
        self.comments_pte.setPlainText(str(comments))
        self.unit_le.setText(str(unit))
        self.field_of_view_le.setText(field_of_view)
        self.pmt_gain_le.setText(str(pmt_gain))
        self.scan_line_rate_le.setText(str(scan_line_rate))
        self.starting_frame_le.setText(str(starting_frame))
        self.bits_per_pixel_le.setText(str(bits_per_pixel))
        self.dimension_le.setText(dimension)
        self.resolution_le.setText(str(resolution))
        self.conversion_le.setText(str(conversion))
        self.starting_time_le.setText(str(starting_time))
        self.rate_le.setText(str(rate))
        self.control_le.setText(str(control))
        self.control_description_le.setText(str(control_description))

        #Line Edits display file contents
        self.path_to_stack_updates_lbl.setText(tiff_stack)
        self.imaging_plane_updates_lbl.setText(str(imaging_plane))
             

        #Button connections go here, prior to retranslate
        self.update_btn.clicked.connect(self.on_click)
        self.save_btn.clicked.connect(self.save_on_click)

        #@pyqtSlot()
    
    def on_click(self):
        global two_photon_metadata
        global starting_time
        meta_data = scipy.io.loadmat(two_photon_metadata)
        two_photon_series_dictionary = meta_data['two_photon_series']
               
        global tiff_stack
        global two_photon_series
        
        two_photon_series = pynwb.ophys.TwoPhotonSeries( 
            name = str(self.name_le.text()),
            imaging_plane = imaging_plane,
            format = 'tiff',
            field_of_view = self.field_of_view_le.text().split(","),
            dimension = self.dimension_le.text().split(","),
            external_file = [tiff_stack],
            bits_per_pixel = int(self.bits_per_pixel_le.text()),
            resolution = float(self.resolution_le.text()),
            conversion = float(self.conversion_le.text()),
            starting_time = float(self.starting_time_le.text()),
            starting_frame = list(self.starting_frame_le.text()),
            rate = float(self.rate_le.text()),
            comments = str(self.comments_pte.toPlainText()),
            description = str(self.description_pte.toPlainText()),
            unit = str(self.unit_le.text()),
            control = self.control_le.text().split(","),
            control_description = self.control_description_le.text().split(",")
        )
        
        nwbfile.add_acquisition(two_photon_series)
        self.update_btn.setText("Updated")
        self.update_btn.clicked.disconnect()
        print(two_photon_series)

    def save_on_click(self): 
        #create global variables for NWB classes and write them to the file
        global nwbfile
        global imaging_plane
        global tiff_stack
        global two_photon_series


        with NWBHDF5IO(identifier + '.nwb', 'w') as io:
            io.write(nwbfile)
        print(nwbfile)
        self.save_btn.setText("Saved")
        self.save_btn.clicked.disconnect()

#code for Widefield/2p page 3
class WidefieldStep3(QtWidgets.QWizardPage):
    def __init__(self, parent=None):        
        super(WidefieldStep3, self).__init__(parent)

        self.setObjectName("Dialog")
        self.resize(1800, 1200)
        self.step2_gb = QtWidgets.QGroupBox(self)
        self.step2_gb.setGeometry(QtCore.QRect(10, 240, 341, 321))
        self.step2_gb.setObjectName("step2_gb")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.step2_gb)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 331, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.step2_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.step2_grid.setContentsMargins(0, 0, 0, 0)
        self.step2_grid.setObjectName("step2_grid")
        self.image_stacks_cb_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.image_stacks_cb_lbl.setObjectName("image_stacks_cb_lbl")
        self.step2_grid.addWidget(self.image_stacks_cb_lbl, 2, 0, 1, 1)
        self.image_stacks_cb = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.image_stacks_cb.setObjectName("image_stacks_cb")
        self.step2_grid.addWidget(self.image_stacks_cb, 2, 1, 1, 1)
        self.name2_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.name2_le.setObjectName("name2_le")
        self.step2_grid.addWidget(self.name2_le, 0, 1, 1, 1)
        self.description2_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.description2_lbl.setObjectName("description2_lbl")
        self.step2_grid.addWidget(self.description2_lbl, 1, 0, 1, 1)
        self.name2_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.name2_lbl.setObjectName("name2_lbl")
        self.step2_grid.addWidget(self.name2_lbl, 0, 0, 1, 1)
        self.id_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.id_lbl.setObjectName("id_lbl")
        self.step2_grid.addWidget(self.id_lbl, 3, 0, 1, 1)
        self.id_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.id_le.setObjectName("id_le")
        self.step2_grid.addWidget(self.id_le, 3, 1, 1, 1)
        self.description2_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.description2_pte.setMinimumSize(QtCore.QSize(0, 100))
        self.description2_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.description2_pte.setObjectName("description2_pte")
        self.step2_grid.addWidget(self.description2_pte, 1, 1, 1, 1)
        self.step4_gb = QtWidgets.QGroupBox(self)
        self.step4_gb.setGeometry(QtCore.QRect(360, 40, 481, 771))
        self.step4_gb.setObjectName("step4_gb")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.step4_gb)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(50, 30, 431, 731))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.roi_response_series_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.roi_response_series_grid.setContentsMargins(0, 0, 0, 0)
        self.roi_response_series_grid.setObjectName("roi_response_series_grid")
        self.comments_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.comments_lbl.setObjectName("comments_lbl")
        self.roi_response_series_grid.addWidget(self.comments_lbl, 7, 0, 1, 1)
        self.name3_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.name3_lbl.setObjectName("name3_lbl")
        self.roi_response_series_grid.addWidget(self.name3_lbl, 0, 0, 1, 1)
        self.name3_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.name3_le.setObjectName("name3_le")
        self.roi_response_series_grid.addWidget(self.name3_le, 0, 1, 1, 1)
        self.description3_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.description3_lbl.setObjectName("description3_lbl")
        self.roi_response_series_grid.addWidget(self.description3_lbl, 1, 0, 1, 1)
        self.rate_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.rate_lbl.setObjectName("rate_lbl")
        self.roi_response_series_grid.addWidget(self.rate_lbl, 6, 0, 1, 1)
        self.starting_time_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.starting_time_lbl.setObjectName("starting_time_lbl")
        self.roi_response_series_grid.addWidget(self.starting_time_lbl, 5, 0, 1, 1)
        self.resolution_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.resolution_lbl.setObjectName("resolution_lbl")
        self.roi_response_series_grid.addWidget(self.resolution_lbl, 3, 0, 1, 1)
        self.conversion_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.conversion_lbl.setObjectName("conversion_lbl")
        self.roi_response_series_grid.addWidget(self.conversion_lbl, 4, 0, 1, 1)
        self.unit_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.unit_lbl.setObjectName("unit_lbl")
        self.roi_response_series_grid.addWidget(self.unit_lbl, 2, 0, 1, 1)
        self.control_description_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.control_description_le.setObjectName("control_description_le")
        self.roi_response_series_grid.addWidget(self.control_description_le, 9, 1, 1, 1)
        self.rate_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.rate_le.setObjectName("rate_le")
        self.roi_response_series_grid.addWidget(self.rate_le, 6, 1, 1, 1)
        self.unit_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.unit_le.setObjectName("unit_le")
        self.roi_response_series_grid.addWidget(self.unit_le, 2, 1, 1, 1)
        self.starting_time_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.starting_time_le.setObjectName("starting_time_le")
        self.roi_response_series_grid.addWidget(self.starting_time_le, 5, 1, 1, 1)
        self.conversion_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.conversion_le.setObjectName("conversion_le")
        self.roi_response_series_grid.addWidget(self.conversion_le, 4, 1, 1, 1)
        self.resolution_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.resolution_le.setObjectName("resolution_le")
        self.roi_response_series_grid.addWidget(self.resolution_le, 3, 1, 1, 1)
        self.control_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.control_lbl.setObjectName("control_lbl")
        self.roi_response_series_grid.addWidget(self.control_lbl, 8, 0, 1, 1)
        self.control_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.control_le.setObjectName("control_le")
        self.roi_response_series_grid.addWidget(self.control_le, 8, 1, 1, 1)
        self.control_description_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.control_description_lbl.setObjectName("control_description_lbl")
        self.roi_response_series_grid.addWidget(self.control_description_lbl, 9, 0, 1, 1)
        self.description3_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.description3_pte.setMinimumSize(QtCore.QSize(0, 100))
        self.description3_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.description3_pte.setObjectName("description3_pte")
        self.roi_response_series_grid.addWidget(self.description3_pte, 1, 1, 1, 1)
        self.comments_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.comments_pte.setMinimumSize(QtCore.QSize(0, 100))
        self.comments_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.comments_pte.setObjectName("comments_pte")
        self.roi_response_series_grid.addWidget(self.comments_pte, 7, 1, 1, 1)
        self.add_roi_gb = QtWidgets.QGroupBox(self)
        self.add_roi_gb.setGeometry(QtCore.QRect(0, 20, 851, 900))
        self.add_roi_gb.setMinimumSize(QtCore.QSize(0, 900))
        self.add_roi_gb.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.add_roi_gb.setObjectName("add_roi_gb")
        self.update_btn = QtWidgets.QPushButton(self.add_roi_gb)
        self.update_btn.setGeometry(QtCore.QRect(690, 800, 150, 30))
        self.update_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.update_btn.setObjectName("update_btn")
        self.step3_gb = QtWidgets.QGroupBox(self.add_roi_gb)
        self.step3_gb.setGeometry(QtCore.QRect(10, 560, 341, 231))
        self.step3_gb.setObjectName("step3_gb")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.step3_gb)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 30, 331, 141))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.roi_type_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.roi_type_grid.setContentsMargins(0, 0, 0, 0)
        self.roi_type_grid.setObjectName("roi_type_grid")
        self.mask_upload_tool = QtWidgets.QToolButton(self.gridLayoutWidget_6)
        self.mask_upload_tool.setMinimumSize(QtCore.QSize(100, 0))
        self.mask_upload_tool.setObjectName("mask_upload_tool")
        self.roi_type_grid.addWidget(self.mask_upload_tool, 0, 1, 1, 1)
        self.mask_upload_lbl = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.mask_upload_lbl.setObjectName("mask_upload_lbl")
        self.roi_type_grid.addWidget(self.mask_upload_lbl, 0, 0, 1, 1)
        self.mask_selector_lbl = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.mask_selector_lbl.setObjectName("mask_selector_lbl")
        self.roi_type_grid.addWidget(self.mask_selector_lbl, 1, 0, 1, 1)
        self.mask_selector_cb = QtWidgets.QComboBox(self.gridLayoutWidget_6)
        self.mask_selector_cb.setMinimumSize(QtCore.QSize(100, 24))
        self.mask_selector_cb.setObjectName("mask_selector_cb")
        self.mask_selector_cb.addItem("")
        self.mask_selector_cb.addItem("")
        self.mask_selector_cb.addItem("")
        self.roi_type_grid.addWidget(self.mask_selector_cb, 1, 1, 1, 1)
        self.dff_upload_tool = QtWidgets.QToolButton(self.gridLayoutWidget_6)
        self.dff_upload_tool.setMinimumSize(QtCore.QSize(100, 0))
        self.dff_upload_tool.setObjectName("dff_upload_tool")
        self.roi_type_grid.addWidget(self.dff_upload_tool, 2, 1, 1, 1)
        self.dff_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.dff_label.setObjectName("dff_label")
        self.roi_type_grid.addWidget(self.dff_label, 2, 0, 1, 1)
        self.step1_gb = QtWidgets.QGroupBox(self.add_roi_gb)
        self.step1_gb.setGeometry(QtCore.QRect(10, 30, 341, 181))
        self.step1_gb.setObjectName("step1_gb")
        self.gridLayoutWidget = QtWidgets.QWidget(self.step1_gb)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 331, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.step1_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.step1_grid.setContentsMargins(0, 0, 0, 0)
        self.step1_grid.setObjectName("step1_grid")
        self.name1_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name1_lbl.setObjectName("name1_lbl")
        self.step1_grid.addWidget(self.name1_lbl, 0, 0, 1, 1)
        self.description1_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.description1_lbl.setObjectName("description1_lbl")
        self.step1_grid.addWidget(self.description1_lbl, 1, 0, 1, 1)
        self.description1_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.description1_le.setObjectName("description1_le")
        self.step1_grid.addWidget(self.description1_le, 1, 1, 1, 1)
        self.name1_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name1_le.setObjectName("name1_le")
        self.step1_grid.addWidget(self.name1_le, 0, 1, 1, 1)
        self.create_btn = QtWidgets.QPushButton(self.step1_gb)
        self.create_btn.setGeometry(QtCore.QRect(210, 150, 75, 23))
        self.create_btn.setObjectName("create_btn")
        self.file_contents_gb = QtWidgets.QGroupBox(self)
        self.file_contents_gb.setGeometry(QtCore.QRect(890, 30, 511, 1000))
        self.file_contents_gb.setMinimumSize(QtCore.QSize(0, 900))
        self.file_contents_gb.setObjectName("file_contents_gb")
        self.roi_table = QtWidgets.QTableWidget(self.file_contents_gb)
        self.roi_table.setGeometry(QtCore.QRect(20, 60, 450, 202))
        self.roi_table.setMinimumSize(QtCore.QSize(450, 200))
        self.roi_table.setMaximumSize(QtCore.QSize(16777211, 16777215))
        self.roi_table.setRowCount(5)
        self.roi_table.setColumnCount(3)
        self.roi_table.setObjectName("roi_table")
        item = QtWidgets.QTableWidgetItem()
        self.roi_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.roi_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.roi_table.setHorizontalHeaderItem(2, item)
        self.save_btn = QtWidgets.QPushButton(self.file_contents_gb)
        self.save_btn.setGeometry(QtCore.QRect(350, 790, 150, 30))
        self.save_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.save_btn.setObjectName("save_btn")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(870, 30, 20, 811))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.add_roi_gb.raise_()
        self.step2_gb.raise_()
        self.step4_gb.raise_()
        self.file_contents_gb.raise_()
        self.line.raise_()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.step2_gb.setTitle(_translate("Dialog", "Step 2: Image and Plane Segmentation"))
        self.image_stacks_cb_lbl.setText(_translate("Dialog", "Image Stacks your \n"
        "ROI applies to:"))
        self.description2_lbl.setText(_translate("Dialog", "Description"))
        self.name2_lbl.setText(_translate("Dialog", "Name"))
        self.id_lbl.setText(_translate("Dialog", "ID (Table Identifiers)"))
        self.step4_gb.setTitle(_translate("Dialog", "Step 4: ROI Response Series"))
        self.comments_lbl.setText(_translate("Dialog", "Comments"))
        self.name3_lbl.setText(_translate("Dialog", "Name"))
        self.description3_lbl.setText(_translate("Dialog", "Description"))
        self.rate_lbl.setText(_translate("Dialog", "Rate"))
        self.starting_time_lbl.setText(_translate("Dialog", "Starting Time"))
        self.resolution_lbl.setText(_translate("Dialog", "Resolution"))
        self.conversion_lbl.setText(_translate("Dialog", "Conversion"))
        self.unit_lbl.setText(_translate("Dialog", "Unit"))
        self.control_lbl.setText(_translate("Dialog", "Control"))
        self.control_description_lbl.setText(_translate("Dialog", "Control Desciption"))
        self.add_roi_gb.setTitle(_translate("Dialog", "Add ROIs"))
        self.update_btn.setText(_translate("Dialog", "Update/Verify"))
        self.step3_gb.setTitle(_translate("Dialog", "Step 3: Upload Mask and dF/F"))
        self.mask_upload_tool.setText(_translate("Dialog", "..."))
        self.mask_upload_lbl.setText(_translate("Dialog", "Upload  ROI Pixel, Voxel, Image Mask"))
        self.mask_selector_lbl.setText(_translate("Dialog", "Select Mask Type:"))
        self.mask_selector_cb.setItemText(0, _translate("Dialog", "Image Mask"))
        self.mask_selector_cb.setItemText(1, _translate("Dialog", "Voxel Mask"))
        self.mask_selector_cb.setItemText(2, _translate("Dialog", "Pixel Mask"))
        self.dff_upload_tool.setText(_translate("Dialog", "..."))
        self.dff_label.setText(_translate("Dialog", "Upload dF/F Trace:"))
        self.step1_gb.setTitle(_translate("Dialog", "Step 1: Create Processing Module"))
        self.name1_lbl.setText(_translate("Dialog", "Name"))
        self.description1_lbl.setText(_translate("Dialog", "Description"))
        self.create_btn.setText(_translate("Dialog", "Create"))
        self.file_contents_gb.setTitle(_translate("Dialog", "File Contents"))
        item = self.roi_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID (region)"))
        item = self.roi_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.roi_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Description"))
        self.save_btn.setText(_translate("Dialog", "Save"))

    #Do stuff that happens when the page loads
    def initializePage(self):
        #unpacking data from config file
        meta_data = scipy.io.loadmat(two_photon_metadata)

        #Extracting dictionary values from processing module
        processing_module = meta_data['processing_module']
        name1 = processing_module[0,0]['name']
        description1 = processing_module[0,0]['description']

        #Extracting dictionary values from plane segmentation
        plane_segmentation = meta_data['plane_segmentation']
        name2 = plane_segmentation[0,0]['name']
        description2 = plane_segmentation[0,0]['description']
        plane_segmentation_id = plane_segmentation[0,0]['ID'] #Id has a python meaning, thus the rename
        plane_segmentation_id = plane_segmentation_id[0] #Removing brackets by retreiving index

        #Extracting dictionary values from ROI response series
        roi_response_series = meta_data['roi_response_series']
        name3 = roi_response_series[0,0]['name']
        description3 = roi_response_series[0,0]['description']
        unit = roi_response_series[0,0]['unit']
        resolution = roi_response_series[0,0]['resolution']
        resolution = resolution[0]
        print(resolution)
        conversion = roi_response_series[0,0]['conversion']
        conversion = conversion[0]
        starting_time = roi_response_series[0,0]['starting_time']
        rate = roi_response_series[0,0]['rate']
        rate = rate[0]
        comments = roi_response_series[0,0]['comments']
        control = roi_response_series[0,0]['control']
        control = control[0]
        control_description = roi_response_series[0,0]['control_description']
        control_description = control_description[0]

        #Populate processing module lineedit fields from metdata file
        self.name1_le.setText(str(name1))
        self.description1_le.setText(str(description1))

        #Populate Image and PlaneSegmentaton lineedit fields from metdata file
        self.name2_le.setText(str(name2))
        self.description2_pte.setPlainText(str(description2))
        self.id_le.setText(str(plane_segmentation_id))

        #Populate ROI response lineedit fields from metdata file
        self.name3_le.setText(str(name3))
        self.description3_pte.setPlainText(str(description3))
        self.unit_le.setText(str(unit))
        self.resolution_le.setText(str(resolution))
        self.conversion_le.setText(str(conversion))
        self.starting_time_le.setText(str(starting_time))
        self.rate_le.setText(str(rate))
        self.comments_pte.setPlainText(str(comments))
        self.control_le.setText(control)
        self.control_description_le.setText(control_description)
        
        #Populate Image Stack selector with image stacks.  Someday this should be a list, and tiff stacks should get names
        global tiff_stack
        self.image_stacks_cb.addItem(str(tiff_stack))

        #Hook up the buttons
        self.mask_upload_tool.clicked.connect(self.on_click_roi)
        self.dff_upload_tool.clicked.connect(self.on_click_dff)
        self.create_btn.clicked.connect(self.on_click_create)
        self.update_btn.clicked.connect(self.on_click_update)
        self.save_btn.clicked.connect(self.on_click_save)
        
    def on_click_create(self):
        global processing_module
        global image_segmentation
        global processing_module
        processing_module = nwbfile.create_processing_module(
            name = str(self.name1_le.text()), 
            description = str(self.description1_le.text())
            )
        self.create_btn.setText("Created")
        self.create_btn.clicked.disconnect()
        print(processing_module)

    def on_click_update(self):
        #This button does many things.  Overview:
        # 1) Create and populate plane segmentation
        # 2) Add ROI mask 
        # 3) Create ROI table Region and add it to QTableWidget
        # 4) Create a fluorescence processing module and data interface
        # 5) Create ROI Response series
        # 6) Create fluorescence module and add a data interface
        # 7) Create dff Response series
       

        #1) Populate NWB planesegmentation class
        global imaging_plane
        global two_photon_series
        global roi_mask
        global starting_time
        global image_segmentation
        global processing_module
        
        #1a Create image segmentation
        image_segmentation = pynwb.ophys.ImageSegmentation(
            name = 'My Image Segmentation (which holds plane segmentations)' #Fix hard coding
        )


        #1b Add image segmenatation as a data interface to the processing module
        processing_module.add_data_interface(image_segmentation)
        
        #1c Create a plane segementation within the imagesegmentation and pass it data
        #There is an unused option to manually add columns to this class.Adding the ROI below creates a column 
        plane_segmentation = image_segmentation.create_plane_segmentation(
            str(self.description2_pte.toPlainText()),
            two_photon_series,
            name = str(self.name2_le.text()),
            imaging_plane = imaging_plane, 
            #reference_images = tiff_stack,  #This wasn't covered in the python tutorial.  Not a required field, but maybe should be used at some point.
            #id = [3,3] #list(self.id_le.text())  #commenting this out triggers an autopopulate of column/row #s
        )  

        #Someday may want to add multiple plane_segmentations to the image segmentation, which expects a list.
        plane_segmentation_list = [plane_segmentation]

 
        #2 Add ROI to plane segmentation
        #Deterimine the type of ROI and add it to the plane segmentation
        roi_type = str(self.mask_selector_cb.currentText()).lower()
        plane_segmentation.add_roi(image_mask = [(0, 0, 1.1), (1, 1, 1.2), (2, 2, 1.3)])
        print(plane_segmentation)

        #3) Create ROI table Region

        #This shouldn't be hard coded, but it needs to be tested with software that does something with the table region.
        global region

        name = '1st ROI Region'
        region = [0]
        description = 'My ROI table region'

        table_region = plane_segmentation.create_roi_table_region(
            description, 
            region, 
            name)
        
        
        self.roi_table.insertRow(1)

        self.roi_table.setItem(1 , 0, QtWidgets.QTableWidgetItem(str(region)))
        self.roi_table.setItem(1 , 1, QtWidgets.QTableWidgetItem(str(name)))
        self.roi_table.setItem(1 , 2, QtWidgets.QTableWidgetItem(str(description)))

        #4:Create fluorescence module and add a data interface
        global fluorescence
        fluorescence = pynwb.ophys.Fluorescence()
        processing_module.add_data_interface(fluorescence)
        
        #5: Create ROI Response series.  Code gets values for ROI Response Series and pass to NWB class
        
        global roi_array
        
        roi_response_series = fluorescence.create_roi_response_series(
            str(self.name3_le.text()),
            roi_array,
            str(self.unit_le.text()),
            table_region, #This adds the table region from step #3
            description = str(self.description3_pte.toPlainText()),
            starting_time = float(starting_time),        
            resolution =  float(self.resolution_le.text()),
            conversion = float(self.conversion_le.text()),
            rate = float(self.rate_le.text()),
            comments = str(self.comments_pte.toPlainText()),
            control = self.control_le.text().split(","),
            control_description = self.control_description_le.text().split(",")
        )

        #6:Create fluorescence module and add a data interface
        global dff_array
        global dff
        dff = pynwb.ophys.DfOverF()
        processing_module.add_data_interface(dff)

        #7: Create Dff. response series.  Code gets values from          
        dff_response_series = dff.create_roi_response_series(
            str(self.name3_le.text()),
            dff_array,
            str(self.unit_le.text()),
            table_region, #This adds the table region from step #3
            description = str(self.description3_pte.toPlainText()),
            starting_time = float(starting_time),        
            resolution =  float(self.resolution_le.text()),
            conversion = float(self.conversion_le.text()),
            rate = float(self.rate_le.text()),
            comments = str(self.comments_pte.toPlainText()),
            control = self.control_le.text().split(","),
            control_description = self.control_description_le.text().split(",")
        )

        self.update_btn.setText("Updated")
        self.update_btn.clicked.disconnect()
        print('woo!')

    def on_click_roi(self):
        self.openFileNameDialog()        
        roi_mask = self.fileName
        global roi_array
        roi_mask = scipy.io.loadmat(roi_mask)
        roi_array = roi_mask['x']#Shouldn't hard code this
        self.mask_upload_tool.clicked.disconnect()
        
        print(roi_array)  

    def on_click_dff(self):
        self.openFileNameDialog()        
        dff_trace = self.fileName
        dff_trace = scipy.io.loadmat(dff_trace)
        global dff_array
        dff_array = dff_trace['x']#Shouldn't hard code this 
        print('this is the dff array') 
        print(dff_array)
        self.dff_upload_tool.clicked.disconnect()

    def on_click_save(self):
        #create global variables for NWB classes and write them to the file
        global nwbfile
        global fluorescence
        global identifier
        global dff
        

        #NWB expects a list when adding processing modules.  Add modules to this list:
        module_list = [fluorescence, dff]

        nwbfile.add_processing_module(module_list)
        with NWBHDF5IO(identifier + '.nwb', 'w') as io:
            io.write(nwbfile)
        print(nwbfile)
        self.save_btn.setText("Saved")
        self.save_btn.clicked.disconnect()
       
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Select ROI Mask or dF/F trace", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            print(self.fileName)  

#Code for MatlabStep1
class MatlabStep1(QtWidgets.QWizardPage):
    def __init__(self, parent=None):        
        super(MatlabStep1, self).__init__(parent)

        self.setObjectName("Dialog")
        self.add_electrode_group_gb = QtWidgets.QGroupBox(self)
        self.add_electrode_group_gb.setGeometry(QtCore.QRect(20, 60, 471, 291))
        self.add_electrode_group_gb.setObjectName("add_electrode_group_gb")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.add_electrode_group_gb)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 19, 441, 261))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.add_electrode_group_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.add_electrode_group_grid.setContentsMargins(0, 0, 0, 0)
        self.add_electrode_group_grid.setObjectName("add_electrode_group_grid")
        self.location_le = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.location_le.setObjectName("location_le")
        self.add_electrode_group_grid.addWidget(self.location_le, 3, 1, 1, 1)
        self.electrode_name_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.electrode_name_lbl.setObjectName("electrode_name_lbl")
        self.add_electrode_group_grid.addWidget(self.electrode_name_lbl, 1, 0, 1, 1)
        self.description_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.description_lbl.setObjectName("description_lbl")
        self.add_electrode_group_grid.addWidget(self.description_lbl, 2, 0, 1, 1)
        self.description_le = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.description_le.setObjectName("description_le")
        self.add_electrode_group_grid.addWidget(self.description_le, 2, 1, 1, 1)
        self.location_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.location_lbl.setObjectName("location_lbl")
        self.add_electrode_group_grid.addWidget(self.location_lbl, 3, 0, 1, 1)
        self.electrode_name_le = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.electrode_name_le.setObjectName("electrode_name_le")
        self.add_electrode_group_grid.addWidget(self.electrode_name_le, 1, 1, 1, 1)
        self.device_le = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.device_le.setObjectName("device_le")
        self.add_electrode_group_grid.addWidget(self.device_le, 0, 1, 1, 1)
        self.device_lbl = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.device_lbl.setObjectName("device_lbl")
        self.add_electrode_group_grid.addWidget(self.device_lbl, 0, 0, 1, 1)
        self.add_electrode_gb = QtWidgets.QGroupBox(self)
        self.add_electrode_gb.setGeometry(QtCore.QRect(20, 360, 471, 451))
        self.add_electrode_gb.setObjectName("add_electrode_gb")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.add_electrode_gb)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(60, 340, 101, 80))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.x_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.x_grid.setContentsMargins(0, 0, 0, 0)
        self.x_grid.setObjectName("x_grid")
        self.x_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.x_le.setObjectName("x_le")
        self.x_grid.addWidget(self.x_le, 0, 1, 1, 1)
        self.x_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.x_lbl.setObjectName("x_lbl")
        self.x_grid.addWidget(self.x_lbl, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.add_electrode_gb)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(160, 340, 101, 80))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.y_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.y_grid.setContentsMargins(0, 0, 0, 0)
        self.y_grid.setObjectName("y_grid")
        self.y_le = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.y_le.setObjectName("y_le")
        self.y_grid.addWidget(self.y_le, 0, 1, 1, 1)
        self.y_lbl = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.y_lbl.setObjectName("y_lbl")
        self.y_grid.addWidget(self.y_lbl, 0, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.add_electrode_gb)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(270, 340, 101, 80))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.z_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.z_grid.setContentsMargins(0, 0, 0, 0)
        self.z_grid.setObjectName("z_grid")
        self.z_le = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.z_le.setObjectName("z_le")
        self.z_grid.addWidget(self.z_le, 0, 1, 1, 1)
        self.z_lbl = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.z_lbl.setObjectName("z_lbl")
        self.z_grid.addWidget(self.z_lbl, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.add_electrode_gb)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 441, 261))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.add_electrode_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.add_electrode_grid.setContentsMargins(0, 0, 0, 0)
        self.add_electrode_grid.setObjectName("add_electrode_grid")
        self.filtering_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.filtering_le.setObjectName("filtering_le")
        self.add_electrode_grid.addWidget(self.filtering_le, 1, 1, 1, 1)
        self.id_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.id_le.setObjectName("id_le")
        self.add_electrode_grid.addWidget(self.id_le, 0, 1, 1, 1)
        self.filtering_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.filtering_lbl.setObjectName("filtering_lbl")
        self.add_electrode_grid.addWidget(self.filtering_lbl, 1, 0, 1, 1)
        self.id_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.id_lbl.setObjectName("id_lbl")
        self.add_electrode_grid.addWidget(self.id_lbl, 0, 0, 1, 1)
        self.location_le_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.location_le_2.setObjectName("location_le_2")
        self.add_electrode_grid.addWidget(self.location_le_2, 2, 1, 1, 1)
        self.location_lbl_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.location_lbl_2.setObjectName("location_lbl_2")
        self.add_electrode_grid.addWidget(self.location_lbl_2, 2, 0, 1, 1)
        self.imp_le = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.imp_le.setObjectName("imp_le")
        self.add_electrode_grid.addWidget(self.imp_le, 3, 1, 1, 1)
        self.imp_lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.imp_lbl.setObjectName("imp_lbl")
        self.add_electrode_grid.addWidget(self.imp_lbl, 3, 0, 1, 1)
        self.electrode_table = QtWidgets.QTableWidget(self)
        self.electrode_table.setGeometry(QtCore.QRect(520, 70, 441, 51))
        self.electrode_table.setObjectName("electrode_table")
        self.electrode_table.setColumnCount(2)
        self.electrode_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.electrode_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.electrode_table.setHorizontalHeaderItem(1, item)
        self.update_btn = QtWidgets.QPushButton(self)
        self.update_btn.setGeometry(QtCore.QRect(780, 630, 161, 31))
        self.update_btn.setObjectName("update_btn")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 471, 51))
        self.label.setObjectName("label")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_electrode_group_gb.setTitle(_translate("Dialog", "Add Electrode Group"))
        self.electrode_name_lbl.setText(_translate("Dialog", "Electrode Name"))
        self.description_lbl.setText(_translate("Dialog", "Description"))
        self.location_lbl.setText(_translate("Dialog", "Location"))
        self.device_lbl.setText(_translate("Dialog", "Device"))
        self.add_electrode_gb.setTitle(_translate("Dialog", "Add Electrode"))
        self.x_lbl.setText(_translate("Dialog", "    x "))
        self.y_lbl.setText(_translate("Dialog", "    y "))
        self.z_lbl.setText(_translate("Dialog", "   z "))
        self.filtering_lbl.setText(_translate("Dialog", "Filtering"))
        self.id_lbl.setText(_translate("Dialog", "ID "))
        self.location_lbl_2.setText(_translate("Dialog", "Location"))
        self.imp_lbl.setText(_translate("Dialog", "Impedance"))
        item = self.electrode_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Region"))
        item = self.electrode_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Description"))
        self.update_btn.setText(_translate("Dialog", "Update/Verify"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Add electrode meta data</span></p></body></html>"))


    def initializePage(self):
        self.openFileNameDialog()

        #File name verification error handling

        if 'ephys_meta_data.mat' not in self.fileName:
            file_verify_dialog = QtWidgets.QDialog()
            ui = Ui_file_verify_dialog()
            ui.setupUi(file_verify_dialog)
            file_verify_dialog.show()                 
            rsp = file_verify_dialog.exec_() #The exec statement prevents window closing immediately
            self.initializePage()
            
        else:
            print('File name verified')

        electrode_meta_data = self.fileName
        meta_data = scipy.io.loadmat(electrode_meta_data)
        electrode_group_dictionary = meta_data['electrode_group']
        electrode_dictionary = meta_data['electrode_meta_data']
        
        #Unpacking the electrode group values 
        device  = electrode_group_dictionary[0,0]['device']
        device = device[0]
        electrode_name = electrode_group_dictionary[0,0]['electrode_name']
        electrode_name = electrode_name[0]
        description = electrode_group_dictionary[0,0]['description']
        description = description[0]
        location = electrode_group_dictionary[0,0]['location']
        location = location[0]

        #Unpacking electrode values
        electrode_id = electrode_dictionary[0,0]['id']
        electrode_id = electrode_id[0]
        filtering = electrode_dictionary[0,0]['filtering']
        filtering = filtering[0]
        location_2 = electrode_dictionary[0,0]['location']
        location_2 = location_2[0]
        imp = electrode_dictionary[0,0]['imp']
        imp = imp[0]   
        x = electrode_dictionary[0,0]['x']
        x = x[0]
        y = electrode_dictionary[0,0]['y']
        y = y[0]
        z = electrode_dictionary[0,0]['z']
        z = z[0]

        #Populate line edit fields from metdata file
        self.device_le.setText(str(device))
        self.electrode_name_le.setText(str(electrode_name))
        self.description_le.setText(str(description))
        self.location_le.setText(str(location))
        self.filtering_le.setText(str(filtering))
        self.location_le_2.setText(str(location_2))
        self.id_le.setText(str(electrode_id))
        self.imp_le.setText(str(imp))
        self.x_le.setText(str(x))
        self.y_le.setText(str(y))
        self.z_le.setText(str(z))

        #Connect the button here
        self.update_btn.clicked.connect(self.on_click) 

    def on_click(self):
        #This button does several things:
        #1 Populates NWB classes
        #2 Creates an electrode table region
        global nwbfile
        global electrode_group        
        
        electrode_group = nwbfile.create_electrode_group(
            str(self.electrode_name_le.text()),
            str(self.description_le.text()),
            str(self.location_le.text()),
            device =  nwbfile.create_device(self.device_le.text())
        )

        electrode = nwbfile.add_electrode(
            float(self.x_le.text()),
            float(self.y_le.text()),
            float(self.z_le.text()),
            float(self.imp_le.text()),
            str(self.location_le_2.text()),
            str(self.filtering_le.text()),
            electrode_group,
            int(self.id_le.text())
        )        
        print('This is a gotcha: I verified that electrode is in the file, but it prints as:' )
        print(electrode)

        #I'm not sure if a table region makes much sense for a single session.  The table region index is hard coded as there is only one electrode in our table region
        global electrode_table_region 
        electrode_table_region = nwbfile.create_electrode_table_region([0], str(self.description_le.text()))
        print(nwbfile)

        self.electrode_table.insertRow(2)
        self.electrode_table.setItem(1 , 0, QtWidgets.QTableWidgetItem(str(1)))
        self.electrode_table.setItem(1 , 1, QtWidgets.QTableWidgetItem(str(self.description_le.text())))

        #Disconnect
        self.update_btn.setText("Updated")
        self.update_btn.clicked.disconnect()


              

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Select Ephys Meta Data", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            print(self.fileName) 


#code for MatlabStep2
class MatlabStep2(QtWidgets.QWizardPage):
    def __init__(self, parent=None):        
        super(MatlabStep2, self).__init__(parent)
        
        self.setObjectName("Dialog")
        self.resize(1076, 1400)
        self.setMinimumSize(QtCore.QSize(0, 1400))
        self.time_series_translator_gb = QtWidgets.QGroupBox(self)
        self.time_series_translator_gb.setGeometry(QtCore.QRect(60, 20, 981, 1411))
        self.time_series_translator_gb.setMinimumSize(QtCore.QSize(0, 1400))
        self.time_series_translator_gb.setObjectName("time_series_translator_gb")
        self.update_btn = QtWidgets.QPushButton(self.time_series_translator_gb)
        self.update_btn.setGeometry(QtCore.QRect(770, 1280, 150, 30))
        self.update_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.update_btn.setObjectName("update_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 40, 881, 1221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.time_series_translator_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.time_series_translator_grid.setContentsMargins(0, 0, 0, 0)
        self.time_series_translator_grid.setObjectName("time_series_translator_grid")
        self.overwrite_line_cb_1 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_1.setObjectName("overwrite_line_cb_1")
        self.overwrite_line_cb_1.addItem("")
        self.overwrite_line_cb_1.addItem("")
        self.overwrite_line_cb_1.addItem("")
        self.overwrite_line_cb_1.addItem("")
        self.overwrite_line_cb_1.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_1, 0, 1, 1, 1)
        self.overwrite_le_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_1.setReadOnly(True)
        self.overwrite_le_1.setObjectName("overwrite_le_1")
        self.time_series_translator_grid.addWidget(self.overwrite_le_1, 0, 0, 1, 1)
        self.overwrite_le_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_2.setReadOnly(True)
        self.overwrite_le_2.setObjectName("overwrite_le_2")
        self.time_series_translator_grid.addWidget(self.overwrite_le_2, 1, 0, 1, 1)
        self.overwrite_le_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_3.setReadOnly(True)
        self.overwrite_le_3.setObjectName("overwrite_le_3")
        self.time_series_translator_grid.addWidget(self.overwrite_le_3, 2, 0, 1, 1)
        self.overwrite_le_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_4.setReadOnly(True)
        self.overwrite_le_4.setObjectName("overwrite_le_4")
        self.time_series_translator_grid.addWidget(self.overwrite_le_4, 3, 0, 1, 1)
        self.overwrite_le_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_5.setReadOnly(True)
        self.overwrite_le_5.setObjectName("overwrite_le_5")
        self.time_series_translator_grid.addWidget(self.overwrite_le_5, 4, 0, 1, 1)
        self.overwrite_le_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_6.setReadOnly(True)
        self.overwrite_le_6.setObjectName("overwrite_le_6")
        self.time_series_translator_grid.addWidget(self.overwrite_le_6, 5, 0, 1, 1)
        self.overwrite_le_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_7.setReadOnly(True)
        self.overwrite_le_7.setObjectName("overwrite_le_7")
        self.time_series_translator_grid.addWidget(self.overwrite_le_7, 6, 0, 1, 1)
        self.overwrite_le_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_8.setReadOnly(True)
        self.overwrite_le_8.setObjectName("overwrite_le_8")
        self.time_series_translator_grid.addWidget(self.overwrite_le_8, 7, 0, 1, 1)
        self.overwrite_le_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_9.setReadOnly(True)
        self.overwrite_le_9.setObjectName("overwrite_le_9")
        self.time_series_translator_grid.addWidget(self.overwrite_le_9, 8, 0, 1, 1)
        self.overwrite_le_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_10.setReadOnly(True)
        self.overwrite_le_10.setObjectName("overwrite_le_10")
        self.time_series_translator_grid.addWidget(self.overwrite_le_10, 9, 0, 1, 1)
        self.overwrite_le_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_11.setReadOnly(True)
        self.overwrite_le_11.setObjectName("overwrite_le_11")
        self.time_series_translator_grid.addWidget(self.overwrite_le_11, 10, 0, 1, 1)
        self.overwrite_le_12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_12.setReadOnly(True)
        self.overwrite_le_12.setObjectName("overwrite_le_12")
        self.time_series_translator_grid.addWidget(self.overwrite_le_12, 11, 0, 1, 1)
        self.overwrite_le_13 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_13.setReadOnly(True)
        self.overwrite_le_13.setObjectName("overwrite_le_13")
        self.time_series_translator_grid.addWidget(self.overwrite_le_13, 12, 0, 1, 1)
        self.overwrite_le_14 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_14.setReadOnly(True)
        self.overwrite_le_14.setObjectName("overwrite_le_14")
        self.time_series_translator_grid.addWidget(self.overwrite_le_14, 13, 0, 1, 1)
        self.overwrite_le_15 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_15.setReadOnly(True)
        self.overwrite_le_15.setObjectName("overwrite_le_15")
        self.time_series_translator_grid.addWidget(self.overwrite_le_15, 14, 0, 1, 1)
        self.overwrite_le_16 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_16.setReadOnly(True)
        self.overwrite_le_16.setObjectName("overwrite_le_16")
        self.time_series_translator_grid.addWidget(self.overwrite_le_16, 15, 0, 1, 1)
        self.overwrite_le_17 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_17.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_17.setReadOnly(True)
        self.overwrite_le_17.setObjectName("overwrite_le_17")
        self.time_series_translator_grid.addWidget(self.overwrite_le_17, 16, 0, 1, 1)
        self.overwrite_le_18 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_18.setReadOnly(True)
        self.overwrite_le_18.setObjectName("overwrite_le_18")
        self.time_series_translator_grid.addWidget(self.overwrite_le_18, 17, 0, 1, 1)
        self.overwrite_le_19 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_19.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_19.setReadOnly(True)
        self.overwrite_le_19.setObjectName("overwrite_le_19")
        self.time_series_translator_grid.addWidget(self.overwrite_le_19, 18, 0, 1, 1)
        self.overwrite_le_20 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_20.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_20.setReadOnly(True)
        self.overwrite_le_20.setObjectName("overwrite_le_20")
        self.time_series_translator_grid.addWidget(self.overwrite_le_20, 19, 0, 1, 1)
        self.overwrite_le_21 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_21.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_21.setReadOnly(True)
        self.overwrite_le_21.setObjectName("overwrite_le_21")
        self.time_series_translator_grid.addWidget(self.overwrite_le_21, 20, 0, 1, 1)
        self.overwrite_le_22 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_22.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_22.setReadOnly(True)
        self.overwrite_le_22.setObjectName("overwrite_le_22")
        self.time_series_translator_grid.addWidget(self.overwrite_le_22, 21, 0, 1, 1)
        self.overwrite_le_23 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_23.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_23.setReadOnly(True)
        self.overwrite_le_23.setObjectName("overwrite_le_23")
        self.time_series_translator_grid.addWidget(self.overwrite_le_23, 22, 0, 1, 1)
        self.overwrite_le_24 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_24.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_24.setReadOnly(True)
        self.overwrite_le_24.setObjectName("overwrite_le_24")
        self.time_series_translator_grid.addWidget(self.overwrite_le_24, 23, 0, 1, 1)
        self.overwrite_le_25 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.overwrite_le_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.overwrite_le_25.setFocusPolicy(QtCore.Qt.NoFocus)
        self.overwrite_le_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overwrite_le_25.setReadOnly(True)
        self.overwrite_le_25.setObjectName("overwrite_le_25")
        self.time_series_translator_grid.addWidget(self.overwrite_le_25, 24, 0, 1, 1)
        self.overwrite_line_cb_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_2.setObjectName("overwrite_line_cb_2")
        self.overwrite_line_cb_2.addItem("")
        self.overwrite_line_cb_2.addItem("")
        self.overwrite_line_cb_2.addItem("")
        self.overwrite_line_cb_2.addItem("")
        self.overwrite_line_cb_2.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_2, 1, 1, 1, 1)
        self.overwrite_line_cb_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_3.setObjectName("overwrite_line_cb_3")
        self.overwrite_line_cb_3.addItem("")
        self.overwrite_line_cb_3.addItem("")
        self.overwrite_line_cb_3.addItem("")
        self.overwrite_line_cb_3.addItem("")
        self.overwrite_line_cb_3.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_3, 2, 1, 1, 1)
        self.overwrite_line_cb_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_4.setObjectName("overwrite_line_cb_4")
        self.overwrite_line_cb_4.addItem("")
        self.overwrite_line_cb_4.addItem("")
        self.overwrite_line_cb_4.addItem("")
        self.overwrite_line_cb_4.addItem("")
        self.overwrite_line_cb_4.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_4, 3, 1, 1, 1)
        self.overwrite_line_cb_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_5.setObjectName("overwrite_line_cb_5")
        self.overwrite_line_cb_5.addItem("")
        self.overwrite_line_cb_5.addItem("")
        self.overwrite_line_cb_5.addItem("")
        self.overwrite_line_cb_5.addItem("")
        self.overwrite_line_cb_5.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_5, 4, 1, 1, 1)
        self.overwrite_line_cb_6 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_6.setObjectName("overwrite_line_cb_6")
        self.overwrite_line_cb_6.addItem("")
        self.overwrite_line_cb_6.addItem("")
        self.overwrite_line_cb_6.addItem("")
        self.overwrite_line_cb_6.addItem("")
        self.overwrite_line_cb_6.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_6, 5, 1, 1, 1)
        self.overwrite_line_cb_7 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_7.setObjectName("overwrite_line_cb_7")
        self.overwrite_line_cb_7.addItem("")
        self.overwrite_line_cb_7.addItem("")
        self.overwrite_line_cb_7.addItem("")
        self.overwrite_line_cb_7.addItem("")
        self.overwrite_line_cb_7.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_7, 6, 1, 1, 1)
        self.overwrite_line_cb_8 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_8.setObjectName("overwrite_line_cb_8")
        self.overwrite_line_cb_8.addItem("")
        self.overwrite_line_cb_8.addItem("")
        self.overwrite_line_cb_8.addItem("")
        self.overwrite_line_cb_8.addItem("")
        self.overwrite_line_cb_8.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_8, 7, 1, 1, 1)
        self.overwrite_line_cb_9 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_9.setObjectName("overwrite_line_cb_9")
        self.overwrite_line_cb_9.addItem("")
        self.overwrite_line_cb_9.addItem("")
        self.overwrite_line_cb_9.addItem("")
        self.overwrite_line_cb_9.addItem("")
        self.overwrite_line_cb_9.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_9, 8, 1, 1, 1)
        self.overwrite_line_cb_10 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_10.setObjectName("overwrite_line_cb_10")
        self.overwrite_line_cb_10.addItem("")
        self.overwrite_line_cb_10.addItem("")
        self.overwrite_line_cb_10.addItem("")
        self.overwrite_line_cb_10.addItem("")
        self.overwrite_line_cb_10.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_10, 9, 1, 1, 1)
        self.overwrite_line_cb_11 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_11.setObjectName("overwrite_line_cb_11")
        self.overwrite_line_cb_11.addItem("")
        self.overwrite_line_cb_11.addItem("")
        self.overwrite_line_cb_11.addItem("")
        self.overwrite_line_cb_11.addItem("")
        self.overwrite_line_cb_11.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_11, 10, 1, 1, 1)
        self.overwrite_line_cb_12 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_12.setObjectName("overwrite_line_cb_12")
        self.overwrite_line_cb_12.addItem("")
        self.overwrite_line_cb_12.addItem("")
        self.overwrite_line_cb_12.addItem("")
        self.overwrite_line_cb_12.addItem("")
        self.overwrite_line_cb_12.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_12, 11, 1, 1, 1)
        self.overwrite_line_cb_13 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_13.setObjectName("overwrite_line_cb_13")
        self.overwrite_line_cb_13.addItem("")
        self.overwrite_line_cb_13.addItem("")
        self.overwrite_line_cb_13.addItem("")
        self.overwrite_line_cb_13.addItem("")
        self.overwrite_line_cb_13.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_13, 12, 1, 1, 1)
        self.overwrite_line_cb_14 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_14.setObjectName("overwrite_line_cb_14")
        self.overwrite_line_cb_14.addItem("")
        self.overwrite_line_cb_14.addItem("")
        self.overwrite_line_cb_14.addItem("")
        self.overwrite_line_cb_14.addItem("")
        self.overwrite_line_cb_14.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_14, 13, 1, 1, 1)
        self.overwrite_line_cb_15 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_15.setObjectName("overwrite_line_cb_15")
        self.overwrite_line_cb_15.addItem("")
        self.overwrite_line_cb_15.addItem("")
        self.overwrite_line_cb_15.addItem("")
        self.overwrite_line_cb_15.addItem("")
        self.overwrite_line_cb_15.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_15, 14, 1, 1, 1)
        self.overwrite_line_cb_16 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_16.setObjectName("overwrite_line_cb_16")
        self.overwrite_line_cb_16.addItem("")
        self.overwrite_line_cb_16.addItem("")
        self.overwrite_line_cb_16.addItem("")
        self.overwrite_line_cb_16.addItem("")
        self.overwrite_line_cb_16.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_16, 15, 1, 1, 1)
        self.overwrite_line_cb_17 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_17.setObjectName("overwrite_line_cb_17")
        self.overwrite_line_cb_17.addItem("")
        self.overwrite_line_cb_17.addItem("")
        self.overwrite_line_cb_17.addItem("")
        self.overwrite_line_cb_17.addItem("")
        self.overwrite_line_cb_17.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_17, 16, 1, 1, 1)
        self.overwrite_line_cb_18 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_18.setObjectName("overwrite_line_cb_18")
        self.overwrite_line_cb_18.addItem("")
        self.overwrite_line_cb_18.addItem("")
        self.overwrite_line_cb_18.addItem("")
        self.overwrite_line_cb_18.addItem("")
        self.overwrite_line_cb_18.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_18, 17, 1, 1, 1)
        self.overwrite_line_cb_19 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_19.setObjectName("overwrite_line_cb_19")
        self.overwrite_line_cb_19.addItem("")
        self.overwrite_line_cb_19.addItem("")
        self.overwrite_line_cb_19.addItem("")
        self.overwrite_line_cb_19.addItem("")
        self.overwrite_line_cb_19.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_19, 18, 1, 1, 1)
        self.overwrite_line_cb_20 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_20.setObjectName("overwrite_line_cb_20")
        self.overwrite_line_cb_20.addItem("")
        self.overwrite_line_cb_20.addItem("")
        self.overwrite_line_cb_20.addItem("")
        self.overwrite_line_cb_20.addItem("")
        self.overwrite_line_cb_20.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_20, 19, 1, 1, 1)
        self.overwrite_line_cb_21 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_21.setObjectName("overwrite_line_cb_21")
        self.overwrite_line_cb_21.addItem("")
        self.overwrite_line_cb_21.addItem("")
        self.overwrite_line_cb_21.addItem("")
        self.overwrite_line_cb_21.addItem("")
        self.overwrite_line_cb_21.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_21, 20, 1, 1, 1)
        self.overwrite_line_cb_22 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_22.setObjectName("overwrite_line_cb_22")
        self.overwrite_line_cb_22.addItem("")
        self.overwrite_line_cb_22.addItem("")
        self.overwrite_line_cb_22.addItem("")
        self.overwrite_line_cb_22.addItem("")
        self.overwrite_line_cb_22.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_22, 21, 1, 1, 1)
        self.overwrite_line_cb_23 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_23.setObjectName("overwrite_line_cb_23")
        self.overwrite_line_cb_23.addItem("")
        self.overwrite_line_cb_23.addItem("")
        self.overwrite_line_cb_23.addItem("")
        self.overwrite_line_cb_23.addItem("")
        self.overwrite_line_cb_23.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_23, 22, 1, 1, 1)
        self.overwrite_line_cb_24 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_24.setObjectName("overwrite_line_cb_24")
        self.overwrite_line_cb_24.addItem("")
        self.overwrite_line_cb_24.addItem("")
        self.overwrite_line_cb_24.addItem("")
        self.overwrite_line_cb_24.addItem("")
        self.overwrite_line_cb_24.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_24, 23, 1, 1, 1)
        self.overwrite_line_cb_25 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_25.setObjectName("overwrite_line_cb_25")
        self.overwrite_line_cb_25.addItem("")
        self.overwrite_line_cb_25.addItem("")
        self.overwrite_line_cb_25.addItem("")
        self.overwrite_line_cb_25.addItem("")
        self.overwrite_line_cb_25.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_25, 24, 1, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.time_series_translator_gb.setTitle(_translate("Dialog", "Select Timeseries Type:"))
        self.update_btn.setText(_translate("Dialog", "Update/Verify"))
        self.overwrite_line_cb_1.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_1.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_1.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_1.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_1.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_2.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_2.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_2.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_2.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_2.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_3.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_3.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_3.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_3.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_3.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_4.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_4.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_4.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_4.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_4.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_5.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_5.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_5.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_5.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_5.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_6.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_6.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_6.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_6.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_6.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_7.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_7.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_7.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_7.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_7.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_8.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_8.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_8.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_8.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_8.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_9.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_9.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_9.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_9.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_9.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_10.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_10.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_10.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_10.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_10.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_11.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_11.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_11.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_11.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_11.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_12.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_12.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_12.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_12.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_12.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_13.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_13.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_13.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_13.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_13.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_14.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_14.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_14.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_14.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_14.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_15.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_15.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_15.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_15.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_15.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_16.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_16.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_16.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_16.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_16.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_17.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_17.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_17.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_17.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_17.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_18.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_18.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_18.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_18.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_18.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_19.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_19.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_19.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_19.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_19.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_20.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_20.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_20.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_20.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_20.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_21.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_21.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_21.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_21.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_21.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_22.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_22.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_22.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_22.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_22.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_23.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_23.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_23.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_23.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_23.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_24.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_24.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_24.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_24.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_24.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_25.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_25.setItemText(1, _translate("Dialog", "Annotation Timeseries"))
        self.overwrite_line_cb_25.setItemText(2, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_25.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_25.setItemText(4, _translate("Dialog", "Stimulus Timeseries"))
        
    #Code starts here
        #self.initializePage()

    def initializePage(self):
        self.openFileNameDialog()
        global matlab_file
        #matlab_file = hdmf.data_utils.DataChunk(matlab_file)
        
        
        counter = 1
        text_box_prefix = 'overwrite_le_'

        for struct in matlab_file:
            current_text_box_being_edited = text_box_prefix + str(counter)
            #print(str(struct) + " text box is " + current_text_box_being_edited)
            eval("self." + current_text_box_being_edited + ".setText(\"" + str(struct) + "\")")
            #print("set the value of the text in " + current_text_box_being_edited + ".text() to " + struct)
            counter = counter + 1
        
        
        #Hook up the button
        self.update_btn.clicked.connect(self.on_click_update)
        global arrays

        arrays = {}
        for struct, field in matlab_file.items():
            #struct = hdmf.data_utils.DataChunkIterator(struct)
            
            # iterate through group (comment, scale, values, etc.)
            # extract fields of structure within each field (hdf5 group)
            group_dict = {}
            for timeseries, values in field.items():
                # fill group dict with contents of array read into memory ([:])
                # TODO: use read_direct() method to avoid memory duplication
                #values = hdmf.data_utils.DataChunk(values)
                group_dict[timeseries] = values[:]
            
            #arrays[k] = np.array(v)
            arrays[struct] = group_dict

        #Putting this here to speed up testing
        if self.overwrite_line_cb_1.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_1.text()))
            
    def on_click_update(self):
        #This button loops through each of the lineedits to get the struct name
        #and then creates an entry in one of 4 type dictionaries with data that was stored in the badly named "array" from initialize page
        #After the dictionaries are populated, another loop extracts values and passes them to nwb classes, then written to file.

        global matlab_file

        global electric_timeseries_dict
        electric_timeseries_dict = {}
        global alignment_timeseries_dict
        alignment_timeseries_dict = {}
        global stimulus_timeseries_dict
        stimulus_timeseries_dict = {}
        global other_timeseries_dict
        other_timeseries_dict = {}
        global annotation_timeseries_dict
        annotation_timeseries_dict = {}
        
    #Brute force dictionary population
        if self.overwrite_line_cb_1.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_1.text() != ''):
            x = arrays.get(str(self.overwrite_le_1.text()))
            electric_timeseries_dict[str(self.overwrite_le_1.text())] = x 
        elif self.overwrite_line_cb_1.currentText() == "Alignment Timeseries" and (self.overwrite_le_1.text() != ''):
            x = arrays.get(str(self.overwrite_le_1.text()))
            alignment_timeseries_dict[str(self.overwrite_le_1.text())] = x
        elif self.overwrite_line_cb_1.currentText() == "Stimulus Timeseries" and (self.overwrite_le_1.text() != ''):
            x = arrays.get(str(self.overwrite_le_1.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_1.text())] = x
        elif self.overwrite_line_cb_1.currentText() == "Other Timeseries" and (self.overwrite_le_1.text() != ''):
            x = arrays.get(str(self.overwrite_le_1.text())) 
            other_timeseries_dict[str(self.overwrite_le_1.text())] = x
        elif self.overwrite_line_cb_1.currentText() == "Annotation Timeseries" and (self.overwrite_le_1.text() != ''):
            x = arrays.get(str(self.overwrite_le_1.text())) 
            other_timeseries_dict[str(self.overwrite_le_1.text())] = x
        
        if self.overwrite_line_cb_2.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_2.text() != ''):
            x = arrays.get(str(self.overwrite_le_2.text()))
            electric_timeseries_dict[str(self.overwrite_le_2.text())] = x 
        elif self.overwrite_line_cb_2.currentText() == "Alignment Timeseries" and (self.overwrite_le_2.text() != ''):
            x = arrays.get(str(self.overwrite_le_2.text()))
            alignment_timeseries_dict[str(self.overwrite_le_2.text())] = x
        elif self.overwrite_line_cb_2.currentText() == "Stimulus Timeseries" and (self.overwrite_le_2.text() != ''):
            x = arrays.get(str(self.overwrite_le_2.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_2.text())] = x
        elif self.overwrite_line_cb_2.currentText() == "Other Timeseries" and (self.overwrite_le_2.text() != ''):
            x = arrays.get(str(self.overwrite_le_2.text())) 
            other_timeseries_dict[str(self.overwrite_le_2.text())] = x
        elif self.overwrite_line_cb_2.currentText() == "Annotation Timeseries" and (self.overwrite_le_2.text() != ''):
            x = arrays.get(str(self.overwrite_le_2.text())) 
            other_timeseries_dict[str(self.overwrite_le_2.text())] = x

        if self.overwrite_line_cb_3.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_3.text() != ''):
            x = arrays.get(str(self.overwrite_le_3.text()))
            electric_timeseries_dict[str(self.overwrite_le_3.text())] = x 
        elif self.overwrite_line_cb_3.currentText() == "Alignment Timeseries" and (self.overwrite_le_3.text() != ''):
            x = arrays.get(str(self.overwrite_le_3.text()))
            alignment_timeseries_dict[str(self.overwrite_le_3.text())] = x
        elif self.overwrite_line_cb_3.currentText() == "Stimulus Timeseries" and (self.overwrite_le_3.text() != ''):
            x = arrays.get(str(self.overwrite_le_3.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_3.text())] = x
        elif self.overwrite_line_cb_3.currentText() == "Other Timeseries" and (self.overwrite_le_3.text() != ''):
            x = arrays.get(str(self.overwrite_le_3.text())) 
            other_timeseries_dict[str(self.overwrite_le_3.text())] = x
        elif self.overwrite_line_cb_3.currentText() == "Annotation Timeseries" and (self.overwrite_le_3.text() != ''):
            x = arrays.get(str(self.overwrite_le_3.text())) 
            other_timeseries_dict[str(self.overwrite_le_3.text())] = x

        if self.overwrite_line_cb_4.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_4.text() != ''):
            x = arrays.get(str(self.overwrite_le_4.text()))
            electric_timeseries_dict[str(self.overwrite_le_4.text())] = x 
        elif self.overwrite_line_cb_4.currentText() == "Alignment Timeseries" and (self.overwrite_le_4.text() != ''):
            x = arrays.get(str(self.overwrite_le_4.text()))
            alignment_timeseries_dict[str(self.overwrite_le_4.text())] = x
        elif self.overwrite_line_cb_4.currentText() == "Stimulus Timeseries" and (self.overwrite_le_4.text() != ''):
            x = arrays.get(str(self.overwrite_le_4.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_4.text())] = x
        elif self.overwrite_line_cb_4.currentText() == "Other Timeseries" and (self.overwrite_le_4.text() != ''):
            x = arrays.get(str(self.overwrite_le_4.text())) 
            other_timeseries_dict[str(self.overwrite_le_4.text())] = x
        elif self.overwrite_line_cb_4.currentText() == "Annotation Timeseries" and (self.overwrite_le_4.text() != ''):
            x = arrays.get(str(self.overwrite_le_4.text())) 
            other_timeseries_dict[str(self.overwrite_le_4.text())] = x
    
        if self.overwrite_line_cb_5.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_5.text() != ''):
            x = arrays.get(str(self.overwrite_le_5.text()))
            electric_timeseries_dict[str(self.overwrite_le_5.text())] = x 
        elif self.overwrite_line_cb_5.currentText() == "Alignment Timeseries" and (self.overwrite_le_5.text() != ''):
            x = arrays.get(str(self.overwrite_le_5.text()))
            alignment_timeseries_dict[str(self.overwrite_le_5.text())] = x
        elif self.overwrite_line_cb_5.currentText() == "Stimulus Timeseries" and (self.overwrite_le_5.text() != ''):
            x = arrays.get(str(self.overwrite_le_5.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_5.text())] = x
        elif self.overwrite_line_cb_5.currentText() == "Other Timeseries" and (self.overwrite_le_5.text() != ''):
            x = arrays.get(str(self.overwrite_le_5.text())) 
            other_timeseries_dict[str(self.overwrite_le_5.text())] = x
        elif self.overwrite_line_cb_5.currentText() == "Annotation Timeseries" and (self.overwrite_le_5.text() != ''):
            x = arrays.get(str(self.overwrite_le_5.text())) 
            other_timeseries_dict[str(self.overwrite_le_5.text())] = x

        if self.overwrite_line_cb_6.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_6.text() != ''):
            x = arrays.get(str(self.overwrite_le_6.text()))
            electric_timeseries_dict[str(self.overwrite_le_6.text())] = x 
        elif self.overwrite_line_cb_6.currentText() == "Alignment Timeseries" and (self.overwrite_le_6.text() != ''):
            x = arrays.get(str(self.overwrite_le_6.text()))
            alignment_timeseries_dict[str(self.overwrite_le_6.text())] = x
        elif self.overwrite_line_cb_6.currentText() == "Stimulus Timeseries" and (self.overwrite_le_6.text() != ''):
            x = arrays.get(str(self.overwrite_le_6.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_6.text())] = x
        elif self.overwrite_line_cb_6.currentText() == "Other Timeseries" and (self.overwrite_le_6.text() != ''):
            x = arrays.get(str(self.overwrite_le_6.text())) 
            other_timeseries_dict[str(self.overwrite_le_6.text())] = x
        elif self.overwrite_line_cb_6.currentText() == "Annotation Timeseries" and (self.overwrite_le_6.text() != ''):
            x = arrays.get(str(self.overwrite_le_6.text())) 
            other_timeseries_dict[str(self.overwrite_le_6.text())] = x

        if self.overwrite_line_cb_7.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_7.text() != ''):
            x = arrays.get(str(self.overwrite_le_7.text()))
            electric_timeseries_dict[str(self.overwrite_le_7.text())] = x 
        elif self.overwrite_line_cb_7.currentText() == "Alignment Timeseries" and (self.overwrite_le_7.text() != ''):
            x = arrays.get(str(self.overwrite_le_7.text()))
            alignment_timeseries_dict[str(self.overwrite_le_7.text())] = x
        elif self.overwrite_line_cb_7.currentText() == "Stimulus Timeseries" and (self.overwrite_le_7.text() != ''):
            x = arrays.get(str(self.overwrite_le_7.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_7.text())] = x
        elif self.overwrite_line_cb_7.currentText() == "Other Timeseries" and (self.overwrite_le_7.text() != ''):
            x = arrays.get(str(self.overwrite_le_7.text())) 
            other_timeseries_dict[str(self.overwrite_le_7.text())] = x
        elif self.overwrite_line_cb_7.currentText() == "Annotation Timeseries" and (self.overwrite_le_7.text() != ''):
            x = arrays.get(str(self.overwrite_le_7.text())) 
            other_timeseries_dict[str(self.overwrite_le_7.text())] = x

        if self.overwrite_line_cb_8.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_8.text() != ''):
            x = arrays.get(str(self.overwrite_le_8.text()))
            electric_timeseries_dict[str(self.overwrite_le_8.text())] = x 
        elif self.overwrite_line_cb_8.currentText() == "Alignment Timeseries" and (self.overwrite_le_8.text() != ''):
            x = arrays.get(str(self.overwrite_le_8.text()))
            alignment_timeseries_dict[str(self.overwrite_le_8.text())] = x
        elif self.overwrite_line_cb_8.currentText() == "Stimulus Timeseries" and (self.overwrite_le_8.text() != ''):
            x = arrays.get(str(self.overwrite_le_8.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_8.text())] = x
        elif self.overwrite_line_cb_8.currentText() == "Other Timeseries" and (self.overwrite_le_8.text() != ''):
            x = arrays.get(str(self.overwrite_le_8.text())) 
            other_timeseries_dict[str(self.overwrite_le_8.text())] = x
        elif self.overwrite_line_cb_8.currentText() == "Annotation Timeseries" and (self.overwrite_le_8.text() != ''):
            x = arrays.get(str(self.overwrite_le_8.text())) 
            other_timeseries_dict[str(self.overwrite_le_8.text())] = x

        if self.overwrite_line_cb_9.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_9.text() != ''):
            x = arrays.get(str(self.overwrite_le_9.text()))
            electric_timeseries_dict[str(self.overwrite_le_9.text())] = x 
        elif self.overwrite_line_cb_9.currentText() == "Alignment Timeseries" and (self.overwrite_le_9.text() != ''):
            x = arrays.get(str(self.overwrite_le_9.text()))
            alignment_timeseries_dict[str(self.overwrite_le_9.text())] = x
        elif self.overwrite_line_cb_9.currentText() == "Stimulus Timeseries" and (self.overwrite_le_9.text() != ''):
            x = arrays.get(str(self.overwrite_le_9.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_9.text())] = x
        elif self.overwrite_line_cb_9.currentText() == "Other Timeseries" and (self.overwrite_le_9.text() != ''):
            x = arrays.get(str(self.overwrite_le_9.text())) 
            other_timeseries_dict[str(self.overwrite_le_9.text())] = x
        elif self.overwrite_line_cb_9.currentText() == "Annotation Timeseries" and (self.overwrite_le_9.text() != ''):
            x = arrays.get(str(self.overwrite_le_9.text())) 
            other_timeseries_dict[str(self.overwrite_le_9.text())] = x

        if self.overwrite_line_cb_10.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_10.text() != ''):
            x = arrays.get(str(self.overwrite_le_10.text()))
            electric_timeseries_dict[str(self.overwrite_le_10.text())] = x 
        elif self.overwrite_line_cb_10.currentText() == "Alignment Timeseries" and (self.overwrite_le_10.text() != ''):
            x = arrays.get(str(self.overwrite_le_10.text()))
            alignment_timeseries_dict[str(self.overwrite_le_10.text())] = x
        elif self.overwrite_line_cb_10.currentText() == "Stimulus Timeseries" and (self.overwrite_le_10.text() != ''):
            x = arrays.get(str(self.overwrite_le_10.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_10.text())] = x
        elif self.overwrite_line_cb_10.currentText() == "Other Timeseries" and (self.overwrite_le_10.text() != ''):
            x = arrays.get(str(self.overwrite_le_10.text())) 
            other_timeseries_dict[str(self.overwrite_le_10.text())] = x
        elif self.overwrite_line_cb_10.currentText() == "Annotation Timeseries" and (self.overwrite_le_10.text() != ''):
            x = arrays.get(str(self.overwrite_le_10.text())) 
            other_timeseries_dict[str(self.overwrite_le_10.text())] = x

        if self.overwrite_line_cb_11.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_11.text() != ''):
            x = arrays.get(str(self.overwrite_le_11.text()))
            electric_timeseries_dict[str(self.overwrite_le_11.text())] = x 
        elif self.overwrite_line_cb_11.currentText() == "Alignment Timeseries" and (self.overwrite_le_11.text() != ''):
            x = arrays.get(str(self.overwrite_le_11.text()))
            alignment_timeseries_dict[str(self.overwrite_le_11.text())] = x
        elif self.overwrite_line_cb_11.currentText() == "Stimulus Timeseries" and (self.overwrite_le_11.text() != ''):
            x = arrays.get(str(self.overwrite_le_11.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_11.text())] = x
        elif self.overwrite_line_cb_11.currentText() == "Other Timeseries" and (self.overwrite_le_11.text() != ''):
            x = arrays.get(str(self.overwrite_le_11.text())) 
            other_timeseries_dict[str(self.overwrite_le_11.text())] = x
        elif self.overwrite_line_cb_11.currentText() == "Annotation Timeseries" and (self.overwrite_le_11.text() != ''):
            x = arrays.get(str(self.overwrite_le_11.text())) 
            other_timeseries_dict[str(self.overwrite_le_11.text())] = x

        if self.overwrite_line_cb_12.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_12.text() != ''):
            x = arrays.get(str(self.overwrite_le_12.text()))
            electric_timeseries_dict[str(self.overwrite_le_12.text())] = x 
        elif self.overwrite_line_cb_12.currentText() == "Alignment Timeseries" and (self.overwrite_le_12.text() != ''):
            x = arrays.get(str(self.overwrite_le_12.text()))
            alignment_timeseries_dict[str(self.overwrite_le_12.text())] = x
        elif self.overwrite_line_cb_12.currentText() == "Stimulus Timeseries" and (self.overwrite_le_12.text() != ''):
            x = arrays.get(str(self.overwrite_le_12.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_12.text())] = x
        elif self.overwrite_line_cb_12.currentText() == "Other Timeseries" and (self.overwrite_le_12.text() != ''):
            x = arrays.get(str(self.overwrite_le_12.text())) 
            other_timeseries_dict[str(self.overwrite_le_12.text())] = x
        elif self.overwrite_line_cb_12.currentText() == "Annotation Timeseries" and (self.overwrite_le_12.text() != ''):
            x = arrays.get(str(self.overwrite_le_12.text())) 
            other_timeseries_dict[str(self.overwrite_le_12.text())] = x

        if self.overwrite_line_cb_13.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_13.text() != ''):
            x = arrays.get(str(self.overwrite_le_13.text()))
            electric_timeseries_dict[str(self.overwrite_le_13.text())] = x 
        elif self.overwrite_line_cb_13.currentText() == "Alignment Timeseries" and (self.overwrite_le_13.text() != ''):
            x = arrays.get(str(self.overwrite_le_13.text()))
            alignment_timeseries_dict[str(self.overwrite_le_13.text())] = x
        elif self.overwrite_line_cb_13.currentText() == "Stimulus Timeseries" and (self.overwrite_le_13.text() != ''):
            x = arrays.get(str(self.overwrite_le_13.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_13.text())] = x
        elif self.overwrite_line_cb_13.currentText() == "Other Timeseries" and (self.overwrite_le_13.text() != ''):
            x = arrays.get(str(self.overwrite_le_13.text())) 
            other_timeseries_dict[str(self.overwrite_le_13.text())] = x
        elif self.overwrite_line_cb_13.currentText() == "Annotation Timeseries" and (self.overwrite_le_13.text() != ''):
            x = arrays.get(str(self.overwrite_le_13.text())) 
            other_timeseries_dict[str(self.overwrite_le_13.text())] = x

        if self.overwrite_line_cb_14.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_14.text() != ''):
            x = arrays.get(str(self.overwrite_le_14.text()))
            electric_timeseries_dict[str(self.overwrite_le_14.text())] = x 
        elif self.overwrite_line_cb_14.currentText() == "Alignment Timeseries" and (self.overwrite_le_14.text() != ''):
            x = arrays.get(str(self.overwrite_le_14.text()))
            alignment_timeseries_dict[str(self.overwrite_le_14.text())] = x
        elif self.overwrite_line_cb_14.currentText() == "Stimulus Timeseries" and (self.overwrite_le_14.text() != ''):
            x = arrays.get(str(self.overwrite_le_14.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_14.text())] = x
        elif self.overwrite_line_cb_14.currentText() == "Other Timeseries" and (self.overwrite_le_14.text() != ''):
            x = arrays.get(str(self.overwrite_le_14.text())) 
            other_timeseries_dict[str(self.overwrite_le_14.text())] = x
        elif self.overwrite_line_cb_14.currentText() == "Annotation Timeseries" and (self.overwrite_le_14.text() != ''):
            x = arrays.get(str(self.overwrite_le_14.text())) 
            other_timeseries_dict[str(self.overwrite_le_14.text())] = x

        if self.overwrite_line_cb_15.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_15.text() != ''):
            x = arrays.get(str(self.overwrite_le_15.text()))
            electric_timeseries_dict[str(self.overwrite_le_15.text())] = x 
        elif self.overwrite_line_cb_15.currentText() == "Alignment Timeseries" and (self.overwrite_le_15.text() != ''):
            x = arrays.get(str(self.overwrite_le_15.text()))
            alignment_timeseries_dict[str(self.overwrite_le_15.text())] = x
        elif self.overwrite_line_cb_15.currentText() == "Stimulus Timeseries" and (self.overwrite_le_15.text() != ''):
            x = arrays.get(str(self.overwrite_le_15.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_15.text())] = x
        elif self.overwrite_line_cb_15.currentText() == "Other Timeseries" and (self.overwrite_le_15.text() != ''):
            x = arrays.get(str(self.overwrite_le_15.text())) 
            other_timeseries_dict[str(self.overwrite_le_15.text())] = x
        elif self.overwrite_line_cb_15.currentText() == "Annotation Timeseries" and (self.overwrite_le_15.text() != ''):
            x = arrays.get(str(self.overwrite_le_15.text())) 
            other_timeseries_dict[str(self.overwrite_le_15.text())] = x

        if self.overwrite_line_cb_16.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_16.text() != ''):
            x = arrays.get(str(self.overwrite_le_16.text()))
            electric_timeseries_dict[str(self.overwrite_le_16.text())] = x 
        elif self.overwrite_line_cb_16.currentText() == "Alignment Timeseries" and (self.overwrite_le_16.text() != ''):
            x = arrays.get(str(self.overwrite_le_16.text()))
            alignment_timeseries_dict[str(self.overwrite_le_16.text())] = x
        elif self.overwrite_line_cb_16.currentText() == "Stimulus Timeseries" and (self.overwrite_le_16.text() != ''):
            x = arrays.get(str(self.overwrite_le_16.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_16.text())] = x
        elif self.overwrite_line_cb_16.currentText() == "Other Timeseries" and (self.overwrite_le_16.text() != ''):
            x = arrays.get(str(self.overwrite_le_16.text())) 
            other_timeseries_dict[str(self.overwrite_le_16.text())] = x
        elif self.overwrite_line_cb_16.currentText() == "Annotation Timeseries" and (self.overwrite_le_16.text() != ''):
            x = arrays.get(str(self.overwrite_le_16.text())) 
            other_timeseries_dict[str(self.overwrite_le_16.text())] = x

        if self.overwrite_line_cb_17.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_17.text() != ''):
            x = arrays.get(str(self.overwrite_le_17.text()))
            electric_timeseries_dict[str(self.overwrite_le_17.text())] = x 
        elif self.overwrite_line_cb_17.currentText() == "Alignment Timeseries" and (self.overwrite_le_17.text() != ''):
            x = arrays.get(str(self.overwrite_le_17.text()))
            alignment_timeseries_dict[str(self.overwrite_le_17.text())] = x
        elif self.overwrite_line_cb_17.currentText() == "Stimulus Timeseries" and (self.overwrite_le_17.text() != ''):
            x = arrays.get(str(self.overwrite_le_17.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_17.text())] = x
        elif self.overwrite_line_cb_17.currentText() == "Other Timeseries" and (self.overwrite_le_17.text() != ''):
            x = arrays.get(str(self.overwrite_le_17.text())) 
            other_timeseries_dict[str(self.overwrite_le_17.text())] = x
        elif self.overwrite_line_cb_17.currentText() == "Annotation Timeseries" and (self.overwrite_le_17.text() != ''):
            x = arrays.get(str(self.overwrite_le_17.text())) 
            other_timeseries_dict[str(self.overwrite_le_17.text())] = x

        if self.overwrite_line_cb_18.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_18.text() != ''):
            x = arrays.get(str(self.overwrite_le_18.text()))
            electric_timeseries_dict[str(self.overwrite_le_18.text())] = x 
        elif self.overwrite_line_cb_18.currentText() == "Alignment Timeseries" and (self.overwrite_le_18.text() != ''):
            x = arrays.get(str(self.overwrite_le_18.text()))
            alignment_timeseries_dict[str(self.overwrite_le_18.text())] = x
        elif self.overwrite_line_cb_18.currentText() == "Stimulus Timeseries" and (self.overwrite_le_18.text() != ''):
            x = arrays.get(str(self.overwrite_le_18.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_18.text())] = x
        elif self.overwrite_line_cb_18.currentText() == "Other Timeseries" and (self.overwrite_le_18.text() != ''):
            x = arrays.get(str(self.overwrite_le_18.text())) 
            other_timeseries_dict[str(self.overwrite_le_18.text())] = x
        elif self.overwrite_line_cb_18.currentText() == "Annotation Timeseries" and (self.overwrite_le_18.text() != ''):
            x = arrays.get(str(self.overwrite_le_18.text())) 
            other_timeseries_dict[str(self.overwrite_le_18.text())] = x

        if self.overwrite_line_cb_19.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_19.text() != ''):
            x = arrays.get(str(self.overwrite_le_19.text()))
            electric_timeseries_dict[str(self.overwrite_le_19.text())] = x 
        elif self.overwrite_line_cb_19.currentText() == "Alignment Timeseries" and (self.overwrite_le_19.text() != ''):
            x = arrays.get(str(self.overwrite_le_19.text()))
            alignment_timeseries_dict[str(self.overwrite_le_19.text())] = x
        elif self.overwrite_line_cb_19.currentText() == "Stimulus Timeseries" and (self.overwrite_le_19.text() != ''):
            x = arrays.get(str(self.overwrite_le_19.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_19.text())] = x
        elif self.overwrite_line_cb_19.currentText() == "Other Timeseries" and (self.overwrite_le_19.text() != ''):
            x = arrays.get(str(self.overwrite_le_19.text())) 
            other_timeseries_dict[str(self.overwrite_le_19.text())] = x
        elif self.overwrite_line_cb_19.currentText() == "Annotation Timeseries" and (self.overwrite_le_19.text() != ''):
            x = arrays.get(str(self.overwrite_le_19.text())) 
            other_timeseries_dict[str(self.overwrite_le_19.text())] = x

        if self.overwrite_line_cb_20.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_20.text() != ''):
            x = arrays.get(str(self.overwrite_le_20.text()))
            electric_timeseries_dict[str(self.overwrite_le_20.text())] = x 
        elif self.overwrite_line_cb_20.currentText() == "Alignment Timeseries" and (self.overwrite_le_20.text() != ''):
            x = arrays.get(str(self.overwrite_le_20.text()))
            alignment_timeseries_dict[str(self.overwrite_le_20.text())] = x
        elif self.overwrite_line_cb_20.currentText() == "Stimulus Timeseries" and (self.overwrite_le_20.text() != ''):
            x = arrays.get(str(self.overwrite_le_20.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_20.text())] = x
        elif self.overwrite_line_cb_20.currentText() == "Other Timeseries" and (self.overwrite_le_20.text() != ''):
            x = arrays.get(str(self.overwrite_le_20.text())) 
            other_timeseries_dict[str(self.overwrite_le_20.text())] = x
        elif self.overwrite_line_cb_20.currentText() == "Annotation Timeseries" and (self.overwrite_le_20.text() != ''):
            x = arrays.get(str(self.overwrite_le_20.text())) 
            other_timeseries_dict[str(self.overwrite_le_20.text())] = x

        if self.overwrite_line_cb_21.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_21.text() != ''):
            x = arrays.get(str(self.overwrite_le_21.text()))
            electric_timeseries_dict[str(self.overwrite_le_21.text())] = x 
        elif self.overwrite_line_cb_21.currentText() == "Alignment Timeseries" and (self.overwrite_le_21.text() != ''):
            x = arrays.get(str(self.overwrite_le_21.text()))
            alignment_timeseries_dict[str(self.overwrite_le_21.text())] = x
        elif self.overwrite_line_cb_21.currentText() == "Stimulus Timeseries" and (self.overwrite_le_21.text() != ''):
            x = arrays.get(str(self.overwrite_le_21.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_21.text())] = x
        elif self.overwrite_line_cb_21.currentText() == "Other Timeseries" and (self.overwrite_le_21.text() != ''):
            x = arrays.get(str(self.overwrite_le_21.text())) 
            other_timeseries_dict[str(self.overwrite_le_21.text())] = x
        elif self.overwrite_line_cb_21.currentText() == "Annotation Timeseries" and (self.overwrite_le_21.text() != ''):
            x = arrays.get(str(self.overwrite_le_21.text())) 
            other_timeseries_dict[str(self.overwrite_le_21.text())] = x

        if self.overwrite_line_cb_22.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_22.text() != ''):
            x = arrays.get(str(self.overwrite_le_22.text()))
            electric_timeseries_dict[str(self.overwrite_le_22.text())] = x 
        elif self.overwrite_line_cb_22.currentText() == "Alignment Timeseries" and (self.overwrite_le_22.text() != ''):
            x = arrays.get(str(self.overwrite_le_22.text()))
            alignment_timeseries_dict[str(self.overwrite_le_22.text())] = x
        elif self.overwrite_line_cb_22.currentText() == "Stimulus Timeseries" and (self.overwrite_le_22.text() != ''):
            x = arrays.get(str(self.overwrite_le_22.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_22.text())] = x
        elif self.overwrite_line_cb_22.currentText() == "Other Timeseries" and (self.overwrite_le_22.text() != ''):
            x = arrays.get(str(self.overwrite_le_22.text())) 
            other_timeseries_dict[str(self.overwrite_le_22.text())] = x
        elif self.overwrite_line_cb_22.currentText() == "Annotation Timeseries" and (self.overwrite_le_22.text() != ''):
            x = arrays.get(str(self.overwrite_le_22.text())) 
            other_timeseries_dict[str(self.overwrite_le_22.text())] = x

        if self.overwrite_line_cb_23.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_23.text() != ''):
            x = arrays.get(str(self.overwrite_le_23.text()))
            electric_timeseries_dict[str(self.overwrite_le_23.text())] = x 
        elif self.overwrite_line_cb_23.currentText() == "Alignment Timeseries" and (self.overwrite_le_23.text() != ''):
            x = arrays.get(str(self.overwrite_le_23.text()))
            alignment_timeseries_dict[str(self.overwrite_le_23.text())] = x
        elif self.overwrite_line_cb_23.currentText() == "Stimulus Timeseries" and (self.overwrite_le_23.text() != ''):
            x = arrays.get(str(self.overwrite_le_23.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_23.text())] = x
        elif self.overwrite_line_cb_23.currentText() == "Other Timeseries" and (self.overwrite_le_23.text() != ''):
            x = arrays.get(str(self.overwrite_le_23.text())) 
            other_timeseries_dict[str(self.overwrite_le_23.text())] = x
        elif self.overwrite_line_cb_23.currentText() == "Annotation Timeseries" and (self.overwrite_le_23.text() != ''):
            x = arrays.get(str(self.overwrite_le_23.text())) 
            other_timeseries_dict[str(self.overwrite_le_23.text())] = x

        if self.overwrite_line_cb_24.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_24.text() != ''):
            x = arrays.get(str(self.overwrite_le_24.text()))
            electric_timeseries_dict[str(self.overwrite_le_24.text())] = x 
        elif self.overwrite_line_cb_24.currentText() == "Alignment Timeseries" and (self.overwrite_le_24.text() != ''):
            x = arrays.get(str(self.overwrite_le_24.text()))
            alignment_timeseries_dict[str(self.overwrite_le_24.text())] = x
        elif self.overwrite_line_cb_24.currentText() == "Stimulus Timeseries" and (self.overwrite_le_24.text() != ''):
            x = arrays.get(str(self.overwrite_le_24.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_24.text())] = x
        elif self.overwrite_line_cb_24.currentText() == "Other Timeseries" and (self.overwrite_le_24.text() != ''):
            x = arrays.get(str(self.overwrite_le_24.text())) 
            other_timeseries_dict[str(self.overwrite_le_24.text())] = x
        elif self.overwrite_line_cb_24.currentText() == "Annotation Timeseries" and (self.overwrite_le_24.text() != ''):
            x = arrays.get(str(self.overwrite_le_24.text())) 
            other_timeseries_dict[str(self.overwrite_le_24.text())] = x

        if self.overwrite_line_cb_25.currentText() == "Electric Field Potential Timeseries" and (self.overwrite_le_25.text() != ''):
            x = arrays.get(str(self.overwrite_le_25.text()))
            electric_timeseries_dict[str(self.overwrite_le_25.text())] = x 
        elif self.overwrite_line_cb_25.currentText() == "Alignment Timeseries" and (self.overwrite_le_25.text() != ''):
            x = arrays.get(str(self.overwrite_le_25.text()))
            alignment_timeseries_dict[str(self.overwrite_le_25.text())] = x
        elif self.overwrite_line_cb_25.currentText() == "Stimulus Timeseries" and (self.overwrite_le_25.text() != ''):
            x = arrays.get(str(self.overwrite_le_25.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_25.text())] = x
        elif self.overwrite_line_cb_25.currentText() == "Other Timeseries" and (self.overwrite_le_25.text() != ''):
            x = arrays.get(str(self.overwrite_le_25.text())) 
            other_timeseries_dict[str(self.overwrite_le_25.text())] = x
        elif self.overwrite_line_cb_25.currentText() == "Annotation Timeseries" and (self.overwrite_le_25.text() != ''):
            x = arrays.get(str(self.overwrite_le_25.text())) 
            other_timeseries_dict[str(self.overwrite_le_25.text())] = x
               
        
    #Add dict values to nwbfile
        global electrode_table_region
        global electrode_group
        global electrode


        print('Loop through electric dictionary and add electrical series to nwb')
        for struct in electric_timeseries_dict.keys():
                      
            #We name the timeseries data after the struct
            name = struct
            print(name)
            print('the above is a struct')
            print('')
            for value in electric_timeseries_dict[struct].keys(): 
                print(value)
                print('the above is a value')

                if value == 'comment':
                    comments = electric_timeseries_dict[struct][value][:].tolist()
                    #This checks for '', which is how Spike2 passes empty strigs
                    if comments == [0, 0]:
                        comments = 'no comment'
                    else:
                        comments = electric_timeseries_dict[struct][value][:].tolist()
                        comments  = [str(chr(a_character[0])) for a_character in comments]
                        comments = "".join(comments)

                if value == 'interval':
                    #In NWB interval = rate.
                    rate = electric_timeseries_dict[struct][value][0]
                    print(rate)
                    print('the above is a the interval/rate value')
                    print('')

                if value == 'scale':
                    #In NWB scale = conversion.
                    conversion = electric_timeseries_dict[struct][value][0]
                    print(conversion)
                    print('the above is the scale/ conversion')
                    print('')

                if value == 'start':
                    #NWB start = starting_time
                    starting_time = electric_timeseries_dict[struct][value][0]
                    print(starting_time)
                    print('the above is starting_time/start')
                    print('')

                if value =='title':
                    #This seems like it fits description better than name. Could have lab vote on preference.
                    description = electric_timeseries_dict[struct][value][:].tolist()
                    description = electric_timeseries_dict[struct][value][:].tolist()
                    description  = [str(chr(a_character[0])) for a_character in description]
                    description = "".join(description)
                    print(description)
                    print('the above is the title/description')
                    print('')

                if value == 'values':
                    #NWB values = data
                    
                    data = electric_timeseries_dict[struct][value][0]
                    #data = hdmf.data_utils.DataChunkIterator(data)
                    print(data)
                    print('the above is the timeseries data/values')
                    print('')

            
            electrical_timeseries  = pynwb.ecephys.ElectricalSeries(
                name,
                data,
                electrode_table_region,
                #timestamps=ephys_timestamps,                            
                starting_time = float(starting_time),
                rate = float(rate),
                #resolution=0.001,
                comments = comments,
                description = description
                )

            print(electrical_timeseries)
            
            nwbfile.add_acquisition(electrical_timeseries)
            

        for struct in stimulus_timeseries_dict.keys():                      
        #We name the timeseries data after the struct
            name = struct
            print(name)

            for value in stimulus_timeseries_dict[struct].keys(): 
                print(value)
                
                if value == 'comment':
                    comments = stimulus_timeseries_dict[struct][value][:].tolist()
                    #This checks for '', which is how Spike2 passes empty strigs
                    if comments == [0, 0]:
                        comments = 'no comment'
                    else:
                        comments = stimulus_timeseries_dict[struct][value][:].tolist()
                        comments  = [str(chr(a_character[0])) for a_character in comments]
                        comments = "".join(comments)

                if value == 'interval':
                    #In NWB interval = rate.
                    rate = stimulus_timeseries_dict[struct][value][0]
                    print(rate)

                if value == 'scale':
                    #In NWB scale = conversion.
                    conversion = stimulus_timeseries_dict[struct][value][0]
                    print(conversion)

                if value == 'start':
                    #NWB start = starting_time
                    starting_time = stimulus_timeseries_dict[struct][value][0]
                    print(starting_time)

                if value =='title':
                    #This seems like it fits description better than name. Could have lab vote on preference.
                    description = stimulus_timeseries_dict[struct][value][:].tolist()
                    description = stimulus_timeseries_dict[struct][value][:].tolist()
                    description  = [str(chr(a_character[0])) for a_character in description]
                    description = "".join(description)
                    print(description)

                if value == 'values':
                    #NWB values = data
                    
                    data = stimulus_timeseries_dict[struct][value][0]
                    #data = hdmf.data_utils.DataChunkIterator(data)
                    print(data)

                if value == 'units':
                    #NWB vexingly alternates in between 'unit' and 'units'. Here it wants 'unit'
                    unit = stimulus_timeseries_dict[struct][value][:].tolist()
                    unit = stimulus_timeseries_dict[struct][value][:].tolist()
                    unit = [str(chr(a_character[0])) for a_character in unit]
                    unit = "".join(unit)
                    print(unit)

            stimulus_timeseries = pynwb.base.TimeSeries(
                name,
                data = data,
                unit = unit,
                #timestamps=ephys_timestamps,                            
                starting_time = float(starting_time),
                rate = float(rate),
                #resolution=0.001,
                comments = comments,
                description = description
                )     

            print(stimulus_timeseries)

            nwbfile.add_stimulus(stimulus_timeseries)

        for struct in other_timeseries_dict.keys():                      
        #We name the timeseries data after the struct
            name = struct
            print(name)

            for value in other_timeseries_dict[struct].keys(): 
                print(value)
                
                if value == 'comment':
                    comments = other_timeseries_dict[struct][value][:].tolist()
                    #This checks for '', which is how Spike2 passes empty strigs
                    if comments == [0, 0]:
                        comments = 'no comment'
                    else:
                        comments = other_timeseries_dict[struct][value][:].tolist()
                        comments  = [str(chr(a_character[0])) for a_character in comments]
                        comments = "".join(comments)

                if value == 'interval':
                    #In NWB interval = rate.
                    rate = other_timeseries_dict[struct][value][0]
                    print(rate)

                if value == 'scale':
                    #In NWB scale = conversion.
                    conversion = other_timeseries_dict[struct][value][0]
                    print(conversion)

                if value == 'start':
                    #NWB start = starting_time
                    starting_time = other_timeseries_dict[struct][value][0]
                    print(starting_time)

                if value =='title':
                    #This seems like it fits description better than name. Could have lab vote on preference.
                    description = other_timeseries_dict[struct][value][:].tolist()
                    description = other_timeseries_dict[struct][value][:].tolist()
                    description  = [str(chr(a_character[0])) for a_character in description]
                    description = "".join(description)
                    print(description)

                if value == 'values':
                    #NWB values = data
                    
                    data = other_timeseries_dict[struct][value][0]
                    #data = hdmf.data_utils.DataChunkIterator(data)
                    print(data)

                if value == 'units':
                    #NWB vexingly alternates in between 'unit' and 'units'. Here it wants 'unit'
                    unit = other_timeseries_dict[struct][value][:].tolist()
                    unit = other_timeseries_dict[struct][value][:].tolist()
                    unit = [str(chr(a_character[0])) for a_character in unit]
                    unit = "".join(unit)
                    print(unit)

            other_timeseries = pynwb.base.TimeSeries(
                name,
                data = data,
                unit = unit,
                #timestamps=ephys_timestamps,                            
                starting_time = float(starting_time),
                rate = float(rate),
                #resolution=0.001,
                comments = comments,
                description = description
                )     

            print(other_timeseries)

            nwbfile.add_acquisition(other_timeseries)

        for struct in alignment_timeseries_dict.keys():
                      
            #We name the timeseries data after the struct
            name = struct
            print(name)
            print('Alignment struct')
            print('')
            for value in alignment_timeseries_dict[struct].keys(): 
                print(value)
                print('the above is a value')

                if value == 'comment':
                    comments = alignment_timeseries_dict[struct][value][:].tolist()
                    #This checks for '', which is how Spike2 passes empty strigs
                    if comments == [0, 0]:
                        comments = 'no comment'
                    else:
                        comments = alignment_timeseries_dict[struct][value][:].tolist()
                        comments  = [str(chr(a_character[0])) for a_character in comments]
                        comments = "".join(comments)
                                           
                    print(comments)
                    print("empty comment handling worked")
                    print('')

                if value == 'resolution':
                    #In NWB interval = rate.
                    resolution = alignment_timeseries_dict[struct][value][0,0]
                    print(resolution)
                    print('the above is a the resolution value')
                    print('')


                if value == 'times':
                    #NWB values = data
                    
                    timestamps = alignment_timeseries_dict[struct][value][0]
                    #data = hdmf.data_utils.DataChunkIterator(data)
                    print(timestamps)
                    print('the above is the timestamps for this alignment')
                    print('')

                if value =='title':
                    #This seems like it fits description better than name. Could have lab vote on preference.
                    description = alignment_timeseries_dict[struct][value][:].tolist()
                    description = alignment_timeseries_dict[struct][value][:].tolist()
                    description  = [str(chr(a_character[0])) for a_character in description]
                    description = "".join(description)
                    print(description)

            aligment_timeseries = pynwb.base.TimeSeries(
                name,
                #data = data,
                #unit = unit,
                timestamps = timestamps,                            
                #starting_time = float(starting_time),
                #rate = float(rate),
                resolution = resolution,
                comments = comments,
                description = description
                )

            nwbfile.add_acquisition(aligment_timeseries)

        for struct in annotation_timeseries_dict.keys():
                      
            #We name the timeseries data after the struct
            name = struct
            print(name)
            print('annotation struct')
            print('')
            for value in annotation_timeseries_dict[struct].keys(): 
                print(value)
                print('the above is a value')
                
                if value == 'comment':
                    comments = annotation_timeseries_dict[struct][value][:].tolist()
                    #This checks for '', which is how Spike2 passes empty strigs
                    if comments == [0, 0]:
                        comments = 'no comment'
                    else:
                        comments = annotation_timeseries_dict[struct][value][:].tolist()
                        comments  = [str(chr(a_character[0])) for a_character in comments]
                        comments = "".join(comments)
                                           
                    print(comments)
                    print("empty comment handling worked")
                    print('')

                if value == 'resolution':
                    #In NWB interval = rate.
                    resolution = annotation_timeseries_dict[struct][value][0,0]
                    print(resolution)
                    print('the above is a the resolution value')
                    print('')


                if value == 'times':
                    #NWB values = data
                    
                    timestamps = annotation_timeseries_dict[struct][value][0]
                    #data = hdmf.data_utils.DataChunkIterator(data)
                    print(timestamps)
                    print('the above is the timestamps for this annotation')
                    print('')

                if value =='title':
                    #This seems like it fits description better than name. Could have lab vote on preference.
                    description = annotation_timeseries_dict[struct][value][:].tolist()
                    description = annotation_timeseries_dict[struct][value][:].tolist()
                    description  = [str(chr(a_character[0])) for a_character in description]
                    description = "".join(description)
                    print(description)

                if value == 'codes':
                    #NWB values = data
                    
                    data = other_timeseries_dict[struct][value][0]
                    #data = hdmf.data_utils.DataChunkIterator(data)
                    print(data)

            #Revisit this for best practice changes.  Spike2 data doesn't fit well. CH31 from INT017_180629 is the template used
            annotaion_timeseries = pynwb.misc.AnnotationSeries(
                name,
                data = data, #I put 'codes' here
                timestamps = timestamps, #I put 'times' here.                                          
                #rate = float(rate),
                #resolution = resolution, #There is no field for resolution
                comments = comments,
                description = description
                )

            nwbfile.add_add_annotation(aligment_timeseries)

    #Write to file
        global identifier
        with NWBHDF5IO(identifier + '.nwb', 'w') as io:
            io.write(nwbfile)
        print(nwbfile)

        self.update_btn.setText("Updated")
        self.update_btn.clicked.disconnect()
                           

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Select .mat with timeseries data. Warning: SLOW", "","All Files (*);;Python Files (*.py)", options=options)
        global matlab_file
        matlab_file = self.fileName
        matlab_file = h5py.File(matlab_file)
        if self.fileName:
            print(self.fileName)




if __name__ == '__main__':
    import sys
    #PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app = QtWidgets.QApplication(sys.argv)
    headerfilename = ''
    session_start_time = ''
    timestamps_reference_time = ''
    identifier = ''
    session_description = ''
    two_photon_metadata = ''
    two_photon_series = ''
    optical_channel = ''
    imaging_plane = ''
    image_sgementation = ''
    processing_module = ''
    tiff_stack = ''
    roi_array = ''
    dff_array = ''
    region = ''
    nwbfile = ''
    fluorescence = ''
    dff = ''
    #Matlab Step 1
    matlab_file = ''
    arrays = ''
    electric_timeseries_dict = ''
    stimulus_timeseries_dict = ''
    other_timeseries_dict = ''
    alignment_timeseries_dict = ''
    annotation_timeseries_dict = ''
    #Matlab Step 2
    electrode_group = ''
    electrode_table_region = ''
    #NWB
    subject = pynwb.file.Subject()
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())