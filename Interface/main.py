# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poke.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in thisfile will be lost!

import sys
from qwt import QwtText
from PyQt5 import QtWidgets
from poke import Ui_MainWindow

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
