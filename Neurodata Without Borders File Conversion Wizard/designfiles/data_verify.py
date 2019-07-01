# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_verify.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

