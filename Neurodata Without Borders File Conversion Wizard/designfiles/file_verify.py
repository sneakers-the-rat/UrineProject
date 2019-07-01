# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_verify.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_file_verify_dialog(object):
    def setupUi(self, file_verify_dialog):
        file_verify_dialog.setObjectName("file_verify_dialog")
        file_verify_dialog.resize(556, 225)
        self.file_verify_bb = QtWidgets.QDialogButtonBox(file_verify_dialog)
        self.file_verify_bb.setGeometry(QtCore.QRect(30, 170, 261, 32))
        self.file_verify_bb.setOrientation(QtCore.Qt.Horizontal)
        self.file_verify_bb.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.file_verify_bb.setObjectName("file_verify_bb")
        self.gridLayoutWidget = QtWidgets.QWidget(file_verify_dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 502, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.file_verify_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.file_verify_grid.setContentsMargins(0, 0, 0, 0)
        self.file_verify_grid.setObjectName("file_verify_grid")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(200, 80))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.file_verify_grid.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.retranslateUi(file_verify_dialog)
        self.file_verify_bb.accepted.connect(file_verify_dialog.accept)
        self.file_verify_bb.rejected.connect(file_verify_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(file_verify_dialog)

    def retranslateUi(self, file_verify_dialog):
        _translate = QtCore.QCoreApplication.translate
        file_verify_dialog.setWindowTitle(_translate("file_verify_dialog", "Dialog"))
        self.plainTextEdit.setPlainText(_translate("file_verify_dialog", "The NWB Converter expected a different type of file."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    file_verify_dialog = QtWidgets.QDialog()
    ui = Ui_file_verify_dialog()
    ui.setupUi(file_verify_dialog)
    file_verify_dialog.show()
    sys.exit(app.exec_())

