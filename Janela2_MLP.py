# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Janela2_MLP.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from debutanizadora_teste1 import Data, RNA_ml, Kohonen_ml
from PIL import Image

class Ui_janela3(object):
    def setupUi(self, janela3):
        janela3.setObjectName("janela3")
        janela3.resize(1265, 724)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janela3.setWindowIcon(icon)
        janela3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(134, 134, 134, 255), stop:0.5 rgba(124, 124, 124, 255));\n"
"border-radius: 10px;")
        self.centralwidget = QtWidgets.QWidget(janela3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 10, 121, 61))
        self.label.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"border-radius: 0px;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 0, 71, 71))
        self.label_2.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"border-radius: 0px;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("medical (2).png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760, 0, 71, 71))
        self.label_3.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"border-radius: 0px;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("color (1).png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 40, 121, 21))
        self.label_4.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_4.setObjectName("label_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 70, 91, 17))
        self.radioButton_2.setStyleSheet("\n"
"font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(110, 70, 91, 17))
        self.radioButton.setStyleSheet("\n"
"font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 100, 71, 21))
        self.label_5.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 130, 91, 21))
        self.label_6.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 160, 171, 21))
        self.label_7.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 190, 141, 21))
        self.label_8.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 220, 161, 21))
        self.label_9.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 250, 141, 21))
        self.label_10.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 280, 391, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(110, 310, 151, 21))
        self.label_11.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_11.setObjectName("label_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 340, 391, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 100, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 130, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 160, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(390, 190, 113, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(390, 220, 113, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 150, 251, 71))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 80, 251, 71))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 220, 251, 71))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(650, 220, 41, 61))
        self.label_14.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("arrows.png"))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(930, 80, 251, 20))
        self.label_15.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_15.setObjectName("label_15")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(930, 80, 251, 211))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(930, 80, 251, 20))
        self.label_16.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(660, 310, 521, 20))
        self.label_18.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(190, 440, 251, 20))
        self.label_19.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_19.setObjectName("label_19")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(660, 330, 521, 341))
        self.label_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(650, 90, 41, 51))
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("arrow (1).png"))
        self.label_13.setObjectName("label_13")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(650, 230, 41, 61))
        self.label_20.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("arrows.png"))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(650, 160, 31, 51))
        self.label_21.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("business-and-finance.png"))
        self.label_21.setObjectName("label_21")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(232, 380, 271, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(110, 380, 111, 21))
        self.label_12.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_12.setObjectName("label_12")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 460, 251, 211))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.comboBox.raise_()
        self.label_11.raise_()
        self.comboBox_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.textEdit.raise_()
        self.label_16.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_17.raise_()
        self.label_13.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.lineEdit_6.raise_()
        self.label_12.raise_()
        self.textEdit_2.raise_()
        janela3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(janela3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        janela3.setMenuBar(self.menubar)
        self.actionUndo = QtWidgets.QAction(janela3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon1)
        self.actionUndo.setObjectName("actionUndo")
        self.actionQuit = QtWidgets.QAction(janela3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.menuOptions.addAction(self.actionUndo)
        self.menuOptions.addAction(self.actionQuit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(janela3)
        self.actionQuit.triggered.connect(janela3.close)
        QtCore.QMetaObject.connectSlotsByName(janela3)

    def retranslateUi(self, janela3):
        _translate = QtCore.QCoreApplication.translate
        janela3.setWindowTitle(_translate("janela3", "PyDetector"))
        self.label.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">MLP</span></p></body></html>"))
        self.label_4.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Normalization:</span></p></body></html>"))
        self.radioButton_2.setText(_translate("janela3", "Standard"))
        self.radioButton.setText(_translate("janela3", "Min Max"))
        self.label_5.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Epochs:</span></p></body></html>"))
        self.label_6.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Tolerance:</span></p></body></html>"))
        self.label_7.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Percentage to test (%):</span></p></body></html>"))
        self.label_8.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Number of layers:</span></p></body></html>"))
        self.label_9.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Number of neurons:</span></p></body></html>"))
        self.label_10.setText(_translate("janela3", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Transfer Function:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("janela3", "Identity Function"))
        self.comboBox.setItemText(1, _translate("janela3", "The Logistic Sigmoid Function"))
        self.comboBox.setItemText(2, _translate("janela3", "The Hyperbolic Tangent Function"))
        self.comboBox.setItemText(3, _translate("janela3", "Rectified Linear Unit Function"))
        self.label_11.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Training Algorithm:</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("janela3", "quasi-Newton"))
        self.comboBox_2.setItemText(1, _translate("janela3", "The Logistic Sigmoid Function"))
        self.comboBox_2.setItemText(2, _translate("janela3", "Stochastic Gradient Descent"))
        self.comboBox_2.setItemText(3, _translate("janela3", "Stochastic Gradient-based Optimizer"))
        self.pushButton_2.setText(_translate("janela3", "     Train and Test"))
        self.pushButton.setText(_translate("janela3", "  Load Data"))
        self.pushButton_3.setText(_translate("janela3", "   Save Figure"))
        self.label_15.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Information about the Data:</span></p></body></html>"))
        self.label_16.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Information about the Data:</span></p></body></html>"))
        self.label_18.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Vizualization of the graph:</span></p></body></html>"))
        self.label_19.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">MLP Evaluation:</span></p></body></html>"))
        self.label_12.setText(_translate("janela3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Class Column</span></p></body></html>"))
        self.menuOptions.setTitle(_translate("janela3", "Options"))
        self.actionUndo.setText(_translate("janela3", "Undo"))
        self.actionUndo.setShortcut(_translate("janela2", "Ctrl+Z"))
        self.actionQuit.setText(_translate("janela3", "Quit"))
        self.actionQuit.setShortcut(_translate("janela3", "Ctrl+C"))
        self.actionQuit.setShortcut(_translate("janela3", "Ctrl+C"))
        self.pushButton.clicked.connect(self.botao3_loadData_MLP) #botão de carregar dados da MLP
        self.pushButton_2.clicked.connect(self.botao2_testandtrain_MLP) #botão de testar e treinar MLP
       
        self.pushButton_3.clicked.connect(self.botao_saveMLP) #botão de salvar a figura de MLP
        self.actionUndo.triggered.connect(self.undo) #botão deesfazer
        
        
        
          
    
    def undo(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.label_17.clear()
        
        
        
    '''BOTÃO DE CARREGAR DADOS PARA MLP'''
        
    def botao3_loadData_MLP(self):
        self.open_dialog_box1()
        
    def open_dialog_box1(self):
        self.filename1,_= QFileDialog.getOpenFileName()
        if self.filename1.endswith('xlsx'):
          self.dataframe1= pd.read_excel(self.filename1,index_col=False)  
        else:
          self.dataframe1=pd.read_csv(self.filename1, index_col=False)   
         
        num_colunas= self.dataframe1.shape[1]
        num_variaveis= num_colunas-1
        total_dados= self.dataframe1.size
        dadosdaMLP= "\n\n\n\nVariable Numbers: {one}\n\n\nSamples Numbers: {two}\n\n\nTotal Data: {three}".format(one=num_variaveis,two=self.dataframe1.shape[0],three=total_dados)
        self.textEdit.setText(dadosdaMLP)
        
#####################################################################################################
        
        
    '''BOTÃO DE TESTAR E TREINAR A MLP'''        
        
    def botao2_testandtrain_MLP(self):
        E1= int(self.lineEdit.text())  #epocas
        E2= float(self.lineEdit_2.text())  #tolerancia
        E3= float(self.lineEdit_3.text())  #porcentagem de teste
        E4= self.lineEdit_6.text()  #class column
        E5= int(self.lineEdit_4.text()) #numero de camadas
        E6= int(self.lineEdit_5.text())  #numero de neuronios
        C2= self.comboBox.currentIndex() #funcao transferencia
        C3= self.comboBox_2.currentIndex() #algoritimo de treinamento
        
        test= E3/100
            
            
        if C2==0:
            transf_function= 'identity'
            
        elif C2==1:
            transf_function= 'logistic'
        elif C2==2:
            transf_function='tanh'
        else:
            transf_function= 'relu'
                
                
        if C3==0:
            algor_train= 'lbfgs'
            
        elif C3==1:
            algor_train= 'sgd'
        else:
            algor_train= 'adam'
            
            
        if self.radioButton.isChecked():
            RB1= 'Min Max'
        else:
            RB1= 'Standard'
        
        
            
        dados = Data(1,self.filename1,RB1,test,shuffle=True,output=E4)
        data = dados.preprocessing()
        labels = dados.getLabels()

        ml = RNA_ml(data,(E5,E6),transf_function,algor_train,1e-5,E1,E2)
        ml.train()
        scores= ml.evaluate()
        ml.plot(labels)
        f1, accuracy, precision,recall= scores[0], scores[1],scores[2],scores[3]
        evaluation_MLP= "\n\n\n {one}\n\n\n {two}\n\n\n {three}\n\n\n {four}".format(one=f1,two=accuracy,three=precision,four=recall)
        self.textEdit_2.setText(evaluation_MLP)
        ml.plot(labels) 
        self.figure_MLP= self.label_17.setPixmap(QtGui.QPixmap("ConfusionMatrix.png"))
        self.im1 = Image.open( 'ConfusionMatrix.png' )
        
################################################################################################################
    '''SAVE FIGURE_MLP'''
    
    def botao_saveMLP(self):
        self.open_dialog_box_MLP()
        
        
    def open_dialog_box_MLP(self):
        
        option= QFileDialog.Options()
        fileName1,_= QFileDialog.getSaveFileName() 
        self.im1.save(fileName1)
        
############################################################################################################################3



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela3 = QtWidgets.QMainWindow()
    ui = Ui_janela3()
    ui.setupUi(janela3)
    janela3.show()
    sys.exit(app.exec_())

