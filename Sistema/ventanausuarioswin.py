# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanausuarios.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaUsuarios(object):
    def setupUi(self, VentanaUsuarios):
        VentanaUsuarios.setObjectName("VentanaUsuarios")
        VentanaUsuarios.resize(967, 510)
        VentanaUsuarios.setStyleSheet("QPushButton#btnAgregar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/usuario.png\");\n"
"}\n"
"\n"
"QPushButton#btnEstado{\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 25px;\n"
"        image: url(\"../Iconos/lista.png\");\n"
"}\n"
"\n"
"QPushButton#btnReporte {\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 25px;\n"
"        image: url(\"../Iconos/bloc.png\");\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border-radius: 15px;\n"
"    background-color: #A0D8D2;\n"
"    font-family: \'Roboto\';\n"
"}\n"
"\n"
"QLineEdit {\n"
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
"\n"
"QPushButton#btnAgregar:hover {\n"
"    background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnEstado:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnReporte:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: \'Roboto\';\n"
"    font-size: 14px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton#btnAgregar_2 {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/usuario2.png\");\n"
"}\n"
"\n"
"QPushButton#btnLimpiar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/limpiar.png\");\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Agregar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"\n"
"QPushButton#btnAgregar_2:hover {\n"
"    background-color: green;\n"
"}\n"
"\n"
"QPushButton#btnLimpiar:hover{\n"
"    background-color: #B9FFFD\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Agregar:hover {\n"
"    background-color: red;\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Estado{\n"
"    border-radius: 15px;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"QPushButton#btnCerrar_Estado:hover {\n"
"    background-color: red;\n"
"}\n"
"QPushButton#btnEliminar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/usuario3.png\");\n"
"}\n"
"QPushButton#btnRecargar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/archivo.png\");\n"
"}\n"
"QPushButton#btnCerrar_Lista {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"QPushButton#btnAsignar{\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/usuario4.png\");\n"
"}\n"
"QPushButton#btnEliminar:hover{\n"
"    background-color: red;\n"
"}\n"
"QPushButton#btnAgregar:hover {\n"
"    background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnRecargar:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Lista:hover {\n"
"        background-color: red;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QToolBox {\n"
"    border-radius: 15px;\n"
"    \n"
"}\n"
"QTabWidget {\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    borde-radius: 15px;\n"
"    background-color:grey;\n"
"}\n"
"QAction {\n"
"    background-color: white;\n"
"}\n"
"QMainWindow {\n"
"        background-color: #009688;\n"
"}\n"
"QTabWidget {\n"
"    border-size: 15px;\n"
"    background-color: #009688;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(VentanaUsuarios)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gbUsuarios = QtWidgets.QGroupBox(self.centralwidget)
        self.gbUsuarios.setTitle("")
        self.gbUsuarios.setObjectName("gbUsuarios")
        self.gridLayout = QtWidgets.QGridLayout(self.gbUsuarios)
        self.gridLayout.setObjectName("gridLayout")
        self.btnAgregar = QtWidgets.QPushButton(self.gbUsuarios)
        self.btnAgregar.setText("")
        self.btnAgregar.setObjectName("btnAgregar")
        self.gridLayout.addWidget(self.btnAgregar, 0, 0, 1, 1)
        self.btnReporte = QtWidgets.QPushButton(self.gbUsuarios)
        self.btnReporte.setText("")
        self.btnReporte.setObjectName("btnReporte")
        self.gridLayout.addWidget(self.btnReporte, 0, 2, 1, 1)
        self.btnEstado = QtWidgets.QPushButton(self.gbUsuarios)
        self.btnEstado.setText("")
        self.btnEstado.setObjectName("btnEstado")
        self.gridLayout.addWidget(self.btnEstado, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.gbUsuarios, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 0, 0, 1, 1)
        self.tabClientes = QtWidgets.QTabWidget(self.centralwidget)
        self.tabClientes.setEnabled(True)
        self.tabClientes.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabClientes.setTabsClosable(False)
        self.tabClientes.setObjectName("tabClientes")
        self.tabAgregar = QtWidgets.QWidget()
        self.tabAgregar.setObjectName("tabAgregar")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabAgregar)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCI_RIF = QtWidgets.QLabel(self.tabAgregar)
        self.lblCI_RIF.setObjectName("lblCI_RIF")
        self.gridLayout_2.addWidget(self.lblCI_RIF, 0, 0, 1, 1)
        self.leCI_RIF = QtWidgets.QLineEdit(self.tabAgregar)
        self.leCI_RIF.setObjectName("leCI_RIF")
        self.gridLayout_2.addWidget(self.leCI_RIF, 0, 1, 1, 1)
        self.lblNombre = QtWidgets.QLabel(self.tabAgregar)
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout_2.addWidget(self.lblNombre, 0, 2, 1, 1)
        self.leNombre = QtWidgets.QLineEdit(self.tabAgregar)
        self.leNombre.setObjectName("leNombre")
        self.gridLayout_2.addWidget(self.leNombre, 0, 3, 1, 1)
        self.lblApellido = QtWidgets.QLabel(self.tabAgregar)
        self.lblApellido.setObjectName("lblApellido")
        self.gridLayout_2.addWidget(self.lblApellido, 1, 0, 1, 1)
        self.leCorreo = QtWidgets.QLineEdit(self.tabAgregar)
        self.leCorreo.setObjectName("leCorreo")
        self.gridLayout_2.addWidget(self.leCorreo, 1, 3, 1, 1)
        self.leApellido = QtWidgets.QLineEdit(self.tabAgregar)
        self.leApellido.setObjectName("leApellido")
        self.gridLayout_2.addWidget(self.leApellido, 1, 1, 1, 1)
        self.lblCorreo = QtWidgets.QLabel(self.tabAgregar)
        self.lblCorreo.setObjectName("lblCorreo")
        self.gridLayout_2.addWidget(self.lblCorreo, 1, 2, 1, 1)
        self.leTelefono = QtWidgets.QLineEdit(self.tabAgregar)
        self.leTelefono.setObjectName("leTelefono")
        self.gridLayout_2.addWidget(self.leTelefono, 2, 1, 1, 1)
        self.lblTelefono = QtWidgets.QLabel(self.tabAgregar)
        self.lblTelefono.setObjectName("lblTelefono")
        self.gridLayout_2.addWidget(self.lblTelefono, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 1)
        self.btnAgregar_2 = QtWidgets.QPushButton(self.tabAgregar)
        self.btnAgregar_2.setText("")
        self.btnAgregar_2.setObjectName("btnAgregar_2")
        self.gridLayout_4.addWidget(self.btnAgregar_2, 0, 1, 1, 1)
        self.btnLimpiar = QtWidgets.QPushButton(self.tabAgregar)
        self.btnLimpiar.setText("")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.gridLayout_4.addWidget(self.btnLimpiar, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 4, 1, 1)
        self.btnCerrar_Agregar = QtWidgets.QPushButton(self.tabAgregar)
        self.btnCerrar_Agregar.setText("")
        self.btnCerrar_Agregar.setObjectName("btnCerrar_Agregar")
        self.gridLayout_4.addWidget(self.btnCerrar_Agregar, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabClientes.addTab(self.tabAgregar, "")
        self.tabEstado = QtWidgets.QWidget()
        self.tabEstado.setEnabled(True)
        self.tabEstado.setObjectName("tabEstado")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tabEstado)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.leBuscar = QtWidgets.QLineEdit(self.tabEstado)
        self.leBuscar.setObjectName("leBuscar")
        self.gridLayout_6.addWidget(self.leBuscar, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tablaUsuarios = QtWidgets.QTableWidget(self.tabEstado)
        self.tablaUsuarios.setObjectName("tablaUsuarios")
        self.tablaUsuarios.setColumnCount(0)
        self.tablaUsuarios.setRowCount(0)
        self.gridLayout_8.addWidget(self.tablaUsuarios, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 0, 0, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(self.tabEstado)
        self.btnEliminar.setText("")
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout_7.addWidget(self.btnEliminar, 0, 1, 1, 1)
        self.btnRecargar = QtWidgets.QPushButton(self.tabEstado)
        self.btnRecargar.setText("")
        self.btnRecargar.setObjectName("btnRecargar")
        self.gridLayout_7.addWidget(self.btnRecargar, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 0, 4, 1, 1)
        self.btnCerrar_Estado = QtWidgets.QPushButton(self.tabEstado)
        self.btnCerrar_Estado.setText("")
        self.btnCerrar_Estado.setObjectName("btnCerrar_Estado")
        self.gridLayout_7.addWidget(self.btnCerrar_Estado, 0, 3, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)
        self.tabClientes.addTab(self.tabEstado, "")
        self.gridLayout_9.addWidget(self.tabClientes, 1, 0, 1, 3)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        VentanaUsuarios.setCentralWidget(self.centralwidget)
        self.mbUsuarios = QtWidgets.QMenuBar(VentanaUsuarios)
        self.mbUsuarios.setGeometry(QtCore.QRect(0, 0, 967, 22))
        self.mbUsuarios.setObjectName("mbUsuarios")
        self.menuUsuarios = QtWidgets.QMenu(self.mbUsuarios)
        self.menuUsuarios.setObjectName("menuUsuarios")
        self.menuReporte = QtWidgets.QMenu(self.menuUsuarios)
        self.menuReporte.setObjectName("menuReporte")
        self.menuInformacion = QtWidgets.QMenu(self.mbUsuarios)
        self.menuInformacion.setObjectName("menuInformacion")
        VentanaUsuarios.setMenuBar(self.mbUsuarios)
        self.sbUsuarios = QtWidgets.QStatusBar(VentanaUsuarios)
        self.sbUsuarios.setObjectName("sbUsuarios")
        VentanaUsuarios.setStatusBar(self.sbUsuarios)
        self.actionAgregar = QtWidgets.QAction(VentanaUsuarios)
        self.actionAgregar.setObjectName("actionAgregar")
        self.actionEstado = QtWidgets.QAction(VentanaUsuarios)
        self.actionEstado.setObjectName("actionEstado")
        self.actionSalir = QtWidgets.QAction(VentanaUsuarios)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcercaDe = QtWidgets.QAction(VentanaUsuarios)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.actionAgregar_2 = QtWidgets.QAction(VentanaUsuarios)
        self.actionAgregar_2.setObjectName("actionAgregar_2")
        self.actionEstado_2 = QtWidgets.QAction(VentanaUsuarios)
        self.actionEstado_2.setObjectName("actionEstado_2")
        self.actionSalir_2 = QtWidgets.QAction(VentanaUsuarios)
        self.actionSalir_2.setObjectName("actionSalir_2")
        self.actionCSV = QtWidgets.QAction(VentanaUsuarios)
        self.actionCSV.setObjectName("actionCSV")
        self.actionPDF = QtWidgets.QAction(VentanaUsuarios)
        self.actionPDF.setObjectName("actionPDF")
        self.menuReporte.addAction(self.actionCSV)
        self.menuReporte.addAction(self.actionPDF)
        self.menuUsuarios.addSeparator()
        self.menuUsuarios.addAction(self.actionAgregar_2)
        self.menuUsuarios.addAction(self.actionEstado_2)
        self.menuUsuarios.addAction(self.menuReporte.menuAction())
        self.menuUsuarios.addSeparator()
        self.menuUsuarios.addAction(self.actionSalir_2)
        self.menuInformacion.addAction(self.actionAcercaDe)
        self.mbUsuarios.addAction(self.menuUsuarios.menuAction())
        self.mbUsuarios.addAction(self.menuInformacion.menuAction())

        self.retranslateUi(VentanaUsuarios)
        self.tabClientes.setCurrentIndex(1)
        self.btnLimpiar.clicked.connect(self.leTelefono.clear)
        self.btnLimpiar.clicked.connect(self.leCorreo.clear)
        self.btnLimpiar.clicked.connect(self.leNombre.clear)
        self.btnLimpiar.clicked.connect(self.leApellido.clear)
        self.btnLimpiar.clicked.connect(self.leCI_RIF.clear)
        QtCore.QMetaObject.connectSlotsByName(VentanaUsuarios)

    def retranslateUi(self, VentanaUsuarios):
        _translate = QtCore.QCoreApplication.translate
        VentanaUsuarios.setWindowTitle(_translate("VentanaUsuarios", "Clientes"))
        self.btnAgregar.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Agregar un nuevo cliente</p></body></html>"))
        self.btnReporte.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Generar un archivo con la lista de clientes</p></body></html>"))
        self.btnEstado.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Ver lista de clientes registrados</p></body></html>"))
        self.lblCI_RIF.setText(_translate("VentanaUsuarios", "CI/RIF"))
        self.lblNombre.setText(_translate("VentanaUsuarios", "Nombre"))
        self.lblApellido.setText(_translate("VentanaUsuarios", "Apellido"))
        self.lblCorreo.setText(_translate("VentanaUsuarios", "Correo"))
        self.lblTelefono.setText(_translate("VentanaUsuarios", "Telefono"))
        self.btnAgregar_2.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Agregar el nuevo cliente</p></body></html>"))
        self.btnLimpiar.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Borrar lo escrito</p></body></html>"))
        self.btnCerrar_Agregar.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Cerrar la pestaña agregar</p></body></html>"))
        self.tabClientes.setTabText(self.tabClientes.indexOf(self.tabAgregar), _translate("VentanaUsuarios", "Agregar"))
        self.btnEliminar.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Eliminar un cliente</p></body></html>"))
        self.btnRecargar.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Actualizar la lista de clientes</p></body></html>"))
        self.btnCerrar_Estado.setToolTip(_translate("VentanaUsuarios", "<html><head/><body><p>Cerrar la lista </p></body></html>"))
        self.tabClientes.setTabText(self.tabClientes.indexOf(self.tabEstado), _translate("VentanaUsuarios", "Estado"))
        self.menuUsuarios.setTitle(_translate("VentanaUsuarios", "Cientes"))
        self.menuReporte.setTitle(_translate("VentanaUsuarios", "Reporte"))
        self.menuInformacion.setTitle(_translate("VentanaUsuarios", "Informacion"))
        self.actionAgregar.setText(_translate("VentanaUsuarios", "Agregar"))
        self.actionEstado.setText(_translate("VentanaUsuarios", "Estado"))
        self.actionSalir.setText(_translate("VentanaUsuarios", "Salir"))
        self.actionAcercaDe.setText(_translate("VentanaUsuarios", "AcercaDe"))
        self.actionAgregar_2.setText(_translate("VentanaUsuarios", "Agregar"))
        self.actionEstado_2.setText(_translate("VentanaUsuarios", "Estado"))
        self.actionSalir_2.setText(_translate("VentanaUsuarios", "Salir"))
        self.actionCSV.setText(_translate("VentanaUsuarios", "CSV"))
        self.actionPDF.setText(_translate("VentanaUsuarios", "PDF"))

