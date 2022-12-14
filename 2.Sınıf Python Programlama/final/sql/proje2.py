import sys
from PyQt6.QtWidgets import *
from ui_form1 import Ui_MainWindow
import pypyodbc as odbc

class AnaForm(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btnRun.clicked.connect(self.Run)
   
    def Run(self):
        baglanti =odbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-6G93D3J\SQLEXPRESS;DATABASE=kutuphane; UID=;PWD=')
        imlec = baglanti.cursor()
        
        #Alan adlarının seçilmesi
        alanlist = list()
        for x in imlec.columns("ogrenci"):
            alanlist.append(x[3])
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(alanlist))
        self.tableWidget.setHorizontalHeaderLabels(alanlist)    
        imlec.execute(self.textEdit.toPlainText())   # metin bileşenindeki yazıyı al 
        sonuc=imlec.fetchall()
        for i,kayit in enumerate(sonuc):
                self.tableWidget.insertRow(i)
                for j,sutun in enumerate(kayit):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(sutun)))
                
proje2 = QApplication(sys.argv) 
form1 = AnaForm()
proje2.exec()

       
        
        
        