# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poke.ui'
#
# Design created with: PyQt5 UI code generator 5.13.0
#

import re
import sys
import time
import test_rc
import tensorflow
import functions_poke
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from tensorflow.keras.callbacks import TensorBoard


class Ui_PokeIA(object):

    def __init__(self):
        self.name = "vide"
        self.setupUi(PokeIA)

    def setupUi(self, PokeIA):

        ########################
        ##### CENTRAL VIEW #####
        ########################

        PokeIA.setObjectName("PokeIA")
        PokeIA.resize(800, 600)
        PokeIA.setMinimumSize(QtCore.QSize(800, 600))
        PokeIA.setMaximumSize(QtCore.QSize(800, 600))
        PokeIA.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/pokeball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PokeIA.setWindowIcon(icon)
        self.CentralView = QtWidgets.QWidget(PokeIA)
        self.CentralView.setObjectName("CentralView")
        self.Background = QtWidgets.QLabel(self.CentralView)
        self.Background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.Background.setMinimumSize(QtCore.QSize(800, 600))
        self.Background.setMaximumSize(QtCore.QSize(800, 600))
        self.Background.setStyleSheet("background-image: url(:/newPrefix/poke_background.png);")
        self.Background.setObjectName("Background")
        self.DexScreen = QtWidgets.QLabel(self.CentralView)
        self.DexScreen.setGeometry(QtCore.QRect(0, 80, 491, 401))
        self.DexScreen.setStyleSheet("image: url(:/newPrefix/dexxx.png);")
        self.DexScreen.setObjectName("DexScreen")
        self.layoutWidget2 = QtWidgets.QWidget(self.CentralView)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 10, 591, 67))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.TitleLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.TitleLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleLayout.setObjectName("TitleLayout")
        self.Logo1 = QtWidgets.QLabel(self.layoutWidget2)
        self.Logo1.setStyleSheet("image: url(:/newPrefix/pokeball.png);")
        self.Logo1.setText("")
        self.Logo1.setObjectName("Logo1")
        self.TitleLayout.addWidget(self.Logo1)
        self.Title = QtWidgets.QLabel(self.layoutWidget2)
        self.Title.setStyleSheet("font: 75 48pt \"Ubuntu Mnono\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-color: rgb(0, 0, 0);")
        self.Title.setObjectName("Title")
        self.TitleLayout.addWidget(self.Title)
        self.Logo2 = QtWidgets.QLabel(self.layoutWidget2)
        self.Logo2.setStyleSheet("image: url(:/newPrefix/pokeball.png);")
        self.Logo2.setObjectName("Logo2")
        self.TitleLayout.addWidget(self.Logo2)
        ###### IMAGE POKE ######

        self.ImagePoke = QtWidgets.QLabel(self.CentralView)
        self.ImagePoke.setGeometry(QtCore.QRect(11, 185, 213, 213))
        self.ImagePoke.setObjectName("ImagePoke_")
        self.ImagePoke.setContentsMargins(4, 4, 1, 1)
        self.ImagePoke.setScaledContents(True)
        #self.TitleLayout.addWidget(self.Logo2)
        self.ImagePoke.setObjectName("ImagePoke")

        ###### SPEC POKE ######

        self.PokeSpec = QtWidgets.QLabel(self.CentralView)
        self.PokeSpec.setGeometry(QtCore.QRect(280, 190, 191, 241))
        self.PokeSpec.setObjectName("PokeSpec")
        self.PokeSpec.setStyleSheet("Background-color: rgb(255,255,255);")
        ###### LINK Tensorboard ######

        self.TensorboardButton = QtWidgets.QCommandLinkButton(self.CentralView)
        self.TensorboardButton.setGeometry(QtCore.QRect(610, 540, 177, 41))
        self.TensorboardButton.setStyleSheet("font: 75 15pt \"Ubuntu Mono\";\n"
        "color: rgb(255, 255, 255);\n"
        "border-color: rgb(0, 0, 0);\n"
        "background-color: rgb(170, 170, 255);\n"
        "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/tensorflow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TensorboardButton.setIcon(icon1)
        self.TensorboardButton.setObjectName("TensorboardButton")

        ########################
        #### ACTION LAYOUT  ####
        ########################

        self.layoutWidget = QtWidgets.QWidget(self.CentralView)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 450, 321, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.ActionLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.ActionLayout.setContentsMargins(0, 0, 0, 0)
        self.ActionLayout.setObjectName("ActionLayout")
        self.TrainButton = QtWidgets.QPushButton(self.layoutWidget)
        self.TrainButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.TrainButton.setObjectName("TrainButton")
        self.TrainButton.clicked.connect(self.TrainButtonClick)
        self.ActionLayout.addWidget(self.TrainButton, 0, 1, 1, 1)
        self.TestButton = QtWidgets.QPushButton(self.layoutWidget)
        self.TestButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.TestButton.setObjectName("TestButton")
        self.TestButton.clicked.connect(self.TestButtonClick)
        self.ActionLayout.addWidget(self.TestButton, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadImage)
        self.ActionLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.ProgressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.ProgressBar.setStyleSheet("background-color: rgb(70, 63, 88);\n"
        "font: 75 11pt \"Ubuntu Mono\";")
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.ActionLayout.addWidget(self.ProgressBar, 1, 0, 1, 3)

        ########################
        ## MODEL NAME LAYOUT  ##
        ########################

        self.layoutWidget1 = QtWidgets.QWidget(self.CentralView)
        self.layoutWidget1.setGeometry(QtCore.QRect(510, 150, 251, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.ModelNameLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.ModelNameLayout.setContentsMargins(0, 0, 0, 0)
        self.ModelNameLayout.setObjectName("ModelNameLayout")
        self.ModelName = QtWidgets.QLabel(self.layoutWidget1)
        self.ModelName.setStyleSheet("color: rgb(255, 255, 255);\n"
        "border-color: rgb(0, 0, 0);")
        self.ModelName.setObjectName("ModelName")
        self.ModelNameLayout.addWidget(self.ModelName)
        self.InputName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.InputName.setText("")
        self.InputName.setObjectName("InputName")
        self.ModelNameLayout.addWidget(self.InputName)
        self.OKButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.OKButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.OKButton.setObjectName("OKButton")
        self.OKButton.clicked.connect(self.GetModelName)
        self.ModelNameLayout.addWidget(self.OKButton)

        ##################
        ## RAISE FORMS  ##
        ##################

        self.Background.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget1.raise_()
        self.layoutWidget2.raise_()
        self.TensorboardButton.raise_()
        self.DexScreen.raise_()
        self.PokeSpec.raise_()
        self.ImagePoke.raise_()
        PokeIA.setCentralWidget(self.CentralView)


        self.retranslateUi(PokeIA)
        QtCore.QMetaObject.connectSlotsByName(PokeIA)

    def GetModelName(self):
        self.name = self.InputName.text()
        print("The name of your model is ", self.name)
        return self.name

    def LoadImage(self):
        l = QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"/home/machinelearning/Documents/PokeIA/Dataset")
        self.image_path = l[0]
        print('Your image is loaded:', self.image_path)
        self.ImagePoke.setPixmap(QtGui.QPixmap(self.image_path))

        return self.image_path

    def TrainButtonClick(self):
        functions_poke.TrainModel(self.name)
        #self.calc = External()
        #self.calc.start()
        #p1 = Process(target=functions_poke.TrainModel(self.name))
        #p1.start()
        #p2 = Process(target=self.calc.countChanged.connect(self.onCountChanged))
        #p2.start()
        #p1.join()
        #p2.join()

    def TestButtonClick(self):
         self.label,self.flag = functions_poke.Predic(self.image_path,self.name)
         print("Your image is :", self.label)
         if self.flag == True:
             path_spec = 'Images/Spec/spec_'+ self.label +'.png'
             self.PokeSpec.setPixmap(QtGui.QPixmap(path_spec))

    def onCountChanged(self,value):
        self.ProgressBar.setValue(value)

    def retranslateUi(self, PokeIA):
        _translate = QtCore.QCoreApplication.translate
        PokeIA.setWindowTitle(_translate("PokeIA", "PokeIA"))
        self.TensorboardButton.setText(_translate("PokeIA", "Tensorboard"))
        self.TrainButton.setText(_translate("PokeIA", "Train"))
        self.TestButton.setText(_translate("PokeIA", "Test"))
        self.pushButton.setText(_translate("PokeIA", "Browse"))
        self.ModelName.setText(_translate("PokeIA", "Name:"))
        self.OKButton.setText(_translate("PokeIA", "OK"))
        self.Title.setText(_translate("PokeIA", "Poke IA app"))


TIME_LIMIT = 100
class External(QThread):#,Ui_PokeIA):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += 1
            #time.sleep(1)
            self.countChanged.emit(count)
            #--> Problème avec cette logique
            #Passe de 1% à 100% directement et n'incrémente pas
            #pendant que TrainModel s'execute.
            #--> Solution? jouer sur le temps d'execution du TrainModel pour
            #update la progress bar


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PokeIA = QtWidgets.QMainWindow()
    ui = Ui_PokeIA()
    ui.setupUi(PokeIA)
    PokeIA.show()
    sys.exit(app.exec_())
