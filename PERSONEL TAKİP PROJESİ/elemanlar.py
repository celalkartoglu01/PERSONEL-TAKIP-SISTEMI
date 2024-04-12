from PyQt5.QtWidgets import *
from elemanlar_ import Ui_Form
import mysql.connector




con = mysql.connector.connect(user='root', password='', host='localhost', database='pts')
cursor = con.cursor()


class Elemanlar(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.elemanlar = Ui_Form()
        self.elemanlar.setupUi(self)
        self.elemanlar.getir.clicked.connect(self.Getir)
    



    def Getir(self):
        query = "select ad,soyad,telefon,eposta,adres,egitimdurumu,departman,pozisyon,maas from elemanlar"
        cursor.execute(query)
        veriler = cursor.fetchall()
        self.elemanlar.elemanlar.setRowCount(len(veriler))
        self.elemanlar.elemanlar.setColumnCount(9)
        self.elemanlar.elemanlar.setHorizontalHeaderLabels(["Ad", "Soyad", "Telefon","E-Posta","Adres","Eğitim Durumu","Departman","Pozisyon","Maaş"])
        for satir,kayit in enumerate(veriler):
            for sutun, deger in enumerate(kayit):
               self.elemanlar.elemanlar.setItem(satir,sutun,QTableWidgetItem(str(deger)))
        self.elemanlar.elemansayisi.setText(str(len(veriler)))