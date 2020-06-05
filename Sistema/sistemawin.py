# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistemawin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sistemawin(object):
    def setupUi(self, sistemawin):
        sistemawin.setObjectName("sistemawin")
        sistemawin.resize(447, 187)
        sistemawin.setStyleSheet("QPushButton#btnClientes {\n"
"    border-style: inset;\n"
"    border-radius: 15px;\n"
"    image: url(\"../Iconos/grupo-ico.png\")\n"
"}\n"
"QPushButton#btnEmpleados {\n"
"    border-radius: 15px;\n"
"    image: url(\"../Iconos/empleados-ico.png\")\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border-radius: 15px;\n"
"    background-color: #A0D8D2;\n"
"    font-family: \'Roboto\';\n"
"}\n"
"QPushButton#btnHabitaciones {\n"
"    border-radius: 15px;\n"
"    image: url(\"../Iconos/habitaciones-ico.png\")\n"
"}\n"
"\n"
"QPushButton#btnHotel {\n"
"    border-radius: 15px;\n"
"    image: url(\"../Iconos/hotel.png\")\n"
"}\n"
"\n"
"QPushButton#btnCLientes:hover{\n"
"    backgroun-color: #30FDFB\n"
"}\n"
"\n"
"QPushButton#btnHabitaciones:hover{\n"
"    backgroun-color: #30FDFB\n"
"}\n"
"\n"
"QPushButton#btnEmplados:hover{\n"
"    backgroun-color: #30FDFB\n"
"}\n"
"\n"
"QPushButton#btnHotel:hover{\n"
"    backgroun-color: #30FDFB\n"
"}\n"
"\n"
"QMainWindow {\n"
"        background-color: #009688;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    borde-radius: 15px;\n"
"    background-color:grey;\n"
"}\n"
"QAction {\n"
"    background-color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(sistemawin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gbSistema = QtWidgets.QGroupBox(self.centralwidget)
        self.gbSistema.setObjectName("gbSistema")
        self.btnClientes = QtWidgets.QPushButton(self.gbSistema)
        self.btnClientes.setGeometry(QtCore.QRect(20, 30, 91, 71))
        self.btnClientes.setText("")
        self.btnClientes.setObjectName("btnClientes")
        self.btnEmpleados = QtWidgets.QPushButton(self.gbSistema)
        self.btnEmpleados.setGeometry(QtCore.QRect(120, 30, 91, 71))
        self.btnEmpleados.setText("")
        self.btnEmpleados.setObjectName("btnEmpleados")
        self.btnHabitaciones = QtWidgets.QPushButton(self.gbSistema)
        self.btnHabitaciones.setGeometry(QtCore.QRect(220, 30, 91, 71))
        self.btnHabitaciones.setText("")
        self.btnHabitaciones.setObjectName("btnHabitaciones")
        self.btnHotel = QtWidgets.QPushButton(self.gbSistema)
        self.btnHotel.setGeometry(QtCore.QRect(320, 30, 91, 71))
        self.btnHotel.setText("")
        self.btnHotel.setObjectName("btnHotel")
        self.gridLayout_3.addWidget(self.gbSistema, 0, 0, 1, 1)
        sistemawin.setCentralWidget(self.centralwidget)
        self.sbSistema = QtWidgets.QStatusBar(sistemawin)
        self.sbSistema.setObjectName("sbSistema")
        sistemawin.setStatusBar(self.sbSistema)
        self.mbSistema = QtWidgets.QMenuBar(sistemawin)
        self.mbSistema.setGeometry(QtCore.QRect(0, 0, 447, 22))
        self.mbSistema.setObjectName("mbSistema")
        self.menuInformacion = QtWidgets.QMenu(self.mbSistema)
        self.menuInformacion.setObjectName("menuInformacion")
        sistemawin.setMenuBar(self.mbSistema)
        self.actionAbrir = QtWidgets.QAction(sistemawin)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(sistemawin)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(sistemawin)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionPDF = QtWidgets.QAction(sistemawin)
        self.actionPDF.setObjectName("actionPDF")
        self.actionCSV = QtWidgets.QAction(sistemawin)
        self.actionCSV.setObjectName("actionCSV")
        self.actionSalir = QtWidgets.QAction(sistemawin)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCopiar = QtWidgets.QAction(sistemawin)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionCortar = QtWidgets.QAction(sistemawin)
        self.actionCortar.setObjectName("actionCortar")
        self.actionPegar = QtWidgets.QAction(sistemawin)
        self.actionPegar.setObjectName("actionPegar")
        self.actionAcerca_De = QtWidgets.QAction(sistemawin)
        self.actionAcerca_De.setObjectName("actionAcerca_De")
        self.actionAcercaDe = QtWidgets.QAction(sistemawin)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.menuInformacion.addAction(self.actionAcercaDe)
        self.mbSistema.addAction(self.menuInformacion.menuAction())

        self.retranslateUi(sistemawin)
        QtCore.QMetaObject.connectSlotsByName(sistemawin)

    def retranslateUi(self, sistemawin):
        _translate = QtCore.QCoreApplication.translate
        sistemawin.setWindowTitle(_translate("sistemawin", "Hotel"))
        self.gbSistema.setTitle(_translate("sistemawin", "Hotel"))
        self.btnClientes.setToolTip(_translate("sistemawin", "<html><head/><body><p>Clientes</p></body></html>"))
        self.btnEmpleados.setToolTip(_translate("sistemawin", "<html><head/><body><p>Empleados</p></body></html>"))
        self.btnHabitaciones.setToolTip(_translate("sistemawin", "<html><head/><body><p>Habitaciones</p></body></html>"))
        self.btnHotel.setToolTip(_translate("sistemawin", "<html><head/><body><p>Hotel</p></body></html>"))
        self.menuInformacion.setTitle(_translate("sistemawin", "Información"))
        self.actionAbrir.setText(_translate("sistemawin", "Abrir"))
        self.actionGuardar.setText(_translate("sistemawin", "Guardar"))
        self.actionGuardar_Como.setText(_translate("sistemawin", "Guardar Como"))
        self.actionPDF.setText(_translate("sistemawin", "PDF"))
        self.actionCSV.setText(_translate("sistemawin", "CSV"))
        self.actionSalir.setText(_translate("sistemawin", "Salir"))
        self.actionCopiar.setText(_translate("sistemawin", "Copiar"))
        self.actionCortar.setText(_translate("sistemawin", "Cortar"))
        self.actionPegar.setText(_translate("sistemawin", "Pegar"))
        self.actionAcerca_De.setText(_translate("sistemawin", "Acerca De"))
        self.actionAcercaDe.setText(_translate("sistemawin", "AcercaDe"))

