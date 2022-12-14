#Kutuphaneler eklendi
import sys 
from PyQt6.QtWidgets import * 
from form1 import Ui_MainWindow


class Anaform(QMainWindow,Ui_MainWindow):
        def __init__(self):
                super(Anaform,self).__init__() 
                self.setupUi(self)
                self.show()
                self.pushButton.clicked.connect(self.ekle)
                self.comboBox.activated.connect(self.labelaYaz)
             
                
                    
        def ekle(self):
            x=self.lineEdit.text()
            self.comboBox.addItem(x)
            self.lineEdit.setText(None)     
            
        def labelaYaz(self):
            x=self.comboBox.currentText()
            self.label.setText(x)
         
          
            
            
                            
                
                
       
                    
                
                
proje = QApplication(sys.argv)
form1 = Anaform()
form1.resize(500,500)
sys.exit(proje.exec())



