# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercadevista.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_acercaDeWin(object):
    def setupUi(self, acercaDeWin):
        acercaDeWin.setObjectName("acercaDeWin")
        acercaDeWin.setWindowModality(QtCore.Qt.WindowModal)
        acercaDeWin.resize(292, 178)
        acercaDeWin.setMaximumSize(QtCore.QSize(16777213, 16777215))
        acercaDeWin.setStyleSheet("QLabel {\n"
"    font-family: \'Roboto\';\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton#btnCerrar {\n"
"    border-style: inset;\n"
"    border-radius:15px;\n"
"    border-size: 15px;\n"
"    image: url(\"../Iconos/aceptar-ico.png\");\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"QPushButton#btnCerrar:hover {\n"
"    background-color: green;\n"
"}\n"
"\n"
"QDialog {\n"
"    background-color: #009688\n"
"}")
        acercaDeWin.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(acercaDeWin)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.lblTitulo = QtWidgets.QLabel(acercaDeWin)
        self.lblTitulo.setObjectName("lblTitulo")
        self.gridLayout.addWidget(self.lblTitulo, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(acercaDeWin)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(acercaDeWin)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(acercaDeWin)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(acercaDeWin)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 1)
        self.btnCerrar = QtWidgets.QPushButton(acercaDeWin)
        self.btnCerrar.setText("")
        self.btnCerrar.setObjectName("btnCerrar")
        self.gridLayout_4.addWidget(self.btnCerrar, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.retranslateUi(acercaDeWin)
        self.btnCerrar.clicked.connect(acercaDeWin.close)
        QtCore.QMetaObject.connectSlotsByName(acercaDeWin)

    def retranslateUi(self, acercaDeWin):
        _translate = QtCore.QCoreApplication.translate
        acercaDeWin.setWindowTitle(_translate("acercaDeWin", "acercaDe"))
        self.lblTitulo.setText(_translate("acercaDeWin", "Administrador de Hotel"))
        self.label.setText(_translate("acercaDeWin", "Integrantes:"))
        self.label_2.setText(_translate("acercaDeWin", "Yorlys Orpopeza"))
        self.label_3.setText(_translate("acercaDeWin", "Jerrinson Garcia"))
        self.label_4.setText(_translate("acercaDeWin", "Rosmary Lopez"))

