from PyQt5.QtWidgets import *
from ana_sayfa import Ui_Form
from profil import Profil
from calismaozetleri import CalismaOzetleri
from giriscikis import GirisCikis
from elemaneklecikar import ElemanEkleCikar
from elemanlar import Elemanlar


class AnaSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.anasayfa = Ui_Form()
        self.anasayfa.setupUi(self)
        self.profil = Profil()
        self.elemaneklecikar = ElemanEkleCikar()
        self.giriscikis = GirisCikis()
        self.elemanlar = Elemanlar()
        self.calismaozetleri = CalismaOzetleri()
        self.anasayfa.profil.clicked.connect(self.Profil)
        self.anasayfa.calismaozetleri.clicked.connect(self.CalismaOzetleri)
        self.anasayfa.giriscikis.clicked.connect(self.GirisCikis)
        self.anasayfa.elemaneklecikar.clicked.connect(self.EkleCikar)
        self.anasayfa.elemanlar.clicked.connect(self.Elemanlar)
        self.anasayfa.sistemdencik.clicked.connect(self.SistemdenCik)
    



    def Profil(self):
        self.profil.show()
    

    def CalismaOzetleri(self):
        self.calismaozetleri.show()
    

    def GirisCikis(self):
        self.giriscikis.show()
    

    def EkleCikar(self):
        self.elemaneklecikar.show()
    

    def Elemanlar(self):
        self.elemanlar.show()
    

    def SistemdenCik(self):
        self.hide()
       