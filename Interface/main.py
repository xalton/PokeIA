from PyQt5 import QtCore, QtGui, QtWidgets, uic

class MyWindow():
    def __init__(self):
        super(MyWindow,self).__init__()
        uic.loadUi('poke.ui',self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
