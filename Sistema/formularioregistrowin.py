# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularioregistrowin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormularioRegistroWin(object):
    def setupUi(self, FormularioRegistroWin):
        FormularioRegistroWin.setObjectName("FormularioRegistroWin")
        FormularioRegistroWin.resize(385, 491)
        FormularioRegistroWin.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    border-style: ouset;\n"
"    border-width: 2px;\n"
"    border-color: white;\n"
"    border-radius: 10px;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QTextEdit {\n"
"        background-color: white;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"    border-radius: 10px;\n"
"    font: bold 10px;\n"
"    min-width: 10em;\n"
"    padding:2px;\n"
"}\n"
"QMainWindow {\n"
"        background-color: #009688;\n"
"}\n"
"QPushButton#btnRegistrar {\n"
"        border-radius:15px;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 25px;\n"
"        image: url(\"../Iconos/aceptar-ico.png\")\n"
"}\n"
"QPushButton#btnRegistrar:hover {\n"
"    background-color: #0DD706;\n"
"}\n"
"QPushButton#btnSalir {\n"
"    border-radius: 15px;\n"
"    font-family: \'Roboto\';\n"
"    font-size:25px;\n"
"    image: url(\"../Iconos/cancelar.png\")\n"
"}\n"
"QPushButton#btnSalir:hover {\n"
"    background-color: #D31217;\n"
"}\n"
"QPushButton#btnSalir:pressed {\n"
"    background-color: red;\n"
"    border-style: inset;\n"
"}\n"
"QPushButton#btnRegistrar:pressed {\n"
"    background-color: green;\n"
"    border-style: inset;\n"
"}\n"
"QLabel {\n"
"    font-family: \'Roboto\';\n"
"    font-size: 14px;\n"
"    border-style: inset;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(FormularioRegistroWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.lblUsuario.setObjectName("lblUsuario")
        self.gridLayout_2.addWidget(self.lblUsuario, 0, 0, 1, 1)
        self.leUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.leUsuario.setObjectName("leUsuario")
        self.gridLayout_2.addWidget(self.leUsuario, 0, 1, 1, 1)
        self.lblContrasena_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblContrasena_2.setObjectName("lblContrasena_2")
        self.gridLayout_2.addWidget(self.lblContrasena_2, 1, 0, 1, 1)
        self.leContrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.leContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leContrasena.setObjectName("leContrasena")
        self.gridLayout_2.addWidget(self.leContrasena, 1, 1, 1, 1)
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout_2.addWidget(self.lblNombre, 2, 0, 1, 1)
        self.leNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.leNombre.setObjectName("leNombre")
        self.gridLayout_2.addWidget(self.leNombre, 2, 1, 1, 1)
        self.lblApellido = QtWidgets.QLabel(self.centralwidget)
        self.lblApellido.setObjectName("lblApellido")
        self.gridLayout_2.addWidget(self.lblApellido, 3, 0, 1, 1)
        self.leApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.leApellido.setObjectName("leApellido")
        self.gridLayout_2.addWidget(self.leApellido, 3, 1, 1, 1)
        self.lblCI_RIF = QtWidgets.QLabel(self.centralwidget)
        self.lblCI_RIF.setObjectName("lblCI_RIF")
        self.gridLayout_2.addWidget(self.lblCI_RIF, 4, 0, 1, 1)
        self.leCI_RIF = QtWidgets.QLineEdit(self.centralwidget)
        self.leCI_RIF.setObjectName("leCI_RIF")
        self.gridLayout_2.addWidget(self.leCI_RIF, 4, 1, 1, 1)
        self.lblDireccion = QtWidgets.QLabel(self.centralwidget)
        self.lblDireccion.setObjectName("lblDireccion")
        self.gridLayout_2.addWidget(self.lblDireccion, 5, 0, 1, 1)
        self.leDireccion = QtWidgets.QTextEdit(self.centralwidget)
        self.leDireccion.setObjectName("leDireccion")
        self.gridLayout_2.addWidget(self.leDireccion, 5, 1, 1, 1)
        self.lblCorreo = QtWidgets.QLabel(self.centralwidget)
        self.lblCorreo.setObjectName("lblCorreo")
        self.gridLayout_2.addWidget(self.lblCorreo, 6, 0, 1, 1)
        self.leCorreo = QtWidgets.QLineEdit(self.centralwidget)
        self.leCorreo.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.leCorreo.setObjectName("leCorreo")
        self.gridLayout_2.addWidget(self.leCorreo, 6, 1, 1, 1)
        self.lblHotel = QtWidgets.QLabel(self.centralwidget)
        self.lblHotel.setObjectName("lblHotel")
        self.gridLayout_2.addWidget(self.lblHotel, 7, 0, 1, 1)
        self.leHotel = QtWidgets.QLineEdit(self.centralwidget)
        self.leHotel.setObjectName("leHotel")
        self.gridLayout_2.addWidget(self.leHotel, 7, 1, 1, 1)
        self.lblDireccion_Hotel = QtWidgets.QLabel(self.centralwidget)
        self.lblDireccion_Hotel.setObjectName("lblDireccion_Hotel")
        self.gridLayout_2.addWidget(self.lblDireccion_Hotel, 8, 0, 1, 1)
        self.leDireccion_Hotel = QtWidgets.QTextEdit(self.centralwidget)
        self.leDireccion_Hotel.setObjectName("leDireccion_Hotel")
        self.gridLayout_2.addWidget(self.leDireccion_Hotel, 8, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setText("")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.gridLayout.addWidget(self.btnRegistrar, 0, 1, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setText("")
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout.addWidget(self.btnSalir, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        FormularioRegistroWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormularioRegistroWin)
        self.btnSalir.clicked.connect(FormularioRegistroWin.close)
        QtCore.QMetaObject.connectSlotsByName(FormularioRegistroWin)

    def retranslateUi(self, FormularioRegistroWin):
        _translate = QtCore.QCoreApplication.translate
        FormularioRegistroWin.setWindowTitle(_translate("FormularioRegistroWin", "Registro"))
        self.lblUsuario.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Usuario para el ingreso al sistema</p></body></html>"))
        self.lblUsuario.setText(_translate("FormularioRegistroWin", "Usuario"))
        self.leUsuario.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Usuario para el ingreso al sistema</p></body></html>"))
        self.lblContrasena_2.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Contraseña para el ingreso al sistema</p></body></html>"))
        self.lblContrasena_2.setText(_translate("FormularioRegistroWin", "Contraseña"))
        self.leContrasena.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Contraseña para el ingreso al sistema</p></body></html>"))
        self.lblNombre.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Nombre del propietario</p></body></html>"))
        self.lblNombre.setText(_translate("FormularioRegistroWin", "Nombre"))
        self.leNombre.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Nombre del propetario del hotel</p></body></html>"))
        self.lblApellido.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Apellido del propietario</p></body></html>"))
        self.lblApellido.setText(_translate("FormularioRegistroWin", "Apellido"))
        self.leApellido.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Apellido del propetario del hotel</p></body></html>"))
        self.lblCI_RIF.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Cedula o RIF del propietario</p></body></html>"))
        self.lblCI_RIF.setText(_translate("FormularioRegistroWin", "CI/RIF"))
        self.leCI_RIF.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Cedula o RIF del propetario del Hotel</p></body></html>"))
        self.lblDireccion.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Direccion del propietario</p></body></html>"))
        self.lblDireccion.setText(_translate("FormularioRegistroWin", "Direccion"))
        self.leDireccion.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Direccion del propetario del hotel</p></body></html>"))
        self.lblCorreo.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Correo del propietario</p></body></html>"))
        self.lblCorreo.setText(_translate("FormularioRegistroWin", "Correo"))
        self.leCorreo.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Correo del propetario del hotel</p></body></html>"))
        self.lblHotel.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Nombre del hotel</p></body></html>"))
        self.lblHotel.setText(_translate("FormularioRegistroWin", "Hotel"))
        self.leHotel.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Nombre del hotel a registrar</p></body></html>"))
        self.lblDireccion_Hotel.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Direccion exacta del hotel</p></body></html>"))
        self.lblDireccion_Hotel.setText(_translate("FormularioRegistroWin", "Direccion Hotel"))
        self.leDireccion_Hotel.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Direccion exacta del hotel</p></body></html>"))
        self.leDireccion_Hotel.setHtml(_translate("FormularioRegistroWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Serif Semi-Condensed\'; font-size:10px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt; font-weight:400;\"><br /></p></body></html>"))
        self.btnRegistrar.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Registrar</p></body></html>"))
        self.btnSalir.setToolTip(_translate("FormularioRegistroWin", "<html><head/><body><p>Salir</p></body></html>"))

