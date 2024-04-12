from PyQt5 import uic

with open("giris_.py","w",encoding="utf-8") as fout:
    uic.compileUi("giris_yap.ui", fout)


with open("ana_sayfa.py","w",encoding="utf-8") as fout:
    uic.compileUi("anasayfa.ui", fout)



with open("calisma_ozetleri.py","w",encoding="utf-8") as fout:
    uic.compileUi("calismaozetleri.ui", fout)



with open("elemanlar_.py","w",encoding="utf-8") as fout:
    uic.compileUi("elemanlar.ui", fout)



with open("giris_cikis.py","w",encoding="utf-8") as fout:
    uic.compileUi("giriscikis.ui", fout)


with open("profil_.py","w",encoding="utf-8") as fout:
    uic.compileUi("profil.ui", fout)


with open("eleman_ekle_cikar.py","w",encoding="utf-8") as fout:
    uic.compileUi("elemaneklecikar.ui", fout)