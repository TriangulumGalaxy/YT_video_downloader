# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 373)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(561, 374))
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color: rgb(148, 148, 148);\n"
"}\n"
"Line {\n"
"background-color: rgb(222, 222, 222);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setStyleSheet("#path {\n"
"    border-width: 1.5px;\n"
"    border-style: solid;\n"
"    border-color: rgb(79, 79, 79);\n"
"    background-color: #52595d;\n"
"    color: white;\n"
"    border-radius: 80px;\n"
"}")
        self.path.setReadOnly(True)
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 2, 4, 1, 1)
        self.pathButton = QtWidgets.QPushButton(self.centralwidget)
        self.pathButton.setStyleSheet("#pathButton {\n"
"    padding: 2px;\n"
"    border: 2px solid rgb(85, 85, 85);\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: white;\n"
"    font: 9pt \"Bahnschrift SemiBold\";\n"
"}\n"
"#pathButton:hover {\n"
"    padding: 2px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: none;\n"
"    background-color: rgb(85, 85, 85);\n"
"    font: 9pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}")
        self.pathButton.setObjectName("pathButton")
        self.gridLayout.addWidget(self.pathButton, 2, 5, 1, 1)
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setText("")
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 4, 4, 1, 1)
        self.pBar = QtWidgets.QProgressBar(self.centralwidget)
        self.pBar.setEnabled(True)
        self.pBar.setStyleSheet("#pBar {\n"
"    padding: 4px;\n"
"    text-align: center;\n"
"    color: #d3dae3;\n"
"    border-radius: 10px;\n"
"    border-color: transparent;\n"
"    border-style: solid;\n"
"    background-color: #52595d;\n"
"}\n"
"#pBar::chunk {\n"
"    background-color: #214037    ;\n"
"    border-radius: 10px;\n"
"}")
        self.pBar.setProperty("value", 0)
        self.pBar.setTextVisible(True)
        self.pBar.setObjectName("pBar")
        self.gridLayout.addWidget(self.pBar, 8, 4, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("#lineEdit {\n"
"    border-width: 1.5px;\n"
"    border-style: solid;\n"
"    border-color: rgb(79, 79, 79);\n"
"    background-color: #52595d;\n"
"    color: white;\n"
"    border-radius: 80px;\n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 4, 1, 1)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setMouseTracking(False)
        self.downloadButton.setStyleSheet("#downloadButton {\n"
"    padding: 2px;\n"
"    border: 2px solid rgb(85, 85, 85);\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: white;\n"
"    font: 9pt \"Bahnschrift SemiBold\";\n"
"}\n"
"#downloadButton:hover {\n"
"    padding: 2px;\n"
"    color: rgb(255, 255, 255);\n"
"    border: none;\n"
"    background-color: rgb(85, 85, 85);\n"
"    font: 9pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}")
        self.downloadButton.setObjectName("downloadButton")
        self.gridLayout.addWidget(self.downloadButton, 1, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 4, 1, 2)
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setMaximumSize(QtCore.QSize(480, 270))
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 5, 4, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 9, 4, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 4, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Video downloader"))
        self.pathButton.setText(_translate("MainWindow", "Choose path"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Video URL"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
