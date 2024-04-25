# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyDetector.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 271)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(134, 134, 134, 255), stop:0.5 rgba(124, 124, 124, 255));\n"
"border-radius: 10px;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 191, 481))
        self.frame.setStyleSheet("border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 20, 191, 61))
        self.frame_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));\n"
"border-radius: 10px;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 61))
        self.label.setStyleSheet("font: 75 14pt \"Calisto MT\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 100, 191, 71))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    font: 75 30pt \"Calisto MT\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: Opx solid;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 170, 191, 71))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    font: 75 30pt \"Calisto MT\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: Opx solid;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        #self.label_3 = QtWidgets.QLabel(self.frame)
        #self.label_3.setGeometry(QtCore.QRect(40, 260, 91, 31))
        #self.label_3.setStyleSheet("font: 8pt \"Calisto MT\";")
        #self.label_3.setText("")
        #self.label_3.setPixmap(QtGui.QPixmap("logoLabsia.png"))
        #self.label_3.setScaledContents(True)
        #self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 0, 461, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("PyDetector.JPG"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyDetector"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">MACHINES</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "SOM"))
        self.pushButton_2.setText(_translate("MainWindow", "MLP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

