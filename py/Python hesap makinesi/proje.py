import sys
from PyQt6.QtWidgets import *
from form1 import Ui_MainWindow


class Anaform(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.topla)
        self.pushButton_2.clicked.connect(self.sil)
        self.pushButton_3.clicked.connect(self.bol)
        self.pushButton_4.clicked.connect(self.carp)

    def topla(self):
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        sonuc = int(x) + int(y)
        self.label.setText(str(sonuc))

    def sil(self):
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        sonuc = int(x) - int(y)
        self.label.setText(str(sonuc))

    def bol(self):
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        sonuc = int(x) / int(y)
        self.label.setText(str(sonuc))

    def carp(self):
        x = self.lineEdit.text()
        y = self.lineEdit_2.text()
        sonuc = int(x) * int(y)
        self.label.setText(str(sonuc))

   
        
      
            



proje = QApplication(sys.argv)
form1 = Anaform()
form1.resize(800, 400)
sys.exit(proje.exec())
