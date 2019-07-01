from PyQt5 import QtCore, QtGui, QtWidgets
import h5py
import numpy as np
import pdb
from EphysStep2 import Ui_Dialog




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1076, 1400)
        Dialog.setMinimumSize(QtCore.QSize(0, 1400))
        self.time_series_translator_gb = QtWidgets.QGroupBox(Dialog)
        self.time_series_translator_gb.setGeometry(QtCore.QRect(60, 20, 981, 1411))
        self.time_series_translator_gb.setMinimumSize(QtCore.QSize(0, 1400))
        self.time_series_translator_gb.setObjectName("time_series_translator_gb")
        self.gridLayoutWidget = QtWidgets.QWidget(self.time_series_translator_gb)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 881, 1221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.time_series_translator_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.time_series_translator_grid.setContentsMargins(0, 0, 0, 0)
        self.time_series_translator_grid.setObjectName("time_series_translator_grid")
        self.overwrite_line_cb_14 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_14.setObjectName("overwrite_line_cb_14")
        self.overwrite_line_cb_14.addItem("")
        self.overwrite_line_cb_14.addItem("")
        self.overwrite_line_cb_14.addItem("")
        self.overwrite_line_cb_14.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_14, 13, 1, 1, 1)
        self.overwrite_line_cb_18 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_18.setObjectName("overwrite_line_cb_18")
        self.overwrite_line_cb_18.addItem("")
        self.overwrite_line_cb_18.addItem("")
        self.overwrite_line_cb_18.addItem("")
        self.overwrite_line_cb_18.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_18, 17, 1, 1, 1)
        self.overwrite_line_cb_17 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_17.setObjectName("overwrite_line_cb_17")
        self.overwrite_line_cb_17.addItem("")
        self.overwrite_line_cb_17.addItem("")
        self.overwrite_line_cb_17.addItem("")
        self.overwrite_line_cb_17.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_17, 16, 1, 1, 1)
        self.overwrite_line_cb_15 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_15.setObjectName("overwrite_line_cb_15")
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
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_16, 15, 1, 1, 1)
        self.overwrite_line_cb_21 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_21.setObjectName("overwrite_line_cb_21")
        self.overwrite_line_cb_21.addItem("")
        self.overwrite_line_cb_21.addItem("")
        self.overwrite_line_cb_21.addItem("")
        self.overwrite_line_cb_21.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_21, 20, 1, 1, 1)
        self.overwrite_line_cb_19 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_19.setObjectName("overwrite_line_cb_19")
        self.overwrite_line_cb_19.addItem("")
        self.overwrite_line_cb_19.addItem("")
        self.overwrite_line_cb_19.addItem("")
        self.overwrite_line_cb_19.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_19, 18, 1, 1, 1)
        self.overwrite_line_cb_22 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_22.setObjectName("overwrite_line_cb_22")
        self.overwrite_line_cb_22.addItem("")
        self.overwrite_line_cb_22.addItem("")
        self.overwrite_line_cb_22.addItem("")
        self.overwrite_line_cb_22.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_22, 21, 1, 1, 1)
        self.overwrite_line_cb_20 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_20.setObjectName("overwrite_line_cb_20")
        self.overwrite_line_cb_20.addItem("")
        self.overwrite_line_cb_20.addItem("")
        self.overwrite_line_cb_20.addItem("")
        self.overwrite_line_cb_20.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_20, 19, 1, 1, 1)
        self.overwrite_line_cb_10 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_10.setObjectName("overwrite_line_cb_10")
        self.overwrite_line_cb_10.addItem("")
        self.overwrite_line_cb_10.addItem("")
        self.overwrite_line_cb_10.addItem("")
        self.overwrite_line_cb_10.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_10, 9, 1, 1, 1)
        self.overwrite_line_cb_8 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_8.setObjectName("overwrite_line_cb_8")
        self.overwrite_line_cb_8.addItem("")
        self.overwrite_line_cb_8.addItem("")
        self.overwrite_line_cb_8.addItem("")
        self.overwrite_line_cb_8.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_8, 7, 1, 1, 1)
        self.overwrite_line_cb_11 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_11.setObjectName("overwrite_line_cb_11")
        self.overwrite_line_cb_11.addItem("")
        self.overwrite_line_cb_11.addItem("")
        self.overwrite_line_cb_11.addItem("")
        self.overwrite_line_cb_11.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_11, 10, 1, 1, 1)
        self.overwrite_line_cb_9 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_9.setObjectName("overwrite_line_cb_9")
        self.overwrite_line_cb_9.addItem("")
        self.overwrite_line_cb_9.addItem("")
        self.overwrite_line_cb_9.addItem("")
        self.overwrite_line_cb_9.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_9, 8, 1, 1, 1)
        self.overwrite_line_cb_12 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_12.setObjectName("overwrite_line_cb_12")
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
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_13, 12, 1, 1, 1)
        self.overwrite_line_cb_24 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_24.setObjectName("overwrite_line_cb_24")
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
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_25, 24, 1, 1, 1)
        self.overwrite_line_cb_23 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_23.setObjectName("overwrite_line_cb_23")
        self.overwrite_line_cb_23.addItem("")
        self.overwrite_line_cb_23.addItem("")
        self.overwrite_line_cb_23.addItem("")
        self.overwrite_line_cb_23.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_23, 22, 1, 1, 1)
        self.overwrite_line_cb_1 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_1.setObjectName("overwrite_line_cb_1")
        self.overwrite_line_cb_1.addItem("")
        self.overwrite_line_cb_1.addItem("")
        self.overwrite_line_cb_1.addItem("")
        self.overwrite_line_cb_1.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_1, 0, 1, 1, 1)
        self.overwrite_line_cb_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_3.setObjectName("overwrite_line_cb_3")
        self.overwrite_line_cb_3.addItem("")
        self.overwrite_line_cb_3.addItem("")
        self.overwrite_line_cb_3.addItem("")
        self.overwrite_line_cb_3.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_3, 2, 1, 1, 1)
        self.overwrite_line_cb_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_2.setObjectName("overwrite_line_cb_2")
        self.overwrite_line_cb_2.addItem("")
        self.overwrite_line_cb_2.addItem("")
        self.overwrite_line_cb_2.addItem("")
        self.overwrite_line_cb_2.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_2, 1, 1, 1, 1)
        self.overwrite_line_cb_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_4.setObjectName("overwrite_line_cb_4")
        self.overwrite_line_cb_4.addItem("")
        self.overwrite_line_cb_4.addItem("")
        self.overwrite_line_cb_4.addItem("")
        self.overwrite_line_cb_4.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_4, 3, 1, 1, 1)
        self.overwrite_line_cb_6 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_6.setObjectName("overwrite_line_cb_6")
        self.overwrite_line_cb_6.addItem("")
        self.overwrite_line_cb_6.addItem("")
        self.overwrite_line_cb_6.addItem("")
        self.overwrite_line_cb_6.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_6, 5, 1, 1, 1)
        self.overwrite_line_cb_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_5.setObjectName("overwrite_line_cb_5")
        self.overwrite_line_cb_5.addItem("")
        self.overwrite_line_cb_5.addItem("")
        self.overwrite_line_cb_5.addItem("")
        self.overwrite_line_cb_5.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_5, 4, 1, 1, 1)
        self.overwrite_line_cb_7 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overwrite_line_cb_7.setObjectName("overwrite_line_cb_7")
        self.overwrite_line_cb_7.addItem("")
        self.overwrite_line_cb_7.addItem("")
        self.overwrite_line_cb_7.addItem("")
        self.overwrite_line_cb_7.addItem("")
        self.time_series_translator_grid.addWidget(self.overwrite_line_cb_7, 6, 1, 1, 1)
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
        self.update_btn = QtWidgets.QPushButton(self.time_series_translator_gb)
        self.update_btn.setGeometry(QtCore.QRect(770, 1280, 150, 30))
        self.update_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.update_btn.setObjectName("update_btn")
        self.next_page = QtWidgets.QPushButton(self.time_series_translator_gb)
        self.next_page.setGeometry(QtCore.QRect(480, 1330, 75, 23))
        self.next_page.setObjectName("next_page")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.time_series_translator_gb.setTitle(_translate("Dialog", "Select Timeseries Type:"))
        self.overwrite_line_cb_14.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_14.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_14.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_14.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_18.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_18.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_18.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_18.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_17.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_17.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_17.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_17.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_15.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_15.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_15.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_15.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_16.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_16.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_16.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_16.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_21.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_21.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_21.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_21.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_19.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_19.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_19.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_19.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_22.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_22.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_22.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_22.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_20.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_20.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_20.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_20.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_10.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_10.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_10.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_10.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_8.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_8.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_8.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_8.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_11.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_11.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_11.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_11.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_9.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_9.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_9.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_9.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_12.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_12.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_12.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_12.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_13.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_13.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_13.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_13.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_24.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_24.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_24.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_24.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_25.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_25.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_25.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_25.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_23.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_23.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_23.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_23.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_1.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_1.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_1.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_1.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_3.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_3.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_3.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_3.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_2.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_2.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_2.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_2.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_4.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_4.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_4.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_4.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_6.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_6.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_6.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_6.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_5.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_5.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_5.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_5.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.overwrite_line_cb_7.setItemText(0, _translate("Dialog", "Electric Field Potential Timeseries"))
        self.overwrite_line_cb_7.setItemText(1, _translate("Dialog", "Alignment Timeseries"))
        self.overwrite_line_cb_7.setItemText(2, _translate("Dialog", "Stimulus Timeseries"))
        self.overwrite_line_cb_7.setItemText(3, _translate("Dialog", "Other Timeseries Data"))
        self.update_btn.setText(_translate("Dialog", "Update/Verify"))
        self.next_page.setText(_translate("Dialog", "Next Page"))

#Code starts here
        self.initializePage()

   

    def initializePage(self):
        global matlab_file
        matlab_file = h5py.File('INT017_180629.mat', 'r')

        counter = 1
        text_box_prefix = 'overwrite_le_'

        for struct in matlab_file:
            current_text_box_being_edited = text_box_prefix + str(counter)
            print(struct + " text box is " + current_text_box_being_edited)
            eval("self." + current_text_box_being_edited + ".setText(\"" + str(struct) + "\")")
            print("set the value of the text in " + current_text_box_being_edited + ".text() to " + struct)
            counter = counter + 1


        #Hook mup the button
        self.update_btn.clicked.connect(self.on_click_update)

        global arrays
        arrays = {}
        for struct, field in matlab_file.items():
            # iterate through group (comment, scale, values, etc.)
            # extract fields of structure within each field (hdf5 group)
            group_dict = {}
            for timeseries, values in field.items():
                # fill group dict with contents of array read into memory ([:])
                # TODO: use read_direct() method to avoid memory duplication
                group_dict[timeseries] = values[:]
            
            #arrays[k] = np.array(v)
            arrays[struct] = group_dict

        # line_edit.setName("line_1")
        # line_edit.textEdited.connect(self.line_edited)

        # QtCore.sender().name()

    def load_data(self):
        # to reliably convert strings - need to know how matlab encodes strings/character arrays to save in .mat
        # files, so we can reverse it exactly -- for example if matlab uses ASCII then simple chr() should work,
        # but may be more complicated if saves in utf-8
        # at the moment appears to use ASCII for a 'comment' field that reads 'no comment'
        # ie. 'no comment' == [78, 111, 32, ...]

        ## convert text from ordinal example
        # convert to list for jonny's convenience -- more comfortable with list comprehensions than numpy
        # comment_list = alignment_timeseries_dict['INT017_180629_Ch1']['comment'].tolist()
        # comment_list will be a list of lists of ints, [[100], [200], etc.]
        # 
        # convert each number to character
        # comment = [str(chr(a_character[0])) for a_character in comment_list]
        #
        # join to string
        # comment = "".join(comment)

        pass

    def init_ui():
        pass

        # to implement reusable edit fields, connect their editingFinished signal to the logic you want
        # eg.
        # to add 25 rows to a window
        # self.edit_widgets = {}
        # for i in range(25):   
            # widget_name = "edit_number_" + str(i)
            # ledit = QtGui.LineEdit('beginning_text')
            # ledit.setName(widget_name)
            # ledit.editingFinished.connect(self.set_type)
            # ... add to layout ..
            # self.edit_widgets[widget_name] = ledit

        # and then in self.set_type
        # if this object were a QMainWindow or QWidget you could use sender()
        # sender_name = self.sender().name / .getName()
        #
        # otherwise use lambda functions
        # ledit.editingFinished.connect(lambda: self.set_type("edit_number_" + str(i)))

    def set_type(self, sender_name):
        # if using lambda functions, accept sender_name as first argument after self
        # get the object
        # widget_text = self.edit_widgets[sender_name].currentText()
        # do the rest of the logic in on_click_update
        # if widget_text == '...'
            # do this
        pass



    def on_click_update(self):
        global matlab_file

        global electric_timeseries_dict
        electric_timeseries_dict = {}
        global alignment_timeseries_dict
        alignment_timeseries_dict = {}
        global stimulus_timeseries_dict
        stimulus_timeseries_dict = {}
        global other_timeseries_dict
        other_timeseries_dict = {}
        
        if self.overwrite_line_cb_1.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_1.text()))
            electric_timeseries_dict[str(self.overwrite_le_1.text())] = x # Ways I tried to extract keys/values matlab_file['/INT017_180629_Ch1/title']) # (self.overwrite_le_2.text(), str(self.overwrite_le_2.text())), arrays.get('INT017_180629_Ch2')
            print(electric_timeseries_dict)
        elif self.overwrite_line_cb_1.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_1.text()))
            alignment_timeseries_dict[str(self.overwrite_le_1.text())] = x
            print(alignment_timeseries_dict)
        elif self.overwrite_line_cb_1.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_1.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_1.text())] = x
            print(stimulus_timeseries_dict)
        else:
            x = arrays.get(str(self.overwrite_le_1.text()))
            other_timeseries_dict[str(self.overwrite_le_1.text())] = x
            print(other_timeseries_dict)


        if self.overwrite_line_cb_2.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_2.text()))
            electric_timeseries_dict[str(self.overwrite_le_2.text())] = x 
            print(electric_timeseries_dict)
        elif self.overwrite_line_cb_2.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_2.text()))
            alignment_timeseries_dict[str(self.overwrite_le_2.text())] = x
            print(alignment_timeseries_dict)
        elif self.overwrite_line_cb_2.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_2.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_2.text())] = x
            print(stimulus_timeseries_dict)
        else:
            x = arrays.get(str(self.overwrite_le_2.text()))
            other_timeseries_dict[str(self.overwrite_le_2.text())] = x
            print(other_timeseries_dict)


        if self.overwrite_line_cb_3.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_3.text()))
            electric_timeseries_dict[str(self.overwrite_le_3.text())] = x 
        elif self.overwrite_line_cb_3.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_3.text()))
            alignment_timeseries_dict[str(self.overwrite_le_3.text())] = x
        elif self.overwrite_line_cb_3.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_3.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_3.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_3.text()))
            other_timeseries_dict[str(self.overwrite_le_3.text())] = x

        if self.overwrite_line_cb_4.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_4.text()))
            electric_timeseries_dict[str(self.overwrite_le_4.text())] = x 
        elif self.overwrite_line_cb_4.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_4.text()))
            alignment_timeseries_dict[str(self.overwrite_le_4.text())] = x
        elif self.overwrite_line_cb_4.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_4.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_4.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_4.text()))
            other_timeseries_dict[str(self.overwrite_le_4.text())] = x

        if self.overwrite_line_cb_5.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_5.text()))
            electric_timeseries_dict[str(self.overwrite_le_5.text())] = x 
        elif self.overwrite_line_cb_5.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_5.text()))
            alignment_timeseries_dict[str(self.overwrite_le_5.text())] = x
        elif self.overwrite_line_cb_5.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_5.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_5.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_5.text()))
            other_timeseries_dict[str(self.overwrite_le_5.text())] = x
                  

        if self.overwrite_line_cb_6.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_6.text()))
            electric_timeseries_dict[str(self.overwrite_le_6.text())] = x 
        elif self.overwrite_line_cb_6.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_6.text()))
            alignment_timeseries_dict[str(self.overwrite_le_6.text())] = x
        elif self.overwrite_line_cb_6.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_6.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_6.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_6.text()))
            other_timeseries_dict[str(self.overwrite_le_6.text())] = x


        if self.overwrite_line_cb_7.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_7.text()))
            electric_timeseries_dict[str(self.overwrite_le_7.text())] = x 
        elif self.overwrite_line_cb_7.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_7.text()))
            alignment_timeseries_dict[str(self.overwrite_le_7.text())] = x
        elif self.overwrite_line_cb_7.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_7.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_7.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_7.text()))
            other_timeseries_dict[str(self.overwrite_le_7.text())] = x                          


        if self.overwrite_line_cb_8.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_8.text()))
            electric_timeseries_dict[str(self.overwrite_le_8.text())] = x 
        elif self.overwrite_line_cb_8.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_8.text()))
            alignment_timeseries_dict[str(self.overwrite_le_8.text())] = x
        elif self.overwrite_line_cb_8.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_8.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_8.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_8.text()))
            other_timeseries_dict[str(self.overwrite_le_8.text())] = x

        if self.overwrite_line_cb_9.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_9.text()))
            electric_timeseries_dict[str(self.overwrite_le_9.text())] = x 
        elif self.overwrite_line_cb_9.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_9.text()))
            alignment_timeseries_dict[str(self.overwrite_le_9.text())] = x
        elif self.overwrite_line_cb_9.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_9.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_9.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_9.text()))
            other_timeseries_dict[str(self.overwrite_le_9.text())] = x            
        
        
        if self.overwrite_line_cb_10.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_10.text()))
            electric_timeseries_dict[str(self.overwrite_le_10.text())] = x 
        elif self.overwrite_line_cb_10.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_10.text()))
            alignment_timeseries_dict[str(self.overwrite_le_10.text())] = x
        elif self.overwrite_line_cb_10.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_10.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_10.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_10.text()))
            other_timeseries_dict[str(self.overwrite_le_10.text())] = x


        if self.overwrite_line_cb_11.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_11.text()))
            electric_timeseries_dict[str(self.overwrite_le_11.text())] = x 
        elif self.overwrite_line_cb_11.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_11.text()))
            alignment_timeseries_dict[str(self.overwrite_le_11.text())] = x
        elif self.overwrite_line_cb_11.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_11.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_11.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_11.text()))
            other_timeseries_dict[str(self.overwrite_le_11.text())] = x

        
        if self.overwrite_line_cb_12.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_12.text()))
            electric_timeseries_dict[str(self.overwrite_le_12.text())] = x 
        elif self.overwrite_line_cb_12.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_12.text()))
            alignment_timeseries_dict[str(self.overwrite_le_12.text())] = x
        elif self.overwrite_line_cb_12.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_12.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_12.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_12.text()))
            other_timeseries_dict[str(self.overwrite_le_12.text())] = x

        if self.overwrite_line_cb_13.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_13.text()))
            electric_timeseries_dict[str(self.overwrite_le_13.text())] = x 
        elif self.overwrite_line_cb_13.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_13.text()))
            alignment_timeseries_dict[str(self.overwrite_le_13.text())] = x
        elif self.overwrite_line_cb_13.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_13.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_13.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_13.text()))
            other_timeseries_dict[str(self.overwrite_le_13.text())] = x


        if self.overwrite_line_cb_14.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_14.text()))
            electric_timeseries_dict[str(self.overwrite_le_14.text())] = x 
        elif self.overwrite_line_cb_14.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_14.text()))
            alignment_timeseries_dict[str(self.overwrite_le_14.text())] = x
        elif self.overwrite_line_cb_14.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_14.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_14.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_14.text()))
            other_timeseries_dict[str(self.overwrite_le_14.text())] = x

        
        if self.overwrite_line_cb_15.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_15.text()))
            electric_timeseries_dict[str(self.overwrite_le_15.text())] = x 
        elif self.overwrite_line_cb_15.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_15.text()))
            alignment_timeseries_dict[str(self.overwrite_le_15.text())] = x
        elif self.overwrite_line_cb_15.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_15.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_15.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_15.text()))
            other_timeseries_dict[str(self.overwrite_le_15.text())] = x

        
        if self.overwrite_line_cb_16.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_16.text()))
            electric_timeseries_dict[str(self.overwrite_le_16.text())] = x 
        elif self.overwrite_line_cb_16.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_16.text()))
            alignment_timeseries_dict[str(self.overwrite_le_16.text())] = x
        elif self.overwrite_line_cb_16.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_16.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_16.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_16.text()))
            other_timeseries_dict[str(self.overwrite_le_16.text())] = x


        if self.overwrite_line_cb_17.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_17.text()))
            electric_timeseries_dict[str(self.overwrite_le_17.text())] = x 
        elif self.overwrite_line_cb_17.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_17.text()))
            alignment_timeseries_dict[str(self.overwrite_le_17.text())] = x
        elif self.overwrite_line_cb_17.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_17.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_17.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_17.text()))
            other_timeseries_dict[str(self.overwrite_le_17.text())] = x


        if self.overwrite_line_cb_18.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_18.text()))
            electric_timeseries_dict[str(self.overwrite_le_18.text())] = x 
        elif self.overwrite_line_cb_18.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_18.text()))
            alignment_timeseries_dict[str(self.overwrite_le_18.text())] = x
        elif self.overwrite_line_cb_18.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_18.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_18.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_18.text()))
            other_timeseries_dict[str(self.overwrite_le_18.text())] = x


        if self.overwrite_line_cb_19.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_19.text()))
            electric_timeseries_dict[str(self.overwrite_le_19.text())] = x 
        elif self.overwrite_line_cb_19.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_19.text()))
            alignment_timeseries_dict[str(self.overwrite_le_19.text())] = x
        elif self.overwrite_line_cb_19.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_19.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_19.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_19.text()))
            other_timeseries_dict[str(self.overwrite_le_19.text())] = x


        if self.overwrite_line_cb_20.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_20.text()))
            electric_timeseries_dict[str(self.overwrite_le_20.text())] = x 
        elif self.overwrite_line_cb_20.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_20.text()))
            alignment_timeseries_dict[str(self.overwrite_le_20.text())] = x
        elif self.overwrite_line_cb_20.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_20.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_20.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_20.text()))
            other_timeseries_dict[str(self.overwrite_le_20.text())] = x


        if self.overwrite_line_cb_21.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_21.text()))
            electric_timeseries_dict[str(self.overwrite_le_21.text())] = x 
        elif self.overwrite_line_cb_21.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_21.text()))
            alignment_timeseries_dict[str(self.overwrite_le_21.text())] = x
        elif self.overwrite_line_cb_21.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_21.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_21.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_21.text()))
            other_timeseries_dict[str(self.overwrite_le_21.text())] = x


        if self.overwrite_line_cb_22.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_22.text()))
            electric_timeseries_dict[str(self.overwrite_le_22.text())] = x 
        elif self.overwrite_line_cb_22.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_22.text()))
            alignment_timeseries_dict[str(self.overwrite_le_22.text())] = x
        elif self.overwrite_line_cb_22.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_22.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_22.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_22.text()))
            other_timeseries_dict[str(self.overwrite_le_22.text())] = x


        if self.overwrite_line_cb_23.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_23.text()))
            electric_timeseries_dict[str(self.overwrite_le_23.text())] = x 
        elif self.overwrite_line_cb_23.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_23.text()))
            alignment_timeseries_dict[str(self.overwrite_le_23.text())] = x
        elif self.overwrite_line_cb_23.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_23.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_23.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_23.text()))
            other_timeseries_dict[str(self.overwrite_le_23.text())] = x


        if self.overwrite_line_cb_24.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_24.text()))
            electric_timeseries_dict[str(self.overwrite_le_24.text())] = x 
        elif self.overwrite_line_cb_24.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_24.text()))
            alignment_timeseries_dict[str(self.overwrite_le_24.text())] = x
        elif self.overwrite_line_cb_24.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_24.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_24.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_24.text()))
            other_timeseries_dict[str(self.overwrite_le_24.text())] = x

        if self.overwrite_line_cb_25.currentText() == "Electric Field Potential Timeseries":
            x = arrays.get(str(self.overwrite_le_25.text()))
            electric_timeseries_dict[str(self.overwrite_le_25.text())] = x 
        elif self.overwrite_line_cb_25.currentText() == "Alignment Timeseries":
            x = arrays.get(str(self.overwrite_le_25.text()))
            alignment_timeseries_dict[str(self.overwrite_le_25.text())] = x
        elif self.overwrite_line_cb_25.currentText() == "Stimulus Timeseries":
            x = arrays.get(str(self.overwrite_le_25.text()))
            stimulus_timeseries_dict[str(self.overwrite_le_25.text())] = x
        else:
            x = arrays.get(str(self.overwrite_le_25.text()))
            other_timeseries_dict[str(self.overwrite_le_25.text())] = x 

        # to debug this section/(i think any Qt method?)
        # have to use this additional 'removeinputhook' method so 
        # qt doesn't print 'the event loop is already running' over and over
        # QtCore.pyqtRemoveInputHook()
        # pdb.set_trace()  

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    matlab_file = ''
    arrays = ''