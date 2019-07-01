#Code for MatlabStep3
class MatlabStep3(QtWidgets.QWizardPage):
    def __init__(self, parent=None):        
        super(MatlabStep3, self).__init__(parent)

        self.setObjectName("Dialog")
        self.resize(2368, 976)
        self.setMinimumSize(QtCore.QSize(1800, 100))
        self.electric_timeseries_gb = QtWidgets.QGroupBox(self)
        self.electric_timeseries_gb.setGeometry(QtCore.QRect(10, 10, 581, 951))
        self.electric_timeseries_gb.setMinimumSize(QtCore.QSize(450, 0))
        self.electric_timeseries_gb.setObjectName("electric_timeseries_gb")
        self.gridLayoutWidget = QtWidgets.QWidget(self.electric_timeseries_gb)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 29, 561, 911))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.electric_timeseries_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.electric_timeseries_grid.setContentsMargins(0, 0, 0, 0)
        self.electric_timeseries_grid.setObjectName("electric_timeseries_grid")
        self.electric_timeseries_rbtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.electric_timeseries_rbtn.setObjectName("electric_timeseries_rbtn")
        self.electric_timeseries_grid.addWidget(self.electric_timeseries_rbtn, 1, 0, 1, 1)
        self.electric_timeseries_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.electric_timeseries_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.electric_timeseries_pte.setObjectName("electric_timeseries_pte")
        self.electric_timeseries_grid.addWidget(self.electric_timeseries_pte, 0, 0, 1, 1)
        self.electric_timeseries_lw = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.electric_timeseries_lw.setObjectName("electric_timeseries_lw")
        self.electric_timeseries_grid.addWidget(self.electric_timeseries_lw, 2, 0, 1, 1)
        self.other_timeseries_gb = QtWidgets.QGroupBox(self)
        self.other_timeseries_gb.setGeometry(QtCore.QRect(600, 10, 581, 951))
        self.other_timeseries_gb.setMinimumSize(QtCore.QSize(450, 0))
        self.other_timeseries_gb.setObjectName("other_timeseries_gb")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.other_timeseries_gb)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 29, 561, 911))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.other_timeseries_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.other_timeseries_grid.setContentsMargins(0, 0, 0, 0)
        self.other_timeseries_grid.setObjectName("other_timeseries_grid")
        self.other_timeseries_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.other_timeseries_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.other_timeseries_pte.setObjectName("other_timeseries_pte")
        self.other_timeseries_grid.addWidget(self.other_timeseries_pte, 0, 0, 1, 1)
        self.other_timeseries_lw = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.other_timeseries_lw.setObjectName("other_timeseries_lw")
        self.other_timeseries_grid.addWidget(self.other_timeseries_lw, 1, 0, 1, 1)
        self.alignment_timeseries_gb = QtWidgets.QGroupBox(self)
        self.alignment_timeseries_gb.setGeometry(QtCore.QRect(1190, 10, 581, 951))
        self.alignment_timeseries_gb.setMinimumSize(QtCore.QSize(450, 0))
        self.alignment_timeseries_gb.setObjectName("alignment_timeseries_gb")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.alignment_timeseries_gb)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 29, 561, 911))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.alignment_timeseries_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.alignment_timeseries_grid.setContentsMargins(0, 0, 0, 0)
        self.alignment_timeseries_grid.setObjectName("alignment_timeseries_grid")
        self.alignment_timeseries_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        self.alignment_timeseries_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.alignment_timeseries_pte.setObjectName("alignment_timeseries_pte")
        self.alignment_timeseries_grid.addWidget(self.alignment_timeseries_pte, 0, 0, 1, 1)
        self.alignment_timeseries_lw = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.alignment_timeseries_lw.setObjectName("alignment_timeseries_lw")
        self.alignment_timeseries_grid.addWidget(self.alignment_timeseries_lw, 1, 0, 1, 1)
        self.stimulus_timeseries_gb = QtWidgets.QGroupBox(self)
        self.stimulus_timeseries_gb.setGeometry(QtCore.QRect(1780, 10, 581, 951))
        self.stimulus_timeseries_gb.setMinimumSize(QtCore.QSize(450, 0))
        self.stimulus_timeseries_gb.setObjectName("stimulus_timeseries_gb")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.stimulus_timeseries_gb)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 29, 561, 911))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.stimulus_timeseries_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.stimulus_timeseries_grid.setContentsMargins(0, 0, 0, 0)
        self.stimulus_timeseries_grid.setObjectName("stimulus_timeseries_grid")
        self.stimulus_timesries_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.stimulus_timesries_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.stimulus_timesries_pte.setObjectName("stimulus_timesries_pte")
        self.stimulus_timeseries_grid.addWidget(self.stimulus_timesries_pte, 0, 0, 1, 1)
        self.stimulus_timeseries_lw = QtWidgets.QListWidget(self.gridLayoutWidget_5)
        self.stimulus_timeseries_lw.setObjectName("stimulus_timeseries_lw")
        self.stimulus_timeseries_grid.addWidget(self.stimulus_timeseries_lw, 1, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.electric_timeseries_gb.setTitle(_translate("Dialog", "Electric Timeseries Data"))
        self.electric_timeseries_rbtn.setText(_translate("Dialog", "Check here if this data has been filtered"))
        self.electric_timeseries_pte.setPlainText(_translate("Dialog", "<Describe the timeseries data>"))
        self.other_timeseries_gb.setTitle(_translate("Dialog", "Other Timeseries Data"))
        self.other_timeseries_pte.setPlainText(_translate("Dialog", "<Describe the timeseries data>"))
        self.alignment_timeseries_gb.setTitle(_translate("Dialog", "Alignment Timeseries Data"))
        self.alignment_timeseries_pte.setPlainText(_translate("Dialog", "<Describe the timeseries data>"))
        self.stimulus_timeseries_gb.setTitle(_translate("Dialog", "Stimulus Timeseries Data"))
        self.stimulus_timesries_pte.setPlainText(_translate("Dialog", "<Describe the timeseries data>"))


    def initializePage(self):

        #Pass the electric timeseries to the list view
        electric_timeseries_structs = []
        for struct in electric_timeseries_dict:
            electric_timeseries_structs.append(struct)
            self.electric_timeseries_lw.addItems(electric_timeseries_structs)
        print(electric_timeseries_structs)

        #Pass the alignment timeseries to the list view
        alignment_timeseries_structs = []
        for struct in alignment_timeseries_dict:
            alignment_timeseries_structs.append(struct)
            self.alignment_timeseries_lw.addItems(alignment_timeseries_structs)
        print(alignment_timeseries_structs)

        #Pass the stimulus timeseries to the list view
        stimulus_timeseries_structs = []
        for struct in stimulus_timeseries_dict:
            stimulus_timeseries_structs.append(struct)
            self.stimulus_timeseries_lw.addItems(stimulus_timeseries_structs)
        print(stimulus_timeseries_structs)

        #Pass the other timeseries to the list view
        other_timeseries_structs = []
        for struct in other_timeseries_dict:
            other_timeseries_structs.append(struct)
            self.other_timeseries_lw.addItems(other_timeseries_structs)
        print(other_timeseries_structs)
