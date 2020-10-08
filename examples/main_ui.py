import sys
from PyQt5 import QtWidgets
#from PySide2.QtWidgets import QApplication, QWidget
from ui_cracha import Ui_Cracha

class Cracha(Ui_Cracha, QtWidgets.QWidget):     
    def __init__(self):
        super(Cracha, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #Cracha = QtWidgets.QWidget()
    #ui = Ui_Cracha()
    #ui.setupUi(Cracha)
    cracha = Cracha()
    cracha.show()
    sys.exit(app.exec_())