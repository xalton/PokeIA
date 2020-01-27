from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import pokeGUI

class PokeApp(QtWidgets.QMainWindow, pokeGUI.Ui_PokeIA):
    def __init__(self, parent=None):
        super(PokeApp, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = PokeApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
