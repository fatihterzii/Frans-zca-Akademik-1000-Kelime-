from PyQt5 import QtWidgets,QtCore
import sys
import sqlite3
import random

liste=[False,False,False,False,False]
class Pencere_olustur(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Fransizca Akademik 1000 Kelime")
        self.kelime = QtWidgets.QLabel()
        self.kelime.setAlignment(QtCore.Qt.AlignHCenter)
        self.dogru_mu_yanlis_mi=QtWidgets.QLabel()
        self.dogru_mu_yanlis_mi.setAlignment(QtCore.Qt.AlignHCenter)
        self.cevap1 = QtWidgets.QPushButton()
        self.cevap1.clicked.connect(self.cevap1_)
        self.cevap2 = QtWidgets.QPushButton()
        self.cevap2.clicked.connect(self.cevap2_)
        self.cevap3 = QtWidgets.QPushButton()
        self.cevap3.clicked.connect(self.cevap3_)
        self.cevap4 = QtWidgets.QPushButton()
        self.cevap4.clicked.connect(self.cevap4_)
        self.cevap5 = QtWidgets.QPushButton()
        self.cevap5.clicked.connect(self.cevap5_)
        self.kelime_getir = QtWidgets.QPushButton("Kelime Getir")
        self.skor=QtWidgets.QLabel("Skorunuz: 0/100")
        self.skor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.skor.setAlignment(QtCore.Qt.AlignHCenter)
        self.skorum=0
        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.kelime)
        v_box.addStretch()
        v_box.addWidget(self.dogru_mu_yanlis_mi)
        v_box.addStretch()
        v_box.addWidget(self.cevap1)
        v_box.addWidget(self.cevap2)
        v_box.addWidget(self.cevap3)
        v_box.addWidget(self.cevap4)
        v_box.addWidget(self.cevap5)
        v_box.addWidget(self.kelime_getir)
        v_box.addWidget(self.skor)
        self.kelime_getir.clicked.connect(self.kelimeleri_getir)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)

        # self.buton2.clicked.connect(self.gonderme)

        self.show()
    def kelimeleri_getir(self):
        self.dogru_mu_yanlis_mi.setText("")
        self.count=0
        self.random_sayi = random.randint(0, 4)
        turkceler = list()
        fransizcalar = list()
        self.baglanti=sqlite3.connect("kelimeler.db")
        self.cursor=self.baglanti.cursor()
        self.cursor.execute("SELECT * FROM kelimeler ORDER BY RANDOM() LIMIT 5")
        data = self.cursor.fetchall()
        for fransizca, turkce in data:
            fransizcalar.append(fransizca)
            turkceler.append(turkce)
        self.kelime.setText(fransizcalar[self.random_sayi])

        self.cevap1.setText(turkceler[0])
        self.cevap2.setText(turkceler[1])
        self.cevap3.setText(turkceler[2])
        self.cevap4.setText(turkceler[3])
        self.cevap5.setText(turkceler[4])


    def kontrol(self):

        global liste

        if (liste[self.random_sayi]==True):
            self.count+=1
            self.dogru_mu_yanlis_mi.setText("Dogru")
            if self.count==1:
                self.skorum+=1
            self.skor.setText("Skorunuz : {}/100".format(self.skorum))

        else:
            self.count+=1
            self.dogru_mu_yanlis_mi.setText("Tekrar Deneyiniz")

            self.skor.setText("Skorunuz : {}/100".format(self.skorum))

        liste=[False,False,False,False,False]

    def cevap1_(self):
        global liste
        liste[0]=True
        self.kontrol()
    def cevap2_(self):
        global liste
        liste[1]=True
        self.kontrol()
    def cevap3_(self):
        global liste
        liste[2]=True
        self.kontrol()
    def cevap4_(self):
        global liste
        liste[3]=True
        self.kontrol()
    def cevap5_(self):
        global liste
        liste[4]=True
        self.kontrol()



app = QtWidgets.QApplication(sys.argv)
pencere = Pencere_olustur()

sys.exit(app.exec_())
