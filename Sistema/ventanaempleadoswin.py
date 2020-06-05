# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaempleadoswin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaEmpleados(object):
    def setupUi(self, VentanaEmpleados):
        VentanaEmpleados.setObjectName("VentanaEmpleados")
        VentanaEmpleados.resize(1086, 600)
        VentanaEmpleados.setStyleSheet("QPushButton#btnAgregar {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/usuario.png\");\n"
"}\n"
"\n"
"QPushButton#btnTurnos {\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-family: \'Roboto\';\n"
"        font-size: 25px;\n"
"        image: url(\"../Iconos/turnos.png\");\n"
"}\n"
"\n"
"QPushButton#btnLista {\n"
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
"QPushButton#btnTurnos:hover {\n"
"        background-color: #D3F9F8;\n"
"}\n"
"\n"
"QPushButton#btnLista:hover {\n"
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
"QPushButton#btnCerrar_Turnos {\n"
"    border-radius: 15px;\n"
"    font-family: \'Roboto\';\n"
"    font-size: 25px;\n"
"    image: url(\"../Iconos/cancelar.png\");\n"
"}\n"
"QPushButton#btnCerrar_Turnos:hover {\n"
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
" border-size: 15px;\n"
" background-color: #009688;\n"
"}\n"
"\n"
"QToolBox {\n"
"    border-size: 15px;\n"
"     background-color: #009688;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(VentanaEmpleados)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btnLista = QtWidgets.QPushButton(self.groupBox)
        self.btnLista.setText("")
        self.btnLista.setObjectName("btnLista")
        self.gridLayout.addWidget(self.btnLista, 0, 2, 1, 1)
        self.btnAgregar = QtWidgets.QPushButton(self.groupBox)
        self.btnAgregar.setText("")
        self.btnAgregar.setObjectName("btnAgregar")
        self.gridLayout.addWidget(self.btnAgregar, 0, 0, 1, 1)
        self.btnTurnos = QtWidgets.QPushButton(self.groupBox)
        self.btnTurnos.setText("")
        self.btnTurnos.setObjectName("btnTurnos")
        self.gridLayout.addWidget(self.btnTurnos, 0, 1, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.tabEmpleados = QtWidgets.QTabWidget(self.centralwidget)
        self.tabEmpleados.setObjectName("tabEmpleados")
        self.tabAgregar = QtWidgets.QWidget()
        self.tabAgregar.setObjectName("tabAgregar")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tabAgregar)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tabAgregar)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.leCI_RIF = QtWidgets.QLineEdit(self.tabAgregar)
        self.leCI_RIF.setObjectName("leCI_RIF")
        self.gridLayout_2.addWidget(self.leCI_RIF, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tabAgregar)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.leNombre = QtWidgets.QLineEdit(self.tabAgregar)
        self.leNombre.setObjectName("leNombre")
        self.gridLayout_2.addWidget(self.leNombre, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tabAgregar)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.leApellido = QtWidgets.QLineEdit(self.tabAgregar)
        self.leApellido.setObjectName("leApellido")
        self.gridLayout_2.addWidget(self.leApellido, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tabAgregar)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.leCorreo = QtWidgets.QLineEdit(self.tabAgregar)
        self.leCorreo.setObjectName("leCorreo")
        self.gridLayout_2.addWidget(self.leCorreo, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tabAgregar)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.leTelefono = QtWidgets.QLineEdit(self.tabAgregar)
        self.leTelefono.setObjectName("leTelefono")
        self.gridLayout_2.addWidget(self.leTelefono, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tabAgregar)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.teDireccion = QtWidgets.QTextEdit(self.tabAgregar)
        self.teDireccion.setObjectName("teDireccion")
        self.gridLayout_2.addWidget(self.teDireccion, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tabAgregar)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.leSueldo = QtWidgets.QLineEdit(self.tabAgregar)
        self.leSueldo.setObjectName("leSueldo")
        self.gridLayout_2.addWidget(self.leSueldo, 6, 1, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnAgregar_2 = QtWidgets.QPushButton(self.tabAgregar)
        self.btnAgregar_2.setText("")
        self.btnAgregar_2.setObjectName("btnAgregar_2")
        self.gridLayout_3.addWidget(self.btnAgregar_2, 0, 0, 1, 1)
        self.btnLimpiar = QtWidgets.QPushButton(self.tabAgregar)
        self.btnLimpiar.setText("")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.gridLayout_3.addWidget(self.btnLimpiar, 0, 1, 1, 1)
        self.btnCerrar_Agregar = QtWidgets.QPushButton(self.tabAgregar)
        self.btnCerrar_Agregar.setText("")
        self.btnCerrar_Agregar.setObjectName("btnCerrar_Agregar")
        self.gridLayout_3.addWidget(self.btnCerrar_Agregar, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.tabEmpleados.addTab(self.tabAgregar, "")
        self.tabTurnos = QtWidgets.QWidget()
        self.tabTurnos.setObjectName("tabTurnos")
        self.tablaTurnos = QtWidgets.QTableWidget(self.tabTurnos)
        self.tablaTurnos.setGeometry(QtCore.QRect(280, 10, 771, 421))
        self.tablaTurnos.setObjectName("tablaTurnos")
        self.tablaTurnos.setColumnCount(0)
        self.tablaTurnos.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(self.tabTurnos)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 256, 356))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.tbTurnos = QtWidgets.QToolBox(self.layoutWidget)
        self.tbTurnos.setObjectName("tbTurnos")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 104, 45))
        self.page.setObjectName("page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.cbTodos = QtWidgets.QComboBox(self.page)
        self.cbTodos.setObjectName("cbTodos")
        self.cbTodos.addItem("")
        self.cbTodos.addItem("")
        self.cbTodos.addItem("")
        self.cbTodos.addItem("")
        self.gridLayout_5.addWidget(self.cbTodos, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.tbTurnos.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 290, 86))
        self.page_2.setObjectName("page_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 2)
        self.leCI_RIF_2 = QtWidgets.QLineEdit(self.page_2)
        self.leCI_RIF_2.setObjectName("leCI_RIF_2")
        self.gridLayout_7.addWidget(self.leCI_RIF_2, 0, 2, 1, 2)
        self.cbEmpleados = QtWidgets.QComboBox(self.page_2)
        self.cbEmpleados.setObjectName("cbEmpleados")
        self.cbEmpleados.addItem("")
        self.cbEmpleados.addItem("")
        self.cbEmpleados.addItem("")
        self.cbEmpleados.addItem("")
        self.gridLayout_7.addWidget(self.cbEmpleados, 1, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 1, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.tbTurnos.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 254, 186))
        self.page_3.setObjectName("page_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)
        self.leCI_RIF_3 = QtWidgets.QLineEdit(self.page_3)
        self.leCI_RIF_3.setObjectName("leCI_RIF_3")
        self.gridLayout_10.addWidget(self.leCI_RIF_3, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_10.addWidget(self.label_11, 1, 0, 1, 1)
        self.dateFecha = QtWidgets.QDateEdit(self.page_3)
        self.dateFecha.setObjectName("dateFecha")
        self.gridLayout_10.addWidget(self.dateFecha, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 2, 0, 1, 1)
        self.timeInicio = QtWidgets.QTimeEdit(self.page_3)
        self.timeInicio.setObjectName("timeInicio")
        self.gridLayout_10.addWidget(self.timeInicio, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 3, 0, 1, 1)
        self.timeFin = QtWidgets.QTimeEdit(self.page_3)
        self.timeFin.setObjectName("timeFin")
        self.gridLayout_10.addWidget(self.timeFin, 3, 1, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 0, 0, 1, 1)
        self.btnAsignar = QtWidgets.QPushButton(self.page_3)
        self.btnAsignar.setText("")
        self.btnAsignar.setObjectName("btnAsignar")
        self.gridLayout_9.addWidget(self.btnAsignar, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem6, 0, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 4, 0, 1, 2)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.tbTurnos.addItem(self.page_3, "")
        self.gridLayout_27.addWidget(self.tbTurnos, 0, 0, 1, 1)
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem7, 0, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_12.addWidget(self.label_14, 0, 0, 1, 1)
        self.cbGuardar = QtWidgets.QComboBox(self.layoutWidget)
        self.cbGuardar.setObjectName("cbGuardar")
        self.cbGuardar.addItem("")
        self.cbGuardar.addItem("")
        self.cbGuardar.addItem("")
        self.gridLayout_12.addWidget(self.cbGuardar, 0, 1, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_12, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem8, 0, 2, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_25, 0, 0, 1, 1)
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem9, 0, 0, 1, 1)
        self.btnCerrar_Turnos = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCerrar_Turnos.setText("")
        self.btnCerrar_Turnos.setObjectName("btnCerrar_Turnos")
        self.gridLayout_24.addWidget(self.btnCerrar_Turnos, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem10, 0, 2, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_24, 1, 0, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_26, 1, 0, 1, 1)
        self.tabEmpleados.addTab(self.tabTurnos, "")
        self.tabLista = QtWidgets.QWidget()
        self.tabLista.setObjectName("tabLista")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tabLista)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.leBuscar_Lista = QtWidgets.QLineEdit(self.tabLista)
        self.leBuscar_Lista.setObjectName("leBuscar_Lista")
        self.gridLayout_20.addWidget(self.leBuscar_Lista, 0, 0, 1, 1)
        self.tablaLista = QtWidgets.QTableWidget(self.tabLista)
        self.tablaLista.setObjectName("tablaLista")
        self.tablaLista.setColumnCount(0)
        self.tablaLista.setRowCount(0)
        self.gridLayout_20.addWidget(self.tablaLista, 1, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem11, 0, 0, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.btnRecargar = QtWidgets.QPushButton(self.tabLista)
        self.btnRecargar.setText("")
        self.btnRecargar.setObjectName("btnRecargar")
        self.gridLayout_18.addWidget(self.btnRecargar, 0, 1, 1, 1)
        self.btnCerrar_Lista = QtWidgets.QPushButton(self.tabLista)
        self.btnCerrar_Lista.setText("")
        self.btnCerrar_Lista.setObjectName("btnCerrar_Lista")
        self.gridLayout_18.addWidget(self.btnCerrar_Lista, 0, 2, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(self.tabLista)
        self.btnEliminar.setText("")
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout_18.addWidget(self.btnEliminar, 0, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem12, 0, 2, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_19, 1, 0, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem13, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tabLista)
        self.label_15.setObjectName("label_15")
        self.gridLayout_21.addWidget(self.label_15, 0, 1, 1, 1)
        self.cbGuardar_Lista = QtWidgets.QComboBox(self.tabLista)
        self.cbGuardar_Lista.setObjectName("cbGuardar_Lista")
        self.cbGuardar_Lista.addItem("")
        self.cbGuardar_Lista.addItem("")
        self.cbGuardar_Lista.addItem("")
        self.gridLayout_21.addWidget(self.cbGuardar_Lista, 0, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem14, 0, 3, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_21, 2, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_22, 0, 0, 1, 1)
        self.tabEmpleados.addTab(self.tabLista, "")
        self.gridLayout_14.addWidget(self.tabEmpleados, 1, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        VentanaEmpleados.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaEmpleados)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 22))
        self.menubar.setObjectName("menubar")
        self.menuInformacion = QtWidgets.QMenu(self.menubar)
        self.menuInformacion.setObjectName("menuInformacion")
        self.menuInformacion_2 = QtWidgets.QMenu(self.menubar)
        self.menuInformacion_2.setObjectName("menuInformacion_2")
        VentanaEmpleados.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaEmpleados)
        self.statusbar.setObjectName("statusbar")
        VentanaEmpleados.setStatusBar(self.statusbar)
        self.actionAgregar = QtWidgets.QAction(VentanaEmpleados)
        self.actionAgregar.setObjectName("actionAgregar")
        self.actionTurnos = QtWidgets.QAction(VentanaEmpleados)
        self.actionTurnos.setObjectName("actionTurnos")
        self.actionLista = QtWidgets.QAction(VentanaEmpleados)
        self.actionLista.setObjectName("actionLista")
        self.actionSalir = QtWidgets.QAction(VentanaEmpleados)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcercaDe = QtWidgets.QAction(VentanaEmpleados)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.menuInformacion.addAction(self.actionAgregar)
        self.menuInformacion.addAction(self.actionTurnos)
        self.menuInformacion.addAction(self.actionLista)
        self.menuInformacion.addSeparator()
        self.menuInformacion.addAction(self.actionSalir)
        self.menuInformacion_2.addAction(self.actionAcercaDe)
        self.menubar.addAction(self.menuInformacion.menuAction())
        self.menubar.addAction(self.menuInformacion_2.menuAction())

        self.retranslateUi(VentanaEmpleados)
        self.tabEmpleados.setCurrentIndex(1)
        self.tbTurnos.setCurrentIndex(2)
        self.btnLimpiar.clicked.connect(self.leSueldo.clear)
        self.btnLimpiar.clicked.connect(self.teDireccion.clear)
        self.btnLimpiar.clicked.connect(self.leTelefono.clear)
        self.btnLimpiar.clicked.connect(self.leCorreo.clear)
        self.btnLimpiar.clicked.connect(self.leApellido.clear)
        self.btnLimpiar.clicked.connect(self.leNombre.clear)
        self.btnLimpiar.clicked.connect(self.leCI_RIF.clear)
        QtCore.QMetaObject.connectSlotsByName(VentanaEmpleados)

    def retranslateUi(self, VentanaEmpleados):
        _translate = QtCore.QCoreApplication.translate
        VentanaEmpleados.setWindowTitle(_translate("VentanaEmpleados", "MainWindow"))
        self.btnLista.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>Listar toda la informacion sobre los empleados</p></body></html>"))
        self.btnAgregar.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>Agregar un nuevo empleado</p><p><br/></p></body></html>"))
        self.btnTurnos.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>Asignar o listar turnos</p></body></html>"))
        self.label.setText(_translate("VentanaEmpleados", "CI/RIF"))
        self.label_2.setText(_translate("VentanaEmpleados", "Nombre"))
        self.label_3.setText(_translate("VentanaEmpleados", "Apellido"))
        self.label_4.setText(_translate("VentanaEmpleados", "Correo"))
        self.label_5.setText(_translate("VentanaEmpleados", "Telefono"))
        self.label_6.setText(_translate("VentanaEmpleados", "Direccion"))
        self.label_7.setText(_translate("VentanaEmpleados", "Sueldo"))
        self.btnAgregar_2.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>Agregar al nuevo empleado</p></body></html>"))
        self.btnLimpiar.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>borrar todo lo escrito</p></body></html>"))
        self.btnCerrar_Agregar.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>cerrar esta pestaña</p></body></html>"))
        self.tabEmpleados.setTabText(self.tabEmpleados.indexOf(self.tabAgregar), _translate("VentanaEmpleados", "Agregar"))
        self.label_9.setText(_translate("VentanaEmpleados", "Por"))
        self.cbTodos.setItemText(0, _translate("VentanaEmpleados", "..."))
        self.cbTodos.setItemText(1, _translate("VentanaEmpleados", "Dia"))
        self.cbTodos.setItemText(2, _translate("VentanaEmpleados", "Mes"))
        self.cbTodos.setItemText(3, _translate("VentanaEmpleados", "Año"))
        self.tbTurnos.setItemText(self.tbTurnos.indexOf(self.page), _translate("VentanaEmpleados", "Todos"))
        self.label_8.setText(_translate("VentanaEmpleados", "CI/RIF"))
        self.cbEmpleados.setItemText(0, _translate("VentanaEmpleados", "..."))
        self.cbEmpleados.setItemText(1, _translate("VentanaEmpleados", "Dia"))
        self.cbEmpleados.setItemText(2, _translate("VentanaEmpleados", "Mes"))
        self.cbEmpleados.setItemText(3, _translate("VentanaEmpleados", "Año"))
        self.label_16.setText(_translate("VentanaEmpleados", "Por"))
        self.tbTurnos.setItemText(self.tbTurnos.indexOf(self.page_2), _translate("VentanaEmpleados", "Por Empleados"))
        self.label_10.setText(_translate("VentanaEmpleados", "CI/RIF"))
        self.label_11.setText(_translate("VentanaEmpleados", "Fecha"))
        self.label_12.setText(_translate("VentanaEmpleados", "Inicio"))
        self.label_13.setText(_translate("VentanaEmpleados", "Fin"))
        self.btnAsignar.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>Asignar un turno</p></body></html>"))
        self.tbTurnos.setItemText(self.tbTurnos.indexOf(self.page_3), _translate("VentanaEmpleados", "Asignar"))
        self.label_14.setText(_translate("VentanaEmpleados", "Guardar"))
        self.cbGuardar.setItemText(0, _translate("VentanaEmpleados", "..."))
        self.cbGuardar.setItemText(1, _translate("VentanaEmpleados", "CSV"))
        self.cbGuardar.setItemText(2, _translate("VentanaEmpleados", "PDF"))
        self.btnCerrar_Turnos.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>cierra la pestaña turnos</p><p><br/></p></body></html>"))
        self.tabEmpleados.setTabText(self.tabEmpleados.indexOf(self.tabTurnos), _translate("VentanaEmpleados", "Turnos"))
        self.btnRecargar.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>Actualizar la lista</p></body></html>"))
        self.btnCerrar_Lista.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>Cerrar la pestaña lista</p></body></html>"))
        self.btnEliminar.setToolTip(_translate("VentanaEmpleados", "<html><head/><body><p>Eliminar un empleado</p></body></html>"))
        self.label_15.setText(_translate("VentanaEmpleados", "Guardar"))
        self.cbGuardar_Lista.setItemText(0, _translate("VentanaEmpleados", "..."))
        self.cbGuardar_Lista.setItemText(1, _translate("VentanaEmpleados", "CSV"))
        self.cbGuardar_Lista.setItemText(2, _translate("VentanaEmpleados", "PDF"))
        self.tabEmpleados.setTabText(self.tabEmpleados.indexOf(self.tabLista), _translate("VentanaEmpleados", "Lista"))
        self.menuInformacion.setTitle(_translate("VentanaEmpleados", "Empleados"))
        self.menuInformacion_2.setTitle(_translate("VentanaEmpleados", "Informacion"))
        self.actionAgregar.setText(_translate("VentanaEmpleados", "Agregar"))
        self.actionTurnos.setText(_translate("VentanaEmpleados", "Turnos"))
        self.actionLista.setText(_translate("VentanaEmpleados", "Lista"))
        self.actionSalir.setText(_translate("VentanaEmpleados", "Salir"))
        self.actionAcercaDe.setText(_translate("VentanaEmpleados", "AcercaDe"))

