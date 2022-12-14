import sys
from PyQt6.QtWidgets import*
from form1 import Ui_MainWindow

class AnaForm(QMainWindow,Ui_MainWindow):
       def __init__(self):
              super().__init__()
              self.setupUi(self)
              self.show()
              self.pushButton.clicked.connect(self.ekle)
              self.pushButton_2.clicked.connect(self.sil)
              self.pushButton_3.clicked.connect(self.arayaEkle)
              self.comboBox.activated.connect(self.yaz) 
              self.listWidget.itemClicked.connect(self.etiketeYaz)
              
              
       def arayaEkle(self):
              x= self.lineEdit.text()
              index = self.listWidget.currentRow()
              self.listWidget.insertItem(index,x)
                     
       
       
       
              
       def ekle(self):
              x=self.lineEdit.text()
              self.comboBox.addItem(x)
              self.lineEdit.setText(None)
       def sil(self):
              self.comboBox.clear()
       
       def yaz(self):
              y=self.comboBox.currentText() 
              self.listWidget.addItem(y)
       def etiketeYaz(self):   
              x=self.listWidget.currentItem().text()
              self.label.setText(x)
              a=self.listWidget.currentRow()
              print(a)
                        
              
Proje=QApplication(sys.argv)
form1=AnaForm()
sys.exit(Proje.exec())
