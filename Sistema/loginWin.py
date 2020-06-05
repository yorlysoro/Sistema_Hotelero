# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginvista.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginWin(object):
    def setupUi(self, loginWin):
        loginWin.setObjectName("loginWin")
        loginWin.resize(366, 131)
        loginWin.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: white;\n"
"    border-radius: 10px;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton#btnSalir {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"\n"
"QMainWindow#loginWin {\n"
"        background-color: #009688;\n"
"}\n"
"QLabel{\n"
"        font-family: \'Roboto\';\n"
"}\n"
"\n"
"QPushButton#btnIngresar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/aceptar-ico.png\");\n"
"}\n"
"QPushButton#btnAcercaDe {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/estrella.png\");\n"
"}\n"
"\n"
"QPushButton#btnIngresar:hover {\n"
"    background-color: green;\n"
"}\n"
"QPushButton#btnAcercaDe:hover {\n"
"    background-color: yellow;\n"
"}\n"
"\n"
"QPushButton#btnSalir:hover {\n"
"    background-color: red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(loginWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.lblUsuario.setObjectName("lblUsuario")
        self.gridLayout.addWidget(self.lblUsuario, 0, 0, 1, 1)
        self.leUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.leUsuario.setObjectName("leUsuario")
        self.gridLayout.addWidget(self.leUsuario, 0, 1, 1, 1)
        self.lblContrasena = QtWidgets.QLabel(self.centralwidget)
        self.lblContrasena.setObjectName("lblContrasena")
        self.gridLayout.addWidget(self.lblContrasena, 1, 0, 1, 1)
        self.leContrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.leContrasena.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.leContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leContrasena.setObjectName("leContrasena")
        self.gridLayout.addWidget(self.leContrasena, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setText("")
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout_2.addWidget(self.btnSalir, 0, 1, 1, 1)
        self.btnIngresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnIngresar.setText("")
        self.btnIngresar.setObjectName("btnIngresar")
        self.gridLayout_2.addWidget(self.btnIngresar, 0, 2, 1, 1)
        self.btnAcercaDe = QtWidgets.QPushButton(self.centralwidget)
        self.btnAcercaDe.setText("")
        self.btnAcercaDe.setObjectName("btnAcercaDe")
        self.gridLayout_2.addWidget(self.btnAcercaDe, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        loginWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWin)
        self.btnSalir.clicked.connect(loginWin.close)
        QtCore.QMetaObject.connectSlotsByName(loginWin)

    def retranslateUi(self, loginWin):
        _translate = QtCore.QCoreApplication.translate
        loginWin.setWindowTitle(_translate("loginWin", "Ingreso al Sistema"))
        self.lblUsuario.setText(_translate("loginWin", "Usuario"))
        self.lblContrasena.setText(_translate("loginWin", "Contraseña"))
        self.btnSalir.setToolTip(_translate("loginWin", "<html><head/><body><p>Cerrar</p></body></html>"))
        self.btnIngresar.setToolTip(_translate("loginWin", "<html><head/><body><p>Ingresar al sistema</p></body></html>"))
        self.btnAcercaDe.setToolTip(_translate("loginWin", "<html><head/><body><p>Acerca del programa</p></body></html>"))

