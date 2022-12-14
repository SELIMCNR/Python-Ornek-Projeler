import sys 
from PyQt6.QtWidgets import * 
from form1 import Ui_MainWindow


class AnaForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AnaForm,self).__init__()
        self.setupUi(self)
        self.show()
        self.BenimButtonum.clicked.connect(self.ekle)
        self.pushButton.clicked.connect(self.temizle)
        self.pushButton_2.clicked.connect(self.ArayaEkle)
       # self.comboBox.activated(self.textEditEkle)
        self.radioButton.clicked.connect(lambda: self.EtiketeYaz(
        self.radioButton))  # lamda: özel bir fonksiyon
        self.radioButton_2.clicked.connect(
            lambda: self.EtiketeYaz(self.radioButton_2))

    # a parametresi lambda dan gelen radioButton ların 3'ünü içeriyor.
    def EtiketeYaz(self, a):
        x = a.text()
        self.label.setText(x)      
        
    #def textEditEkle(self):
     #   x=self.comboBox.currentText() #Line editeki değeri alır
      #  self.textEdit.append(x)          
        
    def ekle(self):
        x=self.lineEdit.text()
        self.label.setText(x)
        self.listWidget.addItem(x)
        self.comboBox.addItem(x)
        self.lineEdit.clear()
        
    def temizle(self):
        self.label.clear()
        self.lineEdit.clear()
        self.listWidget.clear()
        self.comboBox.clear()
        
    def ArayaEkle(self):
        y=self.lineEdit.text()
        #index=self.listWidget.currentRow()
        self.listWidget.insertItem(3,y) 

proje = QApplication(sys.argv)
form1 = AnaForm()
sys.exit(proje.exec())
