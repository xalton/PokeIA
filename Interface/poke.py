# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poke.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PokeIA(object):
    def setupUi(self, PokeIA):
        PokeIA.setObjectName("PokeIA")
        PokeIA.resize(800, 600)
        PokeIA.setMinimumSize(QtCore.QSize(800, 600))
        PokeIA.setMaximumSize(QtCore.QSize(800, 600))
        PokeIA.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pokeball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PokeIA.setWindowIcon(icon)
        self.CentralView = QtWidgets.QWidget(PokeIA)
        self.CentralView.setObjectName("CentralView")
        self.Title = QwtTextLabel(self.CentralView)
        self.Title.setGeometry(QtCore.QRect(170, 10, 451, 31))
        self.Title.setPlainText("")
        self.Title.setObjectName("Title")
        self.Background = QtWidgets.QLabel(self.CentralView)
        self.Background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.Background.setMinimumSize(QtCore.QSize(800, 600))
        self.Background.setMaximumSize(QtCore.QSize(800, 600))
        self.Background.setStyleSheet("background-image: url(:/newPrefix/poke_background.png);")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.CentralView)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 150, 201, 211))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.ImagePoke = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.ImagePoke.setContentsMargins(0, 0, 0, 0)
        self.ImagePoke.setObjectName("ImagePoke")
        self.Spec = QtWidgets.QTableWidget(self.CentralView)
        self.Spec.setGeometry(QtCore.QRect(280, 150, 191, 241))
        self.Spec.setObjectName("Spec")
        self.Spec.setColumnCount(0)
        self.Spec.setRowCount(0)
        self.TensorboardButton = QtWidgets.QCommandLinkButton(self.CentralView)
        self.TensorboardButton.setGeometry(QtCore.QRect(610, 540, 177, 41))
        self.TensorboardButton.setStyleSheet("font: 25 italic 11pt \"Ubuntu\"\n"
"rgb(115, 210, 22)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/tensorflow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TensorboardButton.setIcon(icon1)
        self.TensorboardButton.setObjectName("TensorboardButton")
        self.layoutWidget = QtWidgets.QWidget(self.CentralView)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 430, 321, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Actions = QtWidgets.QGridLayout(self.layoutWidget)
        self.Actions.setContentsMargins(0, 0, 0, 0)
        self.Actions.setObjectName("Actions")
        self.TrainButton = QtWidgets.QPushButton(self.layoutWidget)
        self.TrainButton.setObjectName("TrainButton")
        self.Actions.addWidget(self.TrainButton, 0, 1, 1, 1)
        self.TestButton = QtWidgets.QPushButton(self.layoutWidget)
        self.TestButton.setObjectName("TestButton")
        self.Actions.addWidget(self.TestButton, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.Actions.addWidget(self.pushButton, 0, 0, 1, 1)
        self.ProgressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.Actions.addWidget(self.ProgressBar, 1, 0, 1, 3)
        self.layoutWidget1 = QtWidgets.QWidget(self.CentralView)
        self.layoutWidget1.setGeometry(QtCore.QRect(510, 150, 251, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.ModelName = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.ModelName.setContentsMargins(0, 0, 0, 0)
        self.ModelName.setObjectName("ModelName")
        self.Nameofmodel = QwtTextLabel(self.layoutWidget1)
        self.Nameofmodel.setObjectName("Nameofmodel")
        self.ModelName.addWidget(self.Nameofmodel)
        self.InputName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.InputName.setText("")
        self.InputName.setObjectName("InputName")
        self.ModelName.addWidget(self.InputName)
        self.OKButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.OKButton.setObjectName("OKButton")
        self.ModelName.addWidget(self.OKButton)
        self.label = QtWidgets.QLabel(self.CentralView)
        self.label.setGeometry(QtCore.QRect(0, 40, 491, 401))
        self.label.setStyleSheet("image: url(:/newPrefix/dexxx.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Background.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.Title.raise_()
        self.gridLayoutWidget_2.raise_()
        self.TensorboardButton.raise_()
        self.label.raise_()
        self.Spec.raise_()
        PokeIA.setCentralWidget(self.CentralView)

        self.retranslateUi(PokeIA)
        QtCore.QMetaObject.connectSlotsByName(PokeIA)

    def retranslateUi(self, PokeIA):
        _translate = QtCore.QCoreApplication.translate
        PokeIA.setWindowTitle(_translate("PokeIA", "PokeIA"))
        self.TensorboardButton.setText(_translate("PokeIA", "Tensorboard"))
        self.TrainButton.setText(_translate("PokeIA", "Train"))
        self.TestButton.setText(_translate("PokeIA", "Test"))
        self.pushButton.setText(_translate("PokeIA", "Load"))
        self.Nameofmodel.setPlainText(_translate("PokeIA", "Name"))
        self.OKButton.setText(_translate("PokeIA", "OK"))
from qwt_text_label import QwtTextLabel
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PokeIA = QtWidgets.QMainWindow()
    ui = Ui_PokeIA()
    ui.setupUi(PokeIA)
    PokeIA.show()
    sys.exit(app.exec_())
