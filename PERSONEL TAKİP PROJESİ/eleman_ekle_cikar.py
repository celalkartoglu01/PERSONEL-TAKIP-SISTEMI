# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elemaneklecikar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(987, 838)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-30, -50, 1031, 941))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Adsız.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 20, 631, 71))
        self.label_3.setObjectName("label_3")
        self.goruntu = QtWidgets.QGraphicsView(Form)
        self.goruntu.setGeometry(QtCore.QRect(20, 120, 521, 421))
        self.goruntu.setObjectName("goruntu")
        self.fotografcek = QtWidgets.QPushButton(Form)
        self.fotografcek.setGeometry(QtCore.QRect(350, 570, 81, 23))
        self.fotografcek.setObjectName("fotografcek")
        self.ad = QtWidgets.QLineEdit(Form)
        self.ad.setGeometry(QtCore.QRect(790, 100, 151, 31))
        self.ad.setObjectName("ad")
        self.soyad = QtWidgets.QLineEdit(Form)
        self.soyad.setGeometry(QtCore.QRect(790, 170, 151, 31))
        self.soyad.setObjectName("soyad")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 80, 61, 67))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(640, 590, 131, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(690, 650, 81, 51))
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(670, 150, 101, 71))
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(600, 510, 181, 51))
        self.label_11.setObjectName("label_11")
        self.departman = QtWidgets.QLineEdit(Form)
        self.departman.setGeometry(QtCore.QRect(790, 520, 151, 31))
        self.departman.setObjectName("departman")
        self.maas = QtWidgets.QLineEdit(Form)
        self.maas.setGeometry(QtCore.QRect(790, 660, 151, 31))
        self.maas.setObjectName("maas")
        self.pozisyon = QtWidgets.QLineEdit(Form)
        self.pozisyon.setGeometry(QtCore.QRect(790, 590, 151, 31))
        self.pozisyon.setObjectName("pozisyon")
        self.ekle = QtWidgets.QPushButton(Form)
        self.ekle.setGeometry(QtCore.QRect(750, 800, 75, 23))
        self.ekle.setObjectName("ekle")
        self.ad_2 = QtWidgets.QLineEdit(Form)
        self.ad_2.setGeometry(QtCore.QRect(1280, 830, 151, 31))
        self.ad_2.setObjectName("ad_2")
        self.soyad_2 = QtWidgets.QLineEdit(Form)
        self.soyad_2.setGeometry(QtCore.QRect(1280, 900, 151, 31))
        self.soyad_2.setObjectName("soyad_2")
        self.geciktigisure_2 = QtWidgets.QLineEdit(Form)
        self.geciktigisure_2.setGeometry(QtCore.QRect(1280, 1410, 151, 31))
        self.geciktigisure_2.setObjectName("geciktigisure_2")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(1000, 1400, 311, 51))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(1060, 810, 337, 67))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(1020, 1040, 337, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(1010, 1100, 337, 51))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(950, 1240, 337, 51))
        self.label_16.setObjectName("label_16")
        self.cikissaati_2 = QtWidgets.QLineEdit(Form)
        self.cikissaati_2.setGeometry(QtCore.QRect(1280, 1180, 151, 31))
        self.cikissaati_2.setObjectName("cikissaati_2")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(1040, 880, 337, 71))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(1010, 960, 337, 51))
        self.label_18.setObjectName("label_18")
        self.departman_2 = QtWidgets.QLineEdit(Form)
        self.departman_2.setGeometry(QtCore.QRect(1280, 970, 151, 31))
        self.departman_2.setObjectName("departman_2")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(910, 1320, 337, 51))
        self.label_19.setObjectName("label_19")
        self.izingunu_2 = QtWidgets.QLineEdit(Form)
        self.izingunu_2.setGeometry(QtCore.QRect(1280, 1250, 151, 31))
        self.izingunu_2.setObjectName("izingunu_2")
        self.girissaati_2 = QtWidgets.QLineEdit(Form)
        self.girissaati_2.setGeometry(QtCore.QRect(1280, 1110, 151, 31))
        self.girissaati_2.setObjectName("girissaati_2")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(1010, 1170, 337, 51))
        self.label_20.setObjectName("label_20")
        self.pozisyon_2 = QtWidgets.QLineEdit(Form)
        self.pozisyon_2.setGeometry(QtCore.QRect(1280, 1040, 151, 31))
        self.pozisyon_2.setObjectName("pozisyon_2")
        self.degerlendirme_2 = QtWidgets.QLineEdit(Form)
        self.degerlendirme_2.setGeometry(QtCore.QRect(1280, 1330, 151, 31))
        self.degerlendirme_2.setObjectName("degerlendirme_2")
        self.ad_3 = QtWidgets.QLineEdit(Form)
        self.ad_3.setGeometry(QtCore.QRect(1290, 810, 151, 31))
        self.ad_3.setObjectName("ad_3")
        self.soyad_3 = QtWidgets.QLineEdit(Form)
        self.soyad_3.setGeometry(QtCore.QRect(1290, 880, 151, 31))
        self.soyad_3.setObjectName("soyad_3")
        self.geciktigisure_3 = QtWidgets.QLineEdit(Form)
        self.geciktigisure_3.setGeometry(QtCore.QRect(1290, 1390, 151, 31))
        self.geciktigisure_3.setObjectName("geciktigisure_3")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(1010, 1380, 311, 51))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(1070, 790, 337, 67))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(1030, 1020, 337, 31))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(1020, 1080, 337, 51))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(960, 1220, 337, 51))
        self.label_25.setObjectName("label_25")
        self.cikissaati_3 = QtWidgets.QLineEdit(Form)
        self.cikissaati_3.setGeometry(QtCore.QRect(1290, 1160, 151, 31))
        self.cikissaati_3.setObjectName("cikissaati_3")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(1050, 860, 337, 71))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(1020, 940, 337, 51))
        self.label_27.setObjectName("label_27")
        self.departman_3 = QtWidgets.QLineEdit(Form)
        self.departman_3.setGeometry(QtCore.QRect(1290, 950, 151, 31))
        self.departman_3.setObjectName("departman_3")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(920, 1300, 337, 51))
        self.label_28.setObjectName("label_28")
        self.izingunu_3 = QtWidgets.QLineEdit(Form)
        self.izingunu_3.setGeometry(QtCore.QRect(1290, 1230, 151, 31))
        self.izingunu_3.setObjectName("izingunu_3")
        self.girissaati_3 = QtWidgets.QLineEdit(Form)
        self.girissaati_3.setGeometry(QtCore.QRect(1290, 1090, 151, 31))
        self.girissaati_3.setObjectName("girissaati_3")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(1020, 1150, 337, 51))
        self.label_29.setObjectName("label_29")
        self.pozisyon_3 = QtWidgets.QLineEdit(Form)
        self.pozisyon_3.setGeometry(QtCore.QRect(1290, 1020, 151, 31))
        self.pozisyon_3.setObjectName("pozisyon_3")
        self.degerlendirme_3 = QtWidgets.QLineEdit(Form)
        self.degerlendirme_3.setGeometry(QtCore.QRect(1290, 1310, 151, 31))
        self.degerlendirme_3.setObjectName("degerlendirme_3")
        self.cikar = QtWidgets.QPushButton(Form)
        self.cikar.setGeometry(QtCore.QRect(880, 800, 75, 23))
        self.cikar.setObjectName("cikar")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(650, 230, 121, 51))
        self.label_30.setObjectName("label_30")
        self.telefon = QtWidgets.QLineEdit(Form)
        self.telefon.setGeometry(QtCore.QRect(790, 240, 151, 31))
        self.telefon.setObjectName("telefon")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(650, 300, 121, 51))
        self.label_31.setObjectName("label_31")
        self.eposta = QtWidgets.QLineEdit(Form)
        self.eposta.setGeometry(QtCore.QRect(790, 310, 151, 31))
        self.eposta.setObjectName("eposta")
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setGeometry(QtCore.QRect(660, 370, 121, 51))
        self.label_32.setObjectName("label_32")
        self.adres = QtWidgets.QLineEdit(Form)
        self.adres.setGeometry(QtCore.QRect(790, 380, 151, 31))
        self.adres.setObjectName("adres")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(550, 440, 231, 51))
        self.label_33.setObjectName("label_33")
        self.egitimdurumu = QtWidgets.QLineEdit(Form)
        self.egitimdurumu.setGeometry(QtCore.QRect(790, 450, 151, 31))
        self.egitimdurumu.setObjectName("egitimdurumu")
        self.fotografsec = QtWidgets.QPushButton(Form)
        self.fotografsec.setGeometry(QtCore.QRect(450, 570, 81, 23))
        self.fotografsec.setObjectName("fotografsec")
        self.sistemadi = QtWidgets.QLineEdit(Form)
        self.sistemadi.setGeometry(QtCore.QRect(790, 730, 151, 31))
        self.sistemadi.setObjectName("sistemadi")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(620, 710, 141, 71))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">ELEMAN EKLEME-ÇIKARMA</span></p></body></html>"))
        self.fotografcek.setText(_translate("Form", "Fotoğraf Çek"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Ad :</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Pozisyon :</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Maaş:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Soyad :</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Departman :</span></p></body></html>"))
        self.ekle.setText(_translate("Form", "Ekle"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Geciktiği Süre :</span></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Ad :</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Pozisyon :</span></p></body></html>"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Giriş Saati :</span></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Kullandığı İzin Günü :</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Soyad :</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Departman :</span></p></body></html>"))
        self.label_19.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Performans Değerlendirme :</span></p></body></html>"))
        self.label_20.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Çıkış Saati :</span></p></body></html>"))
        self.label_21.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Geciktiği Süre :</span></p></body></html>"))
        self.label_22.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Ad :</span></p></body></html>"))
        self.label_23.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Pozisyon :</span></p></body></html>"))
        self.label_24.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Giriş Saati :</span></p></body></html>"))
        self.label_25.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Kullandığı İzin Günü :</span></p></body></html>"))
        self.label_26.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Soyad :</span></p></body></html>"))
        self.label_27.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Departman :</span></p></body></html>"))
        self.label_28.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Performans Değerlendirme :</span></p></body></html>"))
        self.label_29.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Çıkış Saati :</span></p></body></html>"))
        self.cikar.setText(_translate("Form", "Çıkar"))
        self.label_30.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Telefon :</span></p></body></html>"))
        self.label_31.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">E-posta :</span></p></body></html>"))
        self.label_32.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Adres :</span></p></body></html>"))
        self.label_33.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Eğitim Durumu :</span></p></body></html>"))
        self.fotografsec.setText(_translate("Form", "Fotoğraf Seç"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Sistem Adı :</span></p></body></html>"))
