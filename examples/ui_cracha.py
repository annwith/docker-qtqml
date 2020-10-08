# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cracha.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Cracha(object):
    def setupUi(self, Cracha):
        Cracha.setObjectName("Cracha")
        Cracha.resize(250, 400)
        self.label = QtWidgets.QLabel(Cracha)
        self.label.setGeometry(QtCore.QRect(0, 0, 250, 400))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/examples/Imagens/modelo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Cracha)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 130, 130))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/examples/Imagens/pessoa.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Cracha)
        self.label_3.setGeometry(QtCore.QRect(40, 240, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Cracha)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 101, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Cracha)
        QtCore.QMetaObject.connectSlotsByName(Cracha)

    def retranslateUi(self, Cracha):
        _translate = QtCore.QCoreApplication.translate
        Cracha.setWindowTitle(_translate("Cracha", "Cracha"))
        self.label_3.setText(_translate("Cracha", "Francisco Silva"))
        self.label_4.setText(_translate("Cracha", "Programador"))

