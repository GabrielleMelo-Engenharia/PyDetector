# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:22:19 2020

@author: gaby1
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyDetector import*
from Janela2_MLP import*
from JanelaSom import*






        
class Janela3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_janela3()
        self.ui.setupUi(self)
        
class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_janela2()
        self.ui.setupUi(self)

class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.jan2= Janela2()
        
        self.ui.pushButton.clicked.connect(self.mudaJanela)
        
        self.jan3= Janela3()
        
        self.ui.pushButton_2.clicked.connect(self.mudaJanela1)
        
    def mudaJanela(self):
        self.jan2.show()
        
    def mudaJanela1(self):
        self.jan3.show()
        
    
        
        
    
    
        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    w= Tela()
    w.show()
    sys.exit(app.exec_())
