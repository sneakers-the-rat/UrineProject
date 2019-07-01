# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomeScreen2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 304)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 9, 401, 171))
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
        self.SaveBtn = QtWidgets.QPushButton(Dialog)
        self.SaveBtn.setGeometry(QtCore.QRect(50, 210, 75, 23))
        self.SaveBtn.setObjectName("SaveBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.HeaderDataAdded.setText(_translate("Dialog", "Header data added!"))
        self.SelectNextDataType.setText(_translate("Dialog", "Select next data type:"))
        self.DataTypeSelector.setItemText(0, _translate("Dialog", "Widefield and 2P data"))
        self.DataTypeSelector.setItemText(1, _translate("Dialog", "Matlab file with multiple timeseries"))
        self.SaveBtn.setText(_translate("Dialog", "Save File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

