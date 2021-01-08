#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Conversor.py
#
# Copyright 2021 JaimeJGJG
#
# Ultimo update:08/01/2021
# 
# PARA TUDO FUNCIONAR INSTALE:
# sudo apt-get install python3-pip
# sudo apt-get install python3-pyqt5
# pip3 install -U pip
# pip3 install SpeechRecognition
# pip3 install gTTS
# pip3 install python-vlc 

from gtts import gTTS
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox
import speech_recognition as sr
import sys
import vlc

r = sr.Recognizer()

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.wall = QLabel(self)
        self.wall.move(0,0)
        self.wall.setPixmap(QtGui.QPixmap('Wall.png'))
        self.wall.resize(300,300)
        
        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(25,45)
        self.caixa_texto.resize(250,50)
        self.caixa_texto.setStyleSheet('QLineEdit {background-color:black;color:white}')
        
        self.label_texto = QLabel(self)
        self.label_texto.setText("Digite algo ou fale no microfone")
        self.label_texto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_texto.move(45,5)
        self.label_texto.setStyleSheet('QLabel {font-size:14px;color:#00FF00}')
        self.label_texto.resize(210,30)
        
        botao_caixa = QPushButton("Converter",self)
        botao_caixa.move(110,110)
        botao_caixa.resize(80,30)
        botao_caixa.setStyleSheet('QPushButton {background-color:blue;font:bold;font-size:12px}')
        botao_caixa.clicked.connect(self.converter_texto)
        
        self.label_mic = QLabel(self)
        self.label_mic.setText("")
        self.label_mic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mic.move(0,140)
        self.label_mic.setStyleSheet('QLabel {font-size:12px;color:white}')
        self.label_mic.resize(300,50)


        botao_mic = QPushButton("",self)
        botao_mic.move(100,190)
        botao_mic.resize(100,100)
        botao_mic.setStyleSheet("background-image : url(mic.png);border-radius: 15px")
        botao_mic.clicked.connect(self.microfone)
        
        self.label_nv = QLabel(self)
        self.label_nv.setText("")
        self.label_nv.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nv.move(0,275)
        self.label_nv.setStyleSheet('QLabel {font-size:10px;color:white}')
        self.label_nv.resize(300,30)

        
        self.CarregarJanela()
		
    def CarregarJanela(self):
        self.setGeometry(50,50,300,300)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(300, 30)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Conversor TTS ou STS")
        self.show()
         
    def microfone(self):
        with sr.Microphone() as s:
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
            speech = r.recognize_google(audio, language= "pt-BR")
            print('VOÇÊ DISSE: ', speech)
            print("Sua frase foi convertida e salva em .mp3")
            self.label_mic.setText("VOÇÊ DISSE:\n" +speech)
            tts = gTTS(text=speech, lang='pt-br')
            tts.save("convertido.mp3")
            p = vlc.MediaPlayer("convertido.mp3")
            p.play()
            self.label_nv.setText("CLIQUE PARA FALAR NOVAMENTE")
            QMessageBox.about(self,"Sucesso","SUA FRASE:\n" +speech +"\nFOI CONVERTIDA E SALVA EM .mp3")
        
    def converter_texto(self):
        conteudo = self.caixa_texto.text()
        tts = gTTS(text=conteudo, lang='pt-br')
        tts.save("convertido.mp3")
        print("A frase: " +conteudo +" foi convertida e salva em .mp3")
        p = vlc.MediaPlayer("convertido.mp3")
        p.play()
        QMessageBox.about(self,"Sucesso","SUA FRASE:\n" +conteudo +"\nFOI CONVERTIDA E SALVA EM .mp3")

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
