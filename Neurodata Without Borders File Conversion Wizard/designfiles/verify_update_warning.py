# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verify_update_warning.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(272, 160)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 120, 241, 30))
        self.buttonBox.setMinimumSize(QtCore.QSize(200, 30))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 241, 102))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.verify_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.verify_grid.setContentsMargins(0, 0, 0, 0)
        self.verify_grid.setObjectName("verify_grid")
        self.verify_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.verify_pte.setMinimumSize(QtCore.QSize(200, 100))
        self.verify_pte.setReadOnly(True)
        self.verify_pte.setObjectName("verify_pte")
        self.verify_grid.addWidget(self.verify_pte, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.verify_pte.setPlainText(_translate("Dialog", "You must verify that your data is correct.  Click OK to proceed."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

