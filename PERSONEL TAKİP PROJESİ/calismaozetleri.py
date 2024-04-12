from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from calisma_ozetleri import Ui_Form
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt
import face_recognition
import os
import cv2
import mysql.connector


con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'pts')
cursor = con.cursor()





class CalismaOzetleri(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.calismaozetleri = Ui_Form()
        self.calismaozetleri.setupUi(self)
        self.calismaozetleri.calisansec.clicked.connect(self.CalisanSec)
        self.known_face_encodings = []
        self.known_face_names = []
        self.folder_path = "calisanlar"
        self.scene = QtWidgets.QGraphicsScene()  
        self.calismaozetleri.goruntu.setScene(self.scene)
        self.file_path = None
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





    def CalisanSec(self):
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
                    query = "select ad,soyad,departman,pozisyon,kullanilanizin,degerlendirme,geciktiğisure from calismaozetleri where sistemadi = %s"
                    cursor.execute(query,(name,))
                    result = cursor.fetchone()
                    ad,soyad,departman,pozisyon,kullanilanizin,degerlendirme,geciktiğisure = result
                    self.calismaozetleri.ad.setText(ad)
                    self.calismaozetleri.soyad.setText(soyad)
                    self.calismaozetleri.departman.setText(departman)
                    self.calismaozetleri.pozisyon.setText(pozisyon)
                    self.calismaozetleri.izingunu.setText(str(kullanilanizin))
                    self.calismaozetleri.degerlendirme.setText(degerlendirme)
                    self.calismaozetleri.geciktigisure.setText(str(geciktiğisure))
                else:
                    cv2.rectangle(img, (topLeftX, topLeftY), (botRightX, botRightY), (0,0,255), 2)
                    cv2.putText(img, name, (topLeftX, topLeftY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    self.calismaozetleri.ad.clear()
                    self.calismaozetleri.soyad.clear()
                    self.calismaozetleri.departman.clear()
                    self.calismaozetleri.pozisyon.clear()
                    self.calismaozetleri.izingunu.clear()
                    self.calismaozetleri.degerlendirme.clear()
                    self.calismaozetleri.geciktigisure.clear()
                
              
               
            

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, _ = img_rgb.shape
            bytes_per_line = width * 3  
            q_img = QPixmap(QImage(img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888))

            view_rect = self.calismaozetleri.goruntu.rect()
            scaled_pixmap = q_img.scaled(view_rect.size(), aspectRatioMode=Qt.KeepAspectRatio)
            self.scene.clear()  
            self.scene.addPixmap(scaled_pixmap)
            self.calismaozetleri.goruntu.setScene(self.scene)
            self.calismaozetleri.goruntu.horizontalScrollBar().setVisible(False)
            self.calismaozetleri.goruntu.verticalScrollBar().setVisible(False)