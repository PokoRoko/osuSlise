# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 392)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(30, 28))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameDifficulty = QtWidgets.QLineEdit(self.centralwidget)
        self.nameDifficulty.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.nameDifficulty.setMaxLength(30)
        self.nameDifficulty.setObjectName("nameDifficulty")
        self.verticalLayout.addWidget(self.nameDifficulty)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.numRepeat = QtWidgets.QSpinBox(self.centralwidget)
        self.numRepeat.setMinimum(1)
        self.numRepeat.setSingleStep(1)
        self.numRepeat.setProperty("value", 20)
        self.numRepeat.setObjectName("numRepeat")
        self.verticalLayout.addWidget(self.numRepeat)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.interval = QtWidgets.QSpinBox(self.centralwidget)
        self.interval.setMaximum(30000)
        self.interval.setSingleStep(250)
        self.interval.setProperty("value", 6000)
        self.interval.setObjectName("interval")
        self.verticalLayout.addWidget(self.interval)
        self.buttonStartSlice = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStartSlice.setObjectName("buttonStartSlice")
        self.verticalLayout.addWidget(self.buttonStartSlice)
        self.logText = QtWidgets.QTextEdit(self.centralwidget)
        self.logText.setEnabled(False)
        self.logText.setObjectName("logText")
        self.verticalLayout.addWidget(self.logText)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.interval, self.nameDifficulty)
        MainWindow.setTabOrder(self.nameDifficulty, self.buttonStartSlice)
        MainWindow.setTabOrder(self.buttonStartSlice, self.numRepeat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "osuSlice"))
        self.label.setText(_translate("MainWindow", "Name difficulty to find"))
        self.nameDifficulty.setText(_translate("MainWindow", "train"))
        self.label_2.setText(_translate("MainWindow", "Number of repeat"))
        self.label_3.setText(_translate("MainWindow", "Interval between repeats (ms)"))
        self.buttonStartSlice.setText(_translate("MainWindow", "Start Slice"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))