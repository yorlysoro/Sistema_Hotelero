# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanahotelwin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaHotel(object):
    def setupUi(self, VentanaHotel):
        VentanaHotel.setObjectName("VentanaHotel")
        VentanaHotel.resize(1042, 603)
        VentanaHotel.setStyleSheet("QPushButton#btnCuentas {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/grafico.png\");\n"
"}\n"
"\n"
"QPushButton#btnClientes {\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 25px;\n"
"        image: url(\"../Iconos/grafico-circular.png\");\n"
"}\n"
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
"\n"
"QPushButton#btnCuentas:hover {\n"
"    background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnClientes:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    font-family: \'Roboto\';\n"
"    font-size: 14px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#btnCerrar_Negocio{\n"
"    border-radius: 15px;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"QPushButton#btnCerrar_Negocio:hover{\n"
"    background-color: red;\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Cliente {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"\n"
"\n"
"QPushButton#btnCerrar_Cliente:hover {\n"
"        background-color: red;\n"
"}\n"
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
"\n"
"QMainWindow {\n"
"        background-color: #009688;\n"
"}\n"
"QTabWidget {\n"
" border-size: 15px;\n"
" background-color: #009688;\n"
"}\n"
"\n"
"QToolBox {\n"
"    border-size: 15px;\n"
"     background-color: #009688;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(VentanaHotel)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gBHotel = QtWidgets.QGroupBox(self.centralwidget)
        self.gBHotel.setTitle("")
        self.gBHotel.setObjectName("gBHotel")
        self.gridLayout = QtWidgets.QGridLayout(self.gBHotel)
        self.gridLayout.setObjectName("gridLayout")
        self.btnCuentas = QtWidgets.QPushButton(self.gBHotel)
        self.btnCuentas.setText("")
        self.btnCuentas.setObjectName("btnCuentas")
        self.gridLayout.addWidget(self.btnCuentas, 0, 0, 1, 1)
        self.btnClientes = QtWidgets.QPushButton(self.gBHotel)
        self.btnClientes.setText("")
        self.btnClientes.setObjectName("btnClientes")
        self.gridLayout.addWidget(self.btnClientes, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.gBHotel, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabHotel = QtWidgets.QTabWidget(self.centralwidget)
        self.tabHotel.setObjectName("tabHotel")
        self.tabCuentas = QtWidgets.QWidget()
        self.tabCuentas.setObjectName("tabCuentas")
        self.layoutWidget = QtWidgets.QWidget(self.tabCuentas)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblGuardar = QtWidgets.QLabel(self.layoutWidget)
        self.lblGuardar.setObjectName("lblGuardar")
        self.gridLayout_5.addWidget(self.lblGuardar, 1, 0, 1, 1)
        self.cBGuardar = QtWidgets.QComboBox(self.layoutWidget)
        self.cBGuardar.setObjectName("cBGuardar")
        self.cBGuardar.addItem("")
        self.cBGuardar.addItem("")
        self.cBGuardar.addItem("")
        self.gridLayout_5.addWidget(self.cBGuardar, 1, 1, 1, 1)
        self.tbNegocio = QtWidgets.QToolBox(self.layoutWidget)
        self.tbNegocio.setObjectName("tbNegocio")
        self.pIngresos = QtWidgets.QWidget()
        self.pIngresos.setGeometry(QtCore.QRect(0, 0, 104, 45))
        self.pIngresos.setObjectName("pIngresos")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.pIngresos)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.pIngresos)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.cBIngresos = QtWidgets.QComboBox(self.pIngresos)
        self.cBIngresos.setObjectName("cBIngresos")
        self.cBIngresos.addItem("")
        self.cBIngresos.addItem("")
        self.cBIngresos.addItem("")
        self.cBIngresos.addItem("")
        self.gridLayout_7.addWidget(self.cBIngresos, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.tbNegocio.addItem(self.pIngresos, "")
        self.pEgresos = QtWidgets.QWidget()
        self.pEgresos.setGeometry(QtCore.QRect(0, 0, 197, 77))
        self.pEgresos.setObjectName("pEgresos")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.pEgresos)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_2 = QtWidgets.QLabel(self.pEgresos)
        self.label_2.setObjectName("label_2")
        self.gridLayout_15.addWidget(self.label_2, 0, 0, 1, 1)
        self.cBEgresos = QtWidgets.QComboBox(self.pEgresos)
        self.cBEgresos.setObjectName("cBEgresos")
        self.cBEgresos.addItem("")
        self.cBEgresos.addItem("")
        self.cBEgresos.addItem("")
        self.cBEgresos.addItem("")
        self.gridLayout_15.addWidget(self.cBEgresos, 0, 1, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)
        self.tbNegocio.addItem(self.pEgresos, "")
        self.gridLayout_5.addWidget(self.tbNegocio, 0, 0, 1, 2)
        self.gridLayout_12.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem3, 1, 0, 1, 1)
        self.btnCerrar_Negocio = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCerrar_Negocio.setText("")
        self.btnCerrar_Negocio.setObjectName("btnCerrar_Negocio")
        self.gridLayout_11.addWidget(self.btnCerrar_Negocio, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem5, 2, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.tablaCuentas = QtWidgets.QTableWidget(self.tabCuentas)
        self.tablaCuentas.setGeometry(QtCore.QRect(225, 11, 771, 411))
        self.tablaCuentas.setObjectName("tablaCuentas")
        self.tablaCuentas.setColumnCount(0)
        self.tablaCuentas.setRowCount(0)
        self.tabHotel.addTab(self.tabCuentas, "")
        self.tabClientes = QtWidgets.QWidget()
        self.tabClientes.setObjectName("tabClientes")
        self.layoutWidget1 = QtWidgets.QWidget(self.tabClientes)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 201, 351))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lblGuardar_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.lblGuardar_2.setObjectName("lblGuardar_2")
        self.gridLayout_6.addWidget(self.lblGuardar_2, 1, 0, 1, 1)
        self.cBGuardar_2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.cBGuardar_2.setObjectName("cBGuardar_2")
        self.cBGuardar_2.addItem("")
        self.cBGuardar_2.addItem("")
        self.cBGuardar_2.addItem("")
        self.gridLayout_6.addWidget(self.cBGuardar_2, 1, 1, 1, 1)
        self.tbClientes = QtWidgets.QToolBox(self.layoutWidget1)
        self.tbClientes.setObjectName("tbClientes")
        self.pClientes = QtWidgets.QWidget()
        self.pClientes.setGeometry(QtCore.QRect(0, 0, 104, 45))
        self.pClientes.setObjectName("pClientes")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.pClientes)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lePor_Clientes = QtWidgets.QLabel(self.pClientes)
        self.lePor_Clientes.setObjectName("lePor_Clientes")
        self.gridLayout_9.addWidget(self.lePor_Clientes, 0, 0, 1, 1)
        self.cBClientes = QtWidgets.QComboBox(self.pClientes)
        self.cBClientes.setObjectName("cBClientes")
        self.cBClientes.addItem("")
        self.cBClientes.addItem("")
        self.cBClientes.addItem("")
        self.cBClientes.addItem("")
        self.gridLayout_9.addWidget(self.cBClientes, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.tbClientes.addItem(self.pClientes, "")
        self.gridLayout_6.addWidget(self.tbClientes, 0, 0, 1, 2)
        self.gridLayout_14.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem7, 1, 0, 1, 1)
        self.btnCerrar_Cliente = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnCerrar_Cliente.setText("")
        self.btnCerrar_Cliente.setObjectName("btnCerrar_Cliente")
        self.gridLayout_13.addWidget(self.btnCerrar_Cliente, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem8, 1, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem9, 2, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_13, 1, 0, 1, 1)
        self.tablaClientes = QtWidgets.QTableWidget(self.tabClientes)
        self.tablaClientes.setGeometry(QtCore.QRect(225, 11, 771, 411))
        self.tablaClientes.setObjectName("tablaClientes")
        self.tablaClientes.setColumnCount(0)
        self.tablaClientes.setRowCount(0)
        self.tabHotel.addTab(self.tabClientes, "")
        self.gridLayout_3.addWidget(self.tabHotel, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        VentanaHotel.setCentralWidget(self.centralwidget)
        self.sbHotel = QtWidgets.QStatusBar(VentanaHotel)
        self.sbHotel.setObjectName("sbHotel")
        VentanaHotel.setStatusBar(self.sbHotel)
        self.mbHotel = QtWidgets.QMenuBar(VentanaHotel)
        self.mbHotel.setGeometry(QtCore.QRect(0, 0, 1042, 22))
        self.mbHotel.setObjectName("mbHotel")
        self.menuHotel = QtWidgets.QMenu(self.mbHotel)
        self.menuHotel.setObjectName("menuHotel")
        self.menuInformacion = QtWidgets.QMenu(self.mbHotel)
        self.menuInformacion.setObjectName("menuInformacion")
        VentanaHotel.setMenuBar(self.mbHotel)
        self.actionCuentas = QtWidgets.QAction(VentanaHotel)
        self.actionCuentas.setObjectName("actionCuentas")
        self.actionClientes = QtWidgets.QAction(VentanaHotel)
        self.actionClientes.setObjectName("actionClientes")
        self.actionSalir = QtWidgets.QAction(VentanaHotel)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcercaDe = QtWidgets.QAction(VentanaHotel)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.menuHotel.addAction(self.actionCuentas)
        self.menuHotel.addAction(self.actionClientes)
        self.menuHotel.addSeparator()
        self.menuHotel.addAction(self.actionSalir)
        self.menuInformacion.addAction(self.actionAcercaDe)
        self.mbHotel.addAction(self.menuHotel.menuAction())
        self.mbHotel.addAction(self.menuInformacion.menuAction())

        self.retranslateUi(VentanaHotel)
        self.tabHotel.setCurrentIndex(0)
        self.tbNegocio.setCurrentIndex(1)
        self.tbClientes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VentanaHotel)

    def retranslateUi(self, VentanaHotel):
        _translate = QtCore.QCoreApplication.translate
        VentanaHotel.setWindowTitle(_translate("VentanaHotel", "MainWindow"))
        self.btnCuentas.setToolTip(_translate("VentanaHotel", "<html><head/><body><p>Ver la cantidad de egresos e ingresos del dia</p></body></html>"))
        self.btnClientes.setToolTip(_translate("VentanaHotel", "<html><head/><body><p>Ver la cantidad de clientes que ingresan al hotel</p></body></html>"))
        self.lblGuardar.setText(_translate("VentanaHotel", "Guardar"))
        self.cBGuardar.setItemText(0, _translate("VentanaHotel", "..."))
        self.cBGuardar.setItemText(1, _translate("VentanaHotel", "PDF"))
        self.cBGuardar.setItemText(2, _translate("VentanaHotel", "CSV"))
        self.label.setText(_translate("VentanaHotel", "Por"))
        self.cBIngresos.setItemText(0, _translate("VentanaHotel", "..."))
        self.cBIngresos.setItemText(1, _translate("VentanaHotel", "Dia"))
        self.cBIngresos.setItemText(2, _translate("VentanaHotel", "Mes"))
        self.cBIngresos.setItemText(3, _translate("VentanaHotel", "Año"))
        self.tbNegocio.setItemText(self.tbNegocio.indexOf(self.pIngresos), _translate("VentanaHotel", "Ingresos"))
        self.label_2.setText(_translate("VentanaHotel", "Por"))
        self.cBEgresos.setItemText(0, _translate("VentanaHotel", "..."))
        self.cBEgresos.setItemText(1, _translate("VentanaHotel", "Dia"))
        self.cBEgresos.setItemText(2, _translate("VentanaHotel", "Mes"))
        self.cBEgresos.setItemText(3, _translate("VentanaHotel", "Año"))
        self.tbNegocio.setItemText(self.tbNegocio.indexOf(self.pEgresos), _translate("VentanaHotel", "Egresos"))
        self.btnCerrar_Negocio.setToolTip(_translate("VentanaHotel", "<html><head/><body><p>Cerrar la pestaña cuentas</p></body></html>"))
        self.tabHotel.setTabText(self.tabHotel.indexOf(self.tabCuentas), _translate("VentanaHotel", "Cuentas"))
        self.lblGuardar_2.setText(_translate("VentanaHotel", "Guardar"))
        self.cBGuardar_2.setItemText(0, _translate("VentanaHotel", "..."))
        self.cBGuardar_2.setItemText(1, _translate("VentanaHotel", "PDF"))
        self.cBGuardar_2.setItemText(2, _translate("VentanaHotel", "CSV"))
        self.lePor_Clientes.setText(_translate("VentanaHotel", "Por"))
        self.cBClientes.setItemText(0, _translate("VentanaHotel", "..."))
        self.cBClientes.setItemText(1, _translate("VentanaHotel", "Dia"))
        self.cBClientes.setItemText(2, _translate("VentanaHotel", "Mes"))
        self.cBClientes.setItemText(3, _translate("VentanaHotel", "Año"))
        self.tbClientes.setItemText(self.tbClientes.indexOf(self.pClientes), _translate("VentanaHotel", "Clientes"))
        self.btnCerrar_Cliente.setToolTip(_translate("VentanaHotel", "<html><head/><body><p>Cerrar la pestaña clientes</p></body></html>"))
        self.tabHotel.setTabText(self.tabHotel.indexOf(self.tabClientes), _translate("VentanaHotel", "Clientes"))
        self.menuHotel.setTitle(_translate("VentanaHotel", "Hotel"))
        self.menuInformacion.setTitle(_translate("VentanaHotel", "Informacion"))
        self.actionCuentas.setText(_translate("VentanaHotel", "Cuentas"))
        self.actionClientes.setText(_translate("VentanaHotel", "Clientes"))
        self.actionSalir.setText(_translate("VentanaHotel", "Salir"))
        self.actionAcercaDe.setText(_translate("VentanaHotel", "AcercaDe"))

