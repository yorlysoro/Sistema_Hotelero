# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanahabitacioneswin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaHabitaciones(object):
    def setupUi(self, VentanaHabitaciones):
        VentanaHabitaciones.setObjectName("VentanaHabitaciones")
        VentanaHabitaciones.resize(1048, 501)
        VentanaHabitaciones.setStyleSheet("QPushButton#btnAsignar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/mas.png\");\n"
"}\n"
"\n"
"QPushButton#btnEstado {\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 25px;\n"
"        image: url(\"../Iconos/lista.png\");\n"
"}\n"
"\n"
"QPushButton#btnAsignaciones {\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 25px;\n"
"        image: url(\"../Iconos/lista2.png\");\n"
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
"\n"
"QPushButton#btnAsignar:hover {\n"
"    background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnEstado:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnAsignaciones:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: \'Roboto\';\n"
"    font-size: 14px;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton#btnAsignar_2 {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/mas.png\");\n"
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
"QPushButton#btnCerrar_Asignar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"\n"
"QPushButton#btnAsignar_2:hover {\n"
"    background-color: green;\n"
"}\n"
"\n"
"QPushButton#btnLimpiar:hover{\n"
"    background-color: #B9FFFD\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Asignar:hover {\n"
"    background-color: red;\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Estado{\n"
"    border-radius: 15px;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"QPushButton#btnCerrar_Estado:hover{\n"
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
"QPushButton#btnAsignar:hover {\n"
"    background-color: green;\n"
"}\n"
"\n"
"QPushButton#btnRecargar_Estado:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"QPushButton#btnLimpiar:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"QPushButton#btnCerrar_Estado:hover {\n"
"        background-color: red;\n"
"}\n"
"QPushButton#btnCerrar_Asignar:hover {\n"
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
"QPushButton#btnRecargar_Estado {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/archivo.png\");\n"
"}\n"
"QPushButton#btnRecargar:hover {\n"
"    background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Asignaciones {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"\n"
"QPushButton#btnCerrar_Asignaciones:hover {\n"
"    background-color: red;\n"
"}\n"
"QMainWindow {\n"
"        background-color: #009688;\n"
"}\n"
"\n"
"QTabWidget {\n"
" border-size: 15px;\n"
" background-color: #009688;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(VentanaHabitaciones)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gBHabitaciones = QtWidgets.QGroupBox(self.centralwidget)
        self.gBHabitaciones.setTitle("")
        self.gBHabitaciones.setObjectName("gBHabitaciones")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gBHabitaciones)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnAsignar = QtWidgets.QPushButton(self.gBHabitaciones)
        self.btnAsignar.setText("")
        self.btnAsignar.setObjectName("btnAsignar")
        self.gridLayout.addWidget(self.btnAsignar, 0, 0, 1, 1)
        self.btnEstado = QtWidgets.QPushButton(self.gBHabitaciones)
        self.btnEstado.setText("")
        self.btnEstado.setObjectName("btnEstado")
        self.gridLayout.addWidget(self.btnEstado, 0, 1, 1, 1)
        self.btnAsignaciones = QtWidgets.QPushButton(self.gBHabitaciones)
        self.btnAsignaciones.setText("")
        self.btnAsignaciones.setObjectName("btnAsignaciones")
        self.gridLayout.addWidget(self.btnAsignaciones, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.gBHabitaciones, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabHabitaciones = QtWidgets.QTabWidget(self.centralwidget)
        self.tabHabitaciones.setObjectName("tabHabitaciones")
        self.tabAsignar = QtWidgets.QWidget()
        self.tabAsignar.setObjectName("tabAsignar")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tabAsignar)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblCI_RIF = QtWidgets.QLabel(self.tabAsignar)
        self.lblCI_RIF.setObjectName("lblCI_RIF")
        self.gridLayout_5.addWidget(self.lblCI_RIF, 0, 0, 1, 1)
        self.leCI_RIF = QtWidgets.QLineEdit(self.tabAsignar)
        self.leCI_RIF.setObjectName("leCI_RIF")
        self.gridLayout_5.addWidget(self.leCI_RIF, 0, 1, 1, 1)
        self.lblHabitacion = QtWidgets.QLabel(self.tabAsignar)
        self.lblHabitacion.setObjectName("lblHabitacion")
        self.gridLayout_5.addWidget(self.lblHabitacion, 0, 2, 1, 1)
        self.leHabitacion = QtWidgets.QLineEdit(self.tabAsignar)
        self.leHabitacion.setObjectName("leHabitacion")
        self.gridLayout_5.addWidget(self.leHabitacion, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lblEntrada = QtWidgets.QLabel(self.tabAsignar)
        self.lblEntrada.setObjectName("lblEntrada")
        self.gridLayout_6.addWidget(self.lblEntrada, 0, 0, 1, 1)
        self.dateEntrada = QtWidgets.QDateEdit(self.tabAsignar)
        self.dateEntrada.setObjectName("dateEntrada")
        self.gridLayout_6.addWidget(self.dateEntrada, 0, 1, 1, 1)
        self.lblSalida = QtWidgets.QLabel(self.tabAsignar)
        self.lblSalida.setObjectName("lblSalida")
        self.gridLayout_6.addWidget(self.lblSalida, 0, 2, 1, 1)
        self.dateSalida = QtWidgets.QDateEdit(self.tabAsignar)
        self.dateSalida.setObjectName("dateSalida")
        self.gridLayout_6.addWidget(self.dateSalida, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lblCostoDia = QtWidgets.QLabel(self.tabAsignar)
        self.lblCostoDia.setObjectName("lblCostoDia")
        self.gridLayout_8.addWidget(self.lblCostoDia, 0, 0, 1, 1)
        self.leCostoDia = QtWidgets.QLineEdit(self.tabAsignar)
        self.leCostoDia.setObjectName("leCostoDia")
        self.gridLayout_8.addWidget(self.leCostoDia, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_8, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.btnAsignar_2 = QtWidgets.QPushButton(self.tabAsignar)
        self.btnAsignar_2.setText("")
        self.btnAsignar_2.setObjectName("btnAsignar_2")
        self.gridLayout_10.addWidget(self.btnAsignar_2, 0, 0, 1, 1)
        self.btnLimpiar = QtWidgets.QPushButton(self.tabAsignar)
        self.btnLimpiar.setText("")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.gridLayout_10.addWidget(self.btnLimpiar, 0, 1, 1, 1)
        self.btnCerrar_Asignar = QtWidgets.QPushButton(self.tabAsignar)
        self.btnCerrar_Asignar.setText("")
        self.btnCerrar_Asignar.setObjectName("btnCerrar_Asignar")
        self.gridLayout_10.addWidget(self.btnCerrar_Asignar, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.tabHabitaciones.addTab(self.tabAsignar, "")
        self.tabEstado = QtWidgets.QWidget()
        self.tabEstado.setObjectName("tabEstado")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tabEstado)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.tablaEstado = QtWidgets.QTableWidget(self.tabEstado)
        self.tablaEstado.setObjectName("tablaEstado")
        self.tablaEstado.setColumnCount(0)
        self.tablaEstado.setRowCount(0)
        self.gridLayout_12.addWidget(self.tablaEstado, 0, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem4, 0, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.lblGuardar = QtWidgets.QLabel(self.tabEstado)
        self.lblGuardar.setObjectName("lblGuardar")
        self.gridLayout_14.addWidget(self.lblGuardar, 0, 0, 1, 1)
        self.cBGuardar = QtWidgets.QComboBox(self.tabEstado)
        self.cBGuardar.setObjectName("cBGuardar")
        self.cBGuardar.addItem("")
        self.cBGuardar.addItem("")
        self.cBGuardar.addItem("")
        self.gridLayout_14.addWidget(self.cBGuardar, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem5, 0, 4, 1, 1)
        self.btnCerrar_Estado = QtWidgets.QPushButton(self.tabEstado)
        self.btnCerrar_Estado.setText("")
        self.btnCerrar_Estado.setObjectName("btnCerrar_Estado")
        self.gridLayout_13.addWidget(self.btnCerrar_Estado, 0, 3, 1, 1)
        self.btnRecargar_Estado = QtWidgets.QPushButton(self.tabEstado)
        self.btnRecargar_Estado.setText("")
        self.btnRecargar_Estado.setObjectName("btnRecargar_Estado")
        self.gridLayout_13.addWidget(self.btnRecargar_Estado, 0, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_13, 1, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_15, 0, 0, 1, 1)
        self.tabHabitaciones.addTab(self.tabEstado, "")
        self.tabAsignaciones = QtWidgets.QWidget()
        self.tabAsignaciones.setObjectName("tabAsignaciones")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tabAsignaciones)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.leBuscarAsignaciones = QtWidgets.QLineEdit(self.tabAsignaciones)
        self.leBuscarAsignaciones.setStyleSheet("QLineEdit {background yellow\n"
"border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0))};")
        self.leBuscarAsignaciones.setObjectName("leBuscarAsignaciones")
        self.gridLayout_16.addWidget(self.leBuscarAsignaciones, 0, 0, 1, 1)
        self.tablaAsignaciones = QtWidgets.QTableWidget(self.tabAsignaciones)
        self.tablaAsignaciones.setObjectName("tablaAsignaciones")
        self.tablaAsignaciones.setColumnCount(0)
        self.tablaAsignaciones.setRowCount(0)
        self.gridLayout_16.addWidget(self.tablaAsignaciones, 1, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem6, 0, 0, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(self.tabAsignaciones)
        self.btnEliminar.setText("")
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout_17.addWidget(self.btnEliminar, 0, 1, 1, 1)
        self.btnRecargar = QtWidgets.QPushButton(self.tabAsignaciones)
        self.btnRecargar.setText("")
        self.btnRecargar.setObjectName("btnRecargar")
        self.gridLayout_17.addWidget(self.btnRecargar, 0, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem7, 0, 4, 1, 1)
        self.btnCerrar_Asignaciones = QtWidgets.QPushButton(self.tabAsignaciones)
        self.btnCerrar_Asignaciones.setText("")
        self.btnCerrar_Asignaciones.setObjectName("btnCerrar_Asignaciones")
        self.gridLayout_17.addWidget(self.btnCerrar_Asignaciones, 0, 3, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_17, 1, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.tabHabitaciones.addTab(self.tabAsignaciones, "")
        self.gridLayout_20.addWidget(self.tabHabitaciones, 1, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        VentanaHabitaciones.setCentralWidget(self.centralwidget)
        self.mbHabitaciones = QtWidgets.QMenuBar(VentanaHabitaciones)
        self.mbHabitaciones.setGeometry(QtCore.QRect(0, 0, 1048, 22))
        self.mbHabitaciones.setObjectName("mbHabitaciones")
        self.menuHabitaciones = QtWidgets.QMenu(self.mbHabitaciones)
        self.menuHabitaciones.setObjectName("menuHabitaciones")
        self.menuInformacion = QtWidgets.QMenu(self.mbHabitaciones)
        self.menuInformacion.setObjectName("menuInformacion")
        VentanaHabitaciones.setMenuBar(self.mbHabitaciones)
        self.stHabitaciones = QtWidgets.QStatusBar(VentanaHabitaciones)
        self.stHabitaciones.setObjectName("stHabitaciones")
        VentanaHabitaciones.setStatusBar(self.stHabitaciones)
        self.actionAsignar = QtWidgets.QAction(VentanaHabitaciones)
        self.actionAsignar.setObjectName("actionAsignar")
        self.actionEstado = QtWidgets.QAction(VentanaHabitaciones)
        self.actionEstado.setObjectName("actionEstado")
        self.actionAcercaDe = QtWidgets.QAction(VentanaHabitaciones)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.actionSalir = QtWidgets.QAction(VentanaHabitaciones)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAsignaciones = QtWidgets.QAction(VentanaHabitaciones)
        self.actionAsignaciones.setObjectName("actionAsignaciones")
        self.actionSalir_2 = QtWidgets.QAction(VentanaHabitaciones)
        self.actionSalir_2.setObjectName("actionSalir_2")
        self.menuHabitaciones.addAction(self.actionAsignar)
        self.menuHabitaciones.addAction(self.actionEstado)
        self.menuHabitaciones.addAction(self.actionAsignaciones)
        self.menuHabitaciones.addSeparator()
        self.menuHabitaciones.addAction(self.actionSalir_2)
        self.menuInformacion.addAction(self.actionAcercaDe)
        self.mbHabitaciones.addAction(self.menuHabitaciones.menuAction())
        self.mbHabitaciones.addAction(self.menuInformacion.menuAction())

        self.retranslateUi(VentanaHabitaciones)
        self.tabHabitaciones.setCurrentIndex(0)
        self.btnLimpiar.clicked.connect(self.leCostoDia.clear)
        self.btnLimpiar.clicked.connect(self.dateEntrada.clear)
        self.btnLimpiar.clicked.connect(self.dateSalida.clear)
        self.btnLimpiar.clicked.connect(self.leHabitacion.clear)
        self.btnLimpiar.clicked.connect(self.leCI_RIF.clear)
        QtCore.QMetaObject.connectSlotsByName(VentanaHabitaciones)

    def retranslateUi(self, VentanaHabitaciones):
        _translate = QtCore.QCoreApplication.translate
        VentanaHabitaciones.setWindowTitle(_translate("VentanaHabitaciones", "MainWindow"))
        self.btnAsignar.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Asignar una habitacion a un cliente</p></body></html>"))
        self.btnEstado.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Ver el listado de las habitaciones</p></body></html>"))
        self.btnAsignaciones.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Ver lista de las asignaciones</p></body></html>"))
        self.lblCI_RIF.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Cedula o RIF del cliente</p></body></html>"))
        self.lblCI_RIF.setText(_translate("VentanaHabitaciones", "CI/RIF"))
        self.lblHabitacion.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Numero de la habitacion</p></body></html>"))
        self.lblHabitacion.setText(_translate("VentanaHabitaciones", "Habitacion"))
        self.lblEntrada.setWhatsThis(_translate("VentanaHabitaciones", "<html><head/><body><p>Fecha en la que se le asigna la habitacion</p></body></html>"))
        self.lblEntrada.setText(_translate("VentanaHabitaciones", "Fecha Entrada"))
        self.lblSalida.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Fecha de salida del cliente</p></body></html>"))
        self.lblSalida.setText(_translate("VentanaHabitaciones", "Fecha Salida"))
        self.lblCostoDia.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Costo del Dia</p></body></html>"))
        self.lblCostoDia.setText(_translate("VentanaHabitaciones", "Costo Dia"))
        self.btnAsignar_2.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Asigna una habitacion al cliente</p></body></html>"))
        self.btnLimpiar.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Borrar todo lo escrito</p></body></html>"))
        self.btnCerrar_Asignar.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>cierra la pestaña asignar</p></body></html>"))
        self.tabHabitaciones.setTabText(self.tabHabitaciones.indexOf(self.tabAsignar), _translate("VentanaHabitaciones", "Asignar"))
        self.lblGuardar.setText(_translate("VentanaHabitaciones", "Guardar"))
        self.cBGuardar.setItemText(0, _translate("VentanaHabitaciones", "..."))
        self.cBGuardar.setItemText(1, _translate("VentanaHabitaciones", "PDF"))
        self.cBGuardar.setItemText(2, _translate("VentanaHabitaciones", "CSV"))
        self.btnCerrar_Estado.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Cierra la lista de las habitaciones</p></body></html>"))
        self.btnRecargar_Estado.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Recargar la lista de las habitaciones</p></body></html>"))
        self.tabHabitaciones.setTabText(self.tabHabitaciones.indexOf(self.tabEstado), _translate("VentanaHabitaciones", "Estado"))
        self.btnEliminar.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Elimina una asignacion</p></body></html>"))
        self.btnRecargar.setToolTip(_translate("VentanaHabitaciones", "<html><head/><body><p>Actualiza la lista de las asignaciones</p></body></html>"))
        self.tabHabitaciones.setTabText(self.tabHabitaciones.indexOf(self.tabAsignaciones), _translate("VentanaHabitaciones", "Asignaciones"))
        self.menuHabitaciones.setTitle(_translate("VentanaHabitaciones", "Habitaciones"))
        self.menuInformacion.setTitle(_translate("VentanaHabitaciones", "Informacion"))
        self.actionAsignar.setText(_translate("VentanaHabitaciones", "Asignar"))
        self.actionEstado.setText(_translate("VentanaHabitaciones", "Estado"))
        self.actionAcercaDe.setText(_translate("VentanaHabitaciones", "AcercaDe"))
        self.actionSalir.setText(_translate("VentanaHabitaciones", "Salir"))
        self.actionAsignaciones.setText(_translate("VentanaHabitaciones", "Asignaciones"))
        self.actionSalir_2.setText(_translate("VentanaHabitaciones", "Salir"))

