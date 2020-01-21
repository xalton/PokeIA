# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poke.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from qwt_text_label import QwtTextLabel
import test_rc

class Ui_PokeIA(object):
    def setupUi(self, PokeIA):
        PokeIA.setObjectName("PokeIA")
        PokeIA.resize(800, 600)
        PokeIA.setMinimumSize(QtCore.QSize(800, 600))
        PokeIA.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PokeIA.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PokeIA)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 120, 431, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(470, 110, 281, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Train_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Train_Button.setObjectName("Train_Button")
        self.horizontalLayout.addWidget(self.Train_Button)
        self.Test_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Test_Button.setObjectName("Test_Button")
        self.horizontalLayout.addWidget(self.Test_Button)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(470, 210, 281, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Nameofmodel = QwtTextLabel(self.centralwidget)
        self.Nameofmodel.setGeometry(QtCore.QRect(430, 80, 100, 20))
        self.Nameofmodel.setObjectName("Nameofmodel")
        self.InputName = QtWidgets.QLineEdit(self.centralwidget)
        self.InputName.setGeometry(QtCore.QRect(540, 80, 113, 25))
        self.InputName.setText("")
        self.InputName.setObjectName("InputName")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(660, 80, 89, 25))
        self.OK.setObjectName("OK")
        self.TextLabel = QwtTextLabel(self.centralwidget)
        self.TextLabel.setGeometry(QtCore.QRect(170, 10, 451, 31))
        self.TextLabel.setProperty("plainText", "")
        self.TextLabel.setObjectName("TextLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setMinimumSize(QtCore.QSize(800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("background-image: url(:/newPrefix/poke_background.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.gridLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.progressBar.raise_()
        self.InputName.raise_()
        self.OK.raise_()
        self.TextLabel.raise_()
        self.Nameofmodel.raise_()
        PokeIA.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PokeIA)
        self.statusbar.setObjectName("statusbar")
        PokeIA.setStatusBar(self.statusbar)

        self.retranslateUi(PokeIA)
        QtCore.QMetaObject.connectSlotsByName(PokeIA)

    def retranslateUi(self, PokeIA):
        _translate = QtCore.QCoreApplication.translate
        PokeIA.setWindowTitle(_translate("PokeIA", "PokeIA"))
        self.Train_Button.setText(_translate("PokeIA", "Train"))
        self.Test_Button.setText(_translate("PokeIA", "Test"))
        self.Nameofmodel.setProperty("plainText", _translate("PokeIA", "Name"))
        self.OK.setText(_translate("PokeIA", "OK"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PokeIA = QtWidgets.QMainWindow()
    ui = Ui_PokeIA()
    ui.setupUi(PokeIA)
    PokeIA.show()
    sys.exit(app.exec_())
