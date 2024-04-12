from PyQt5.QtWidgets import *
from eleman_ekle_cikar import Ui_Form
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer,Qt
import cv2
import mysql.connector
import face_recognition
import os
import numpy as np


con = mysql.connector.connect(user='root', password='', host='localhost', database='pts')
cursor = con.cursor()





class ElemanEkleCikar(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.elemaneklecikar = Ui_Form()
        self.elemaneklecikar.setupUi(self)
        self.elemaneklecikar.fotografcek.clicked.connect(self.FotografCek)
        self.elemaneklecikar.fotografsec.clicked.connect(self.FotografSec)
        self.elemaneklecikar.ekle.clicked.connect(self.Ekle)
        self.scene = QGraphicsScene(self)
        self.elemaneklecikar.goruntu.setScene(self.scene)
        self.timer = QTimer(self)
        self.known_face_encodings = []
        self.known_face_names = []
        self.folder_path = "calisanlar"
        self.file_path = None
        self.current_frame = None
        self.update_known_faces()
    

    def update_known_faces(self):
        self.known_face_encodings = []
        self.known_face_names = []
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
                image_path = os.path.join(self.folder_path, file_name)
                image = face_recognition.load_image_file(image_path)
                encoding = face_recognition.face_encodings(image)[0]
                self.known_face_encodings.append(encoding)
                self.known_face_names.append(os.path.splitext(file_name)[0])

    



    def FotografCek(self):
    
        if self.timer.isActive():
            self.timer.stop()
            self.camera.release()
            return
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            QMessageBox.critical(self, "Hata", "Kamera açılamadı.")
            return
        
        self.timer.timeout.connect(self.display_frame)
        self.timer.start(1000 // 30)  

    def display_frame(self):
        ret, frame = self.camera.read()
        frame = cv2.flip(frame,1)

        

        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            q_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_img)
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.current_frame = rgb_frame.copy()


    def Ekle(self):
        ad = self.elemaneklecikar.ad.text()
        soyad = self.elemaneklecikar.soyad.text()
        telefon = self.elemaneklecikar.telefon.text()
        eposta = self.elemaneklecikar.eposta.text()
        adres = self.elemaneklecikar.adres.text()
        egitimdurumu = self.elemaneklecikar.egitimdurumu.text()
        departman = self.elemaneklecikar.departman.text()
        pozisyon = self.elemaneklecikar.pozisyon.text()
        maas = self.elemaneklecikar.maas.text()
        sistemadi = self.elemaneklecikar.sistemadi.text()
    
        file_path = os.path.join(self.folder_path, f"{sistemadi}.jpg")
        if os.path.exists(file_path):
            QMessageBox.warning(self, "Hata", "Bu dosya adı zaten mevcut. Lütfen farklı bir dosya adı girin.")
            return
        success = cv2.imwrite(file_path, self.current_frame[:, :, ::-1])
        if success:
            query = "INSERT INTO elemanlar (ad, soyad, telefon, eposta, adres, egitimdurumu, departman, pozisyon, maas, sistemadi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (ad, soyad, telefon, eposta, adres, egitimdurumu, departman, pozisyon, maas, sistemadi)
            cursor.execute(query, values)
            con.commit()
            cursor.close()
            QMessageBox.information(self, "Başarılı", "Eleman Eklendi !")
            self.elemaneklecikar.ad.clear()
            self.elemaneklecikar.soyad.clear()
            self.elemaneklecikar.telefon.clear()
            self.elemaneklecikar.eposta.clear()
            self.elemaneklecikar.adres.clear()
            self.elemaneklecikar.egitimdurumu.clear()
            self.elemaneklecikar.departman.clear()
            self.elemaneklecikar.pozisyon.clear()
            self.elemaneklecikar.maas.clear()
            self.elemaneklecikar.sistemadi.clear()
            self.scene.clear()
        else:
            QMessageBox.warning(self, "Hata", "Görüntü kaydedilemedi.")



    def recognize_faces_in_image(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if not face_encodings:
            QMessageBox.warning(self, "Uyarı", "Görüntüde yüz bulunamadı.")
            return
        new_face_encoding = face_encodings[0]
        new_face_name = os.path.splitext(os.path.basename(image_path))[0]
        self.known_face_encodings.append(new_face_encoding)
        self.known_face_names.append(new_face_name)
        self.update_known_faces()
   





    def FotografSec(self):
        self.file_path,_ = QFileDialog.getOpenFileName(self, "Fotoğraf Seç", "", "*.png *.jpg *.jpeg")

        if self.file_path:
            dosyayolu = self.file_path[56:]
            img = cv2.imread(dosyayolu)

            face_locations = face_recognition.face_locations(img)
            face_encodings = face_recognition.face_encodings(img,face_locations)

            for face_encoding, (topLeftY, botRightX, botRightY, topLeftX) in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Bilinmeyen Yuz"
                if any(matches):
                    matched_index = matches.index(True)
                    name = self.known_face_names[matched_index]
                    query = "select ad,soyad,telefon,eposta,adres,egitimdurumu,departman,pozisyon,maas,sistemadi from elemanlar where sistemadi = %s"
                    cursor.execute(query,(name,))
                    result = cursor.fetchone()
                    ad,soyad,telefon,eposta,adres,egitimdurumu,departman,pozisyon,maas,sistemadi = result
                    self.elemaneklecikar.ad.setText(ad)
                    self.elemaneklecikar.soyad.setText(soyad)
                    self.elemaneklecikar.telefon.setText(telefon)
                    self.elemaneklecikar.eposta.setText(eposta)
                    self.elemaneklecikar.adres.setText(adres)
                    self.elemaneklecikar.egitimdurumu.setText(egitimdurumu)
                    self.elemaneklecikar.departman.setText(departman)
                    self.elemaneklecikar.pozisyon.setText(pozisyon)
                    self.elemaneklecikar.maas.setText(maas)
                    self.elemaneklecikar.sistemadi.setText(sistemadi)
                    
                else:
                    cv2.rectangle(img, (topLeftX, topLeftY), (botRightX, botRightY), (0,0,255), 2)
                    cv2.putText(img, name, (topLeftX, topLeftY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    self.elemaneklecikar.ad.clear()
                    self.elemaneklecikar.soyad.clear()
                    self.elemaneklecikar.telefon.clear()
                    self.elemaneklecikar.eposta.clear()
                    self.elemaneklecikar.adres.clear()
                    self.elemaneklecikar.egitimdurumu.clear()
                    self.elemaneklecikar.departman.clear()
                    self.elemaneklecikar.pozisyon.clear()
                    self.elemaneklecikar.maas.clear()
                
              
               
            

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, _ = img_rgb.shape
            bytes_per_line = width * 3  
            q_img = QPixmap(QImage(img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888))

            view_rect = self.elemaneklecikar.goruntu.rect()
            scaled_pixmap = q_img.scaled(view_rect.size(), aspectRatioMode=Qt.KeepAspectRatio)
            self.scene.clear()  
            self.scene.addPixmap(scaled_pixmap)
            self.elemaneklecikar.goruntu.setScene(self.scene)
            self.elemaneklecikar.goruntu.horizontalScrollBar().setVisible(False)
            self.elemaneklecikar.goruntu.verticalScrollBar().setVisible(False)

    
  