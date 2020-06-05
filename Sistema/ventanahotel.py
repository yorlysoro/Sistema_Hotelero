# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QFileDialog
from ventanahotelwin import Ui_VentanaHotel
from PyQt5 import QtSql
from PyQt5.QtGui import QIcon
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, portrait
from reportlab.lib.enums import TA_CENTER
from acercaDe import AcercaDe
import time
import csv
class VentanaHotel(QMainWindow):
	def __init__(self, padre=None, db=None):
		QMainWindow.__init__(self, padre)
		self.ventanahotel = Ui_VentanaHotel()
		self.ventanahotel.setupUi(self)
		self.db = db
		self.ventanahotel.btnCuentas.clicked.connect(self.Cuentas)
		self.ventanahotel.btnClientes.clicked.connect(self.Clientes)
		self.EGIG = ""
		self.db.open()
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT COUNT(CI_RIF) FROM Clientes")
		cantClientesActual = 0
		while consulta.next():
			cantClientesActual = int(consulta.value(0))
		cantClientesAnt = 0
		consulta.exec_("SELECT Cantidad FROM CantClientes")
		while consulta.next():
			cantClientesAnt = int(consulta.value(0))
		FechaAnt = ""
		consulta.exec_("SELECT Fecha FROM CantClientes")
		while consulta.next():
			FechaAnt = consulta.value(0)
		FechaActual = time.strftime("%d/%m/%y")
		if FechaAnt == FechaActual:
			consulta.exec_("UPDATE CantClientes SET Cantidad = %d" %(cantClientesActual))
		else:
			consulta.exec_("INSERT INTO CantClientes (Fecha, Cantidad) VALUES('%s', %d)" %(FechaActual, cantClientesActual))
		self.ventanahotel.actionSalir.triggered.connect(self.close)
		self.ventanahotel.actionCuentas.triggered.connect(self.Cuentas)
		self.ventanahotel.actionClientes.triggered.connect(self.Clientes)
		self.ventanahotel.actionAcercaDe.triggered.connect(self.AcercaDe)
		self.setWindowTitle("Hotel")
		self.setWindowIcon(QIcon("Iconos/hotel.png"))
		self.ventanahotel.actionCuentas.setIcon(QIcon("Iconos/grafico.png"))
		self.ventanahotel.actionSalir.setIcon(QIcon("Iconos/cancelar.png"))
		self.ventanahotel.actionClientes.setIcon(QIcon("Iconos/grafico-circular.png"))
		self.ventanahotel.actionAcercaDe.setIcon(QIcon("Iconos/estrella.png"))
	def Cuentas(self):
		if not self.ventanahotel.tabCuentas.isVisible():
			self.ventanahotel.tabHotel.addTab(self.ventanahotel.tabCuentas, "Cuentas")
			self.ventanahotel.btnCerrar_Negocio.clicked.connect(self.cerrar_Cuentas)
			self.ventanahotel.cBIngresos.currentIndexChanged.connect(self.Ingresos)
			self.ventanahotel.cBGuardar.currentIndexChanged.connect(self.Guardar_Cuentas)
			self.ventanahotel.cBEgresos.currentIndexChanged.connect(self.Egresos)
			self.ventanahotel.tablaCuentas.setColumnCount(3)

	def Ingresos(self):
		tipo = self.ventanahotel.cBIngresos.currentText()
		dia = time.strftime("%d/%m/%y")
		mes = time.strftime("%m/%y")
		anio = time.strftime("/%y")
		self.EGIG = "Ingreso"
		self.ventanahotel.tablaCuentas.setHorizontalHeaderLabels(['N°', 'Fecha', self.EGIG])
		for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)
		if tipo == "Dia":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Ingresos WHERE Fecha BETWEEN'%s' and '%s'" % (dia, dia))
			row = 0
			for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaCuentas.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Ingreso = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaCuentas.setItem(row, 0, Numero)
				self.ventanahotel.tablaCuentas.setItem(row, 1, Fecha)
				self.ventanahotel.tablaCuentas.setItem(row, 2, Ingreso)

				row = row + 1
			self.db.close()
		elif tipo == "Mes":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Ingresos WHERE Fecha BETWEEN '%s' and '%s'" % ('1/'+mes,'31/'+mes))
			row = 0
			for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaCuentas.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Ingreso = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaCuentas.setItem(row, 0, Numero)
				self.ventanahotel.tablaCuentas.setItem(row, 1, Fecha)
				self.ventanahotel.tablaCuentas.setItem(row, 2, Ingreso)

				row = row + 1
			self.db.close()
		elif tipo == "Año":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Ingresos WHERE Fecha BETWEEN '%s' and '%s'" % ('1/1'+anio,'31/12'+anio))
			row = 0
			for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaCuentas.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Ingreso = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaCuentas.setItem(row, 0, Numero)
				self.ventanahotel.tablaCuentas.setItem(row, 1, Fecha)
				self.ventanahotel.tablaCuentas.setItem(row, 2, Ingreso)

				row = row + 1
			self.db.close()
		else:
			for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)
	def Guardar_Cuentas(self):
		tipo = self.ventanahotel.cBGuardar.currentText()
		row = self.ventanahotel.tablaCuentas.rowCount()
		if self.ventanahotel.tablaCuentas.item(0,0) != None:
			if tipo == "CSV":
				ruta_guardar = ""
				NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
				if NombreArchivo[0]:
					file = open(NombreArchivo[0]+'.csv', 'w')
					fieldnames = ["N°", "Fecha", self.EGIG ]
					csvsalida = csv.DictWriter(file, fieldnames)
					for i in range(row):
						csvsalida.writerow({fieldnames[0] : self.ventanahotel.tablaCuentas.item(i, 0).text(),
						fieldnames[1] : self.ventanahotel.tablaCuentas.item(i, 1).text(),
						fieldnames[2] : self.ventanahotel.tablaCuentas.item(i, 2).text()})
					file.close()
			elif tipo == "PDF":
				ruta_guardar = ""
				NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
				if NombreArchivo[0]:
					estiloHoja = getSampleStyleSheet()
					story = []
					cuerpo = estiloHoja["BodyText"]
					cuerpo.alignment=TA_CENTER

					col = ["N°", "Fecha", self.EGIG]
					fil = []
					fil.insert(0, col)
					filasTabla = 0
					for fila in range(row):
						fil.insert(fila+1, [self.ventanahotel.tablaCuentas.item(filasTabla, 0).text(), self.ventanahotel.tablaCuentas.item(filasTabla, 1).text(), self.ventanahotel.tablaCuentas.item(filasTabla, 2).text()])
						filasTabla += 1
					datos = [i for i in fil]
					tabla = Table(data=datos,colWidths=[20,60,60,60,60])
					story.append(tabla)
					doc = SimpleDocTemplate(NombreArchivo[0]+'.pdf',pagesize=portrait(LETTER), leftMargin=3, rightMargin=4, topMargin=3, bottomMargin=4)
					doc.build(story)
	def Egresos(self):
		tipo = self.ventanahotel.cBIngresos.currentText()
		dia = time.strftime("%d/%m/%y")
		mes = time.strftime("%m/%y")
		anio = time.strftime("/%y")
		self.EGIG = "Egreso"
		self.ventanahotel.tablaCuentas.setHorizontalHeaderLabels(['N°', 'Fecha', self.EGIG])
		for i in range(self.ventanahotel.tablaCuentas.rowCount()):
			self.ventanahotel.tablaCuentas.removeRow(i)
		if tipo == "Dia":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Egreso WHERE Fecha BETWEEN '%s' and '%s'" % (dia, dia))
			row = 0
			for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaCuentas.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Egreso = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaCuentas.setItem(row, 0, Numero)
				self.ventanahotel.tablaCuentas.setItem(row, 1, Fecha)
				self.ventanahotel.tablaCuentas.setItem(row, 2, Egreso)

				row = row + 1
			self.db.close()
		elif tipo == "Mes":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Egreso WHERE Fecha BETWEEN '%s' and '%s'" % ('1/'+mes,'31/'+mes))
			row = 0
			for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaCuentas.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Egreso = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaCuentas.setItem(row, 0, Numero)
				self.ventanahotel.tablaCuentas.setItem(row, 1, Fecha)
				self.ventanahotel.tablaCuentas.setItem(row, 2, Egreso)

				row = row + 1
			self.db.close()
		elif tipo == "Año":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Egreso WHERE Fecha BETWEEN '%s' and '%s'" % ('1/1'+anio,'31/12'+anio))
			row = 0
			for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaCuentas.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Egreso = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaCuentas.setItem(row, 0, Numero)
				self.ventanahotel.tablaCuentas.setItem(row, 1, Fecha)
				self.ventanahotel.tablaCuentas.setItem(row, 2, Egreso)

				row = row + 1
			self.db.close()
		else:
			for i in range(self.ventanahotel.tablaCuentas.rowCount()):
				self.ventanahotel.tablaCuentas.removeRow(i)

	def cerrar_Cuentas(self):
		index = self.ventanahotel.tabHotel.indexOf(self.ventanahotel.tabCuentas)
		self.ventanahotel.tabHotel.removeTab(index)
	def Clientes(self):
		if not self.ventanahotel.tabClientes.isVisible():
			self.ventanahotel.tabHotel.addTab(self.ventanahotel.tabClientes, "Clientes")
			self.ventanahotel.btnCerrar_Cliente.clicked.connect(self.cerrar_Clientes)
			self.ventanahotel.cBClientes.currentIndexChanged.connect(self.Ver_Clientes)
			self.ventanahotel.cBGuardar_2.currentIndexChanged.connect(self.Guardar_Clientes)
			for i in range(self.ventanahotel.tablaClientes.rowCount()):
				self.ventanahotel.tablaClientes.removeRow(i)
			self.ventanahotel.tablaClientes.setColumnCount(3)
			self.ventanahotel.tablaClientes.setHorizontalHeaderLabels(['N°', 'Fecha', 'Cantidad'])
	def Ver_Clientes(self):
		tipo = self.ventanahotel.cBClientes.currentText()
		dia = time.strftime("%d/%m/%y")
		mes = time.strftime("%m/%y")
		anio = time.strftime("/%y")
		for i in range(self.ventanahotel.tablaClientes.rowCount()):
			self.ventanahotel.tablaClientes.removeRow(i)
		if tipo == "Dia":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM CantClientes WHERE Fecha BETWEEN '%s' and '%s'" % (dia, dia))
			row = 0
			for i in range(self.ventanahotel.tablaClientes.rowCount()):
				self.ventanahotel.tablaClientes.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaClientes.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Cantidad = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaClientes.setItem(row, 0, Numero)
				self.ventanahotel.tablaClientes.setItem(row, 1, Fecha)
				self.ventanahotel.tablaClientes.setItem(row, 2, Cantidad)

				row = row + 1
			self.db.close()
		elif tipo == "Mes":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM CantClientes WHERE Fecha BETWEEN '%s' and '%s'" % ('1/'+mes, '31/'+mes))
			row = 0
			for i in range(self.ventanahotel.tablaClientes.rowCount()):
				self.ventanahotel.tablaClientes.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaClientes.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Cantidad = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaClientes.setItem(row, 0, Numero)
				self.ventanahotel.tablaClientes.setItem(row, 1, Fecha)
				self.ventanahotel.tablaClientes.setItem(row, 2, Cantidad)

				row = row + 1
			self.db.close()
		elif tipo == "Año":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM CantClientes WHERE Fecha BETWEEN '%s' and '%s'" % ('1/1'+anio,'31/12'+anio))
			row = 0
			for i in range(self.ventanahotel.tablaClientes.rowCount()):
				self.ventanahotel.tablaClientes.removeRow(i)
			while consulta.next():
				self.ventanahotel.tablaClientes.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				Fecha = QTableWidgetItem(str(consulta.value(1)))
				Cantidad = QTableWidgetItem(str(consulta.value(2)))

				self.ventanahotel.tablaClientes.setItem(row, 0, Numero)
				self.ventanahotel.tablaClientes.setItem(row, 1, Fecha)
				self.ventanahotel.tablaClientes.setItem(row, 2, Cantidad)

				row = row + 1
			self.db.close()
		else:
			for i in range(self.ventanahotel.tablaClientes.rowCount()):
				self.ventanahotel.tablaClientes.removeRow(i)
	def Guardar_Clientes(self):
		tipo = self.ventanahotel.cBGuardar_2.currentText()
		row = self.ventanahotel.tablaClientes.rowCount()
		if self.ventanahotel.tablaClientes.item(0,0) != None:
			if tipo == "CSV":
				ruta_guardar = ""
				NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
				if NombreArchivo[0]:
					file = open(NombreArchivo[0]+'.csv', 'w')
					fieldnames = ["N°", "Fecha", "Cantidad" ]
					csvsalida = csv.DictWriter(file, fieldnames)
					for i in range(row):
						csvsalida.writerow({fieldnames[0] : self.ventanahotel.tablaClientess.item(i, 0).text(),
						fieldnames[1] : self.ventanahotel.tablaClientes.item(i, 1).text(),
						fieldnames[2] : self.ventanahotel.tablaClientes.item(i, 2).text()})
				file.close()
			elif tipo == "PDF":
				ruta_guardar = ""
				NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
				if NombreArchivo[0]:
					estiloHoja = getSampleStyleSheet()
					story = []
					cuerpo = estiloHoja["BodyText"]
					cuerpo.alignment=TA_CENTER

					col = ["N°", "Fecha", 'Cantidad']
					fil = []
					fil.insert(0, col)
					filasTabla = 0
					for fila in range(row):
						fil.insert(fila+1, [self.ventanahotel.tablaClientes.item(filasTabla, 0).text(), self.ventanahotel.tablaClientes.item(filasTabla, 1).text(), self.ventanahotel.tablaClientes.item(filasTabla, 2).text()])
						filasTabla += 1
					datos = [i for i in fil]
					tabla = Table(data=datos,colWidths=[20,60,60,60,60])
					story.append(tabla)
					doc = SimpleDocTemplate(NombreArchivo[0]+'.pdf',pagesize=portrait(LETTER), leftMargin=3, rightMargin=4, topMargin=3, bottomMargin=4)
					doc.build(story)
	def cerrar_Clientes(self):
		index = self.ventanahotel.tabHotel.indexOf(self.ventanahotel.tabClientes)
		self.ventanahotel.tabHotel.removeTab(index)
		
	def AcercaDe(self):
		acerca = AcercaDe(self)
		acerca.show()
#app = QApplication([])
#window = VentanaHotel(None)
#window.show()
#app.exec__()
