# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QFileDialog
from ventanahabitacioneswin import Ui_VentanaHabitaciones
from Validaciones import Validaciones
from PyQt5 import QtSql, QtCore
from PyQt5.QtGui import QIcon, QPixmap
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, portrait
from reportlab.lib.enums import TA_CENTER
from acercaDe import AcercaDe
import time
import csv
class VentanaHabitaciones(QMainWindow):
	def __init__(self, padre=None, db=None):
		QMainWindow.__init__(self,padre)
		self.ventanahabitaciones = Ui_VentanaHabitaciones()
		self.ventanahabitaciones.setupUi(self)
		self.validacion = Validaciones(self.ventanahabitaciones)
		self.db = db
		self.ventanahabitaciones.btnAsignar.clicked.connect(self.Asignar)
		self.ventanahabitaciones.btnEstado.clicked.connect(self.Estado)
		self.ventanahabitaciones.btnAsignaciones.clicked.connect(self.Asignaciones)
		self.ventanahabitaciones.actionAcercaDe.triggered.connect(self.close)
		self.ventanahabitaciones.actionAsignaciones.triggered.connect(self.Asignaciones)
		self.ventanahabitaciones.actionAsignar.triggered.connect(self.Asignar)
		self.ventanahabitaciones.actionEstado.triggered.connect(self.Estado)
		self.ventanahabitaciones.actionAcercaDe.triggered.connect(self.AcercaDe)
		self.setWindowTitle("Habitaciones")
		self.setWindowIcon(QIcon("Iconos/habitaciones-ico.png"))
		self.ventanahabitaciones.actionAcercaDe.setIcon(QIcon("Iconos/estrella.png"))
		self.ventanahabitaciones.actionAsignar.setIcon(QIcon("Iconos/mas.png"))
		self.ventanahabitaciones.actionEstado.setIcon(QIcon("Iconos/lista.png"))
		self.ventanahabitaciones.actionAsignaciones.setIcon(QIcon("Iconos/lista2.png"))
		self.ventanahabitaciones.actionSalir.triggered.connect(self.close)
		self.ventanahabitaciones.actionSalir.setIcon(QIcon("Iconos/cancelar.png"))
		self.setFixedSize(447, 187)
	def Asignar(self):
		if not self.ventanahabitaciones.tabAsignar.isVisible():
			self.ventanahabitaciones.tabHabitaciones.addTab(self.ventanahabitaciones.tabAsignar, "Asignar")
			self.ventanahabitaciones.leCI_RIF.textChanged.connect(self.validacion.validar_cedula)
			self.ventanahabitaciones.leHabitacion.textChanged.connect(self.validacion.validar_habitacion)
			self.ventanahabitaciones.leCostoDia.textChanged.connect(self.validacion.validar_costo)
			self.ventanahabitaciones.btnAsignar_2.clicked.connect(self.AsignarBtn)
			self.ventanahabitaciones.btnCerrar_Asignar.clicked.connect(self.cerrarAsignar)

	def AsignarBtn(self):
		self.db.open()
		consulta = QtSql.QSqlQuery()
		cedula = self.ventanahabitaciones.leCI_RIF.text()
		ci = ""
		Habitacion = self.ventanahabitaciones.leHabitacion.text()
		Entrada = self.ventanahabitaciones.dateEntrada.text()
		Salida = self.ventanahabitaciones.dateSalida.text()
		consulta.exec_("SELECT Fecha_Salida FROM AsignarHabitaciones WHERE CI_RIF = '%s" %(cedula))
		FechaAsignada = ""
		capacidad = ""
		asignado = ""
		HabitacionAsignada = ""
		while consulta.next():
			FechaAsignada = consulta.value(0)
		consulta.exec_("SELECT Capacidad, Asignado FROM Habitaciones WHERE Numero_Codigo = '%s'" %(Habitacion))
		while consulta.next():
			capacidad = consulta.value(0)
			asignado = consulta.value(1)
		consulta.exec_("SELECT Habitacion FROM AsignarHabitaciones WHERE CI_RIF = %s" %(cedula))
		while consulta.next():
			HabitacionAsignada = consulta.value(0)
		CI = ""
		consulta.exec_("SELECT CI_RIF From AsignarHabitaciones WHERE CI_RIF = '%s'" %(cedula))
		while consulta.next():
			CI = consulta.value(0)
		
		if Salida < Entrada:
			QMessageBox.warning(self, "Error", "Error al asignar las fechas", QMessageBox.Ok)
		elif Entrada == Salida:
			QMessageBox.warning(self, "Error", "Las fechas no pueden ser iguales", QMessageBox.Ok)
		elif Salida < FechaAsignada:
			QMessageBox.warning(self, "Error", "Aun tiene una asignacion activa", QMessageBox.Ok)
		elif capacidad == asignado and capacidad != "" and asignado != "":
			QMessageBox.warning(self, "Error", "La habitacion a alcanzado su limite", QMessageBox.Ok)
		elif FechaAsignada < Salida and Habitacion != HabitacionAsignada and HabitacionAsignada != "" and Habitacion != "" and FechaAsignada != "" and Salida != "":
			QMessageBox.warning(self, "Error", "No puede asignar dos habitaciones al mismo cliente", QMessageBox.Ok)
		elif FechaAsignada == Salida or Habitacion == HabitacionAsignada:
			QMessageBox.warning(self, "Error", "Ya el cliente tiene la habitacion asignada", QMessageBox.Ok)
		elif CI == cedula:
			QMessageBox.warning(self, "Error", "Ya el cliente tiene una habitacion asignada", QMessageBox.Ok)
		elif not self.validacion.validar_cedula() and not self.validacion.validar_costo() and not self.validacion.validar_habitacion():
			QMessageBox.warning(self, "Error", "No ha llenado ningun campo", QMessageBox.Ok)
		elif not self.validacion.validar_cedula():
			QMessageBox.warning(self, "Error", "No ha introducido la cedula", QMessageBox.Ok)
		elif not self.validacion.validar_habitacion():
			QMessageBox.warning(self, "Error", "No ha introducido la habitacion", QMessageBox.Ok)
		elif not self.validacion.validar_costo():
			QMessageBox.warning(self, "Error", "No ha introducido el costo", QMessageBox.Ok)
		else:
			CostoDia = float(self.ventanahabitaciones.leCostoDia.text())
			consulta.exec__("SELECT CI_RIF FROM Clientes WHERE CI_RIF = '%s'" %(cedula))
			while consulta.next():
				ci = consulta.value(0)
			if ci == "":
				QMessageBox.warning(self, "Error", "El cliente aun no esta registrado", QMessageBox.Ok)
			else:
				listd = Salida.split('/')
				listd2 = Entrada.split('/')
				Dias = int(listd[0]) - int(listd2[0])
				Total = CostoDia * Dias
				fecha = time.strftime("%d/%m/%y")
				anioactual = time.strftime("%y")
				if listd[2] and listd2[2] == anioactual or listd[2] == anioactual:
					consulta.exec__("INSERT INTO AsignarHabitaciones (CI_RIF, Habitacion, Fecha_Entrada, Fecha_Salida, Costo_Dia, Total) VALUES( '%s', '%s', '%s', '%s', '%f', '%f')" %(cedula, Habitacion, Entrada, Salida, CostoDia, Total))
					consulta.exec__("INSERT INTO Ingresos (Fecha, Ingreso) VALUES('%s', '%f')" %(fecha, Total))
					consulta.exec__("SELECT Estado FROM Habitaciones WHERE Numero_Codigo = '%s'" %(Habitacion))
					Estado = ""
					while consulta.next():
						Estado = consulta.value(0)
					if Estado == "Desocupada":
						consulta.exec_("UPDATE Habitaciones SET Estado = 'Ocupada' WHERE Numero_Codigo = '%s'" %(Habitacion))
						consulta.exec_("SELECT Asignado FROM Habitaciones WHERE Numero_Codigo = '%s'" %(Habitacion))
						Asignado = 0
						while consulta.next():
							Asignado = int(consulta.value(0))
						Asignado += 1
						consulta.exec_("UPDATE Habitaciones SET Asignado = %d WHERE Numero_Codigo = '%s'" %(Asignado, Habitacion))
					else:
						consulta.exec_("SELECT Asignado FROM Habitaciones WHERE Numero_Codigo = '%s'" %(Habitacion))
						Asignado = 0
						while consulta.next():
							Asignado = int(consulta.value(0))
						Asignado += 1
						consulta.exec_("UPDATE Habitaciones SET Asignado = %d WHERE Numero_Codigo = '%s'" %(Asignado, Habitacion))
						ultimaFecha = ""
						fechaActual = time.strftime("%d/%m/%y")
						consulta = QtSql.QSqlQuery()
						consulta.exec_("select Fecha from Ingresos")
						while consulta.next():
							ultimaFecha = consulta.value(0)
						if ultimaFecha == fechaActual:
							consulta.exec_("SELECT SUM(Total) FROM AsignarHabitaciones")
							Ingreso = 0.0
							while consulta.next():
								Ingreso = float(consulta.value(0))
							consulta.exec_("UPDATE Ingresos SET Ingreso = %f WHERE Fecha = '%s'" %(Ingreso, ultimaFecha))
						else:
							consulta.exec_("SELECT SUM(Total) FROM AsignarHabitaciones")
							Ingreso = 0.0
							while consulta.next():
								Ingreso = float(consulta.value(0))
							consulta.exec_("INSERT INTO Ingresos (Fecha, Ingreso) VALUES('%s', %f)" %(fechaActual, Ingreso))
					QMessageBox.information(self, "Aviso","Se le ha asignado la habitacion %s al cliente %s" %(Habitacion, cedula), QMessageBox.Ok)
				else:
					QMessageBox.warning(self, "Error", "La fecha es incorrecta", QMessageBox.Ok)
	def Estado(self):
		if not self.ventanahabitaciones.tabEstado.isVisible():
			self.ventanahabitaciones.tabHabitaciones.addTab(self.ventanahabitaciones.tabEstado, "Estado")
			self.ventanahabitaciones.btnCerrar_Estado.clicked.connect(self.cerrarEstado)
			self.ventanahabitaciones.cBGuardar.currentIndexChanged.connect(self.Guardar)
			self.ventanahabitaciones.btnRecargar_Estado.clicked.connect(self.Recargar_Habitaciones)
			self.ventanahabitaciones.tablaEstado.setColumnCount(5)
			self.ventanahabitaciones.tablaEstado.setHorizontalHeaderLabels(['Numero_Codigo', 'Piso', 'Estado', 'Capacidad', 'Asignado'])
			for i in range(self.ventanahabitaciones.tablaEstado.rowCount()):
				self.ventanahabitaciones.tablaEstado.removeRow(i)
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec__("SELECT * FROM Habitaciones")
			row = 0
			while consulta.next():
				self.ventanahabitaciones.tablaEstado.insertRow(row)
				Numero_Codigo = QTableWidgetItem(str(consulta.value(0)))
				Piso = QTableWidgetItem(str(consulta.value(1)))
				Estado = QTableWidgetItem(str(consulta.value(2)))
				Capacidad = QTableWidgetItem(str(consulta.value(3)))
				Asignado = QTableWidgetItem(str(consulta.value(4)))
				self.ventanahabitaciones.tablaEstado.setItem(row, 0, Numero_Codigo)
				self.ventanahabitaciones.tablaEstado.setItem(row, 1, Piso)
				self.ventanahabitaciones.tablaEstado.setItem(row, 2, Estado)
				self.ventanahabitaciones.tablaEstado.setItem(row, 3, Capacidad)
				self.ventanahabitaciones.tablaEstado.setItem(row, 4, Asignado)
				row = row + 1
			self.db.close()
	def Guardar(self):
		tipo = self.ventanahabitaciones.cBGuardar.currentText()
		if tipo == "CSV":
			ruta_guardar = ""
			NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
			if NombreArchivo[0]:
				file = open(NombreArchivo[0]+'.csv', 'w')
				self.db.open()
				consulta = QtSql.QSqlQuery()
				consulta.exec_("SELECT * FROM Habitaciones")
				fieldnames = ["Numero_Codigo", "Piso", "Estado", "Capacidad", "Asignado"]
				csvsalida = csv.DictWriter(file, fieldnames)
				while consulta.next():
					csvsalida.writerow( { fieldnames[0] : consulta.value(0),
							 fieldnames[1] : consulta.value(1),
							 fieldnames[2] : consulta.value(2),
							 fieldnames[3] : consulta.value(3),
							 fieldnames[4] : consulta.value(4)
							 })
				file.close()
		elif tipo == "PDF":
			ruta_guardar = ""
			NombreArchivo = QFileDialog.getSaveFileName(self, "Guarfar Archivo", ruta_guardar)
			if NombreArchivo[0]:
				self.db.open()
				consulta = QtSql.QSqlQuery()
				consulta.exec_("SELECT * FROM Habitaciones")
				estiloHoja = getSampleStyleSheet()
				story = []
				cuerpo = estiloHoja["BodyText"]
				cuerpo.alignment=TA_CENTER

				col = ["Numero_Codigo", "Piso", "Estado", "Capacidad", "Asignado"]
				fil = []
				fil.insert(0, col)
				fila = 1
				while consulta.next():
					fil.insert(fila, [consulta.value(0), consulta.value(1), consulta.value(2), consulta.value(3), consulta.value(4)])
					fila += 1
				datos = [i for i in fil]
				tabla = Table(data=datos,colWidths=[90,60,80,60,80])
				story.append(tabla)
				doc = SimpleDocTemplate(NombreArchivo[0]+'.pdf',pagesize=portrait(LETTER), leftMargin=3, rightMargin=4, topMargin=3, bottomMargin=4)
				doc.build(story)
	def Asignaciones(self):
		if not self.ventanahabitaciones.tabAsignaciones.isVisible():
			self.ventanahabitaciones.tabHabitaciones.addTab(self.ventanahabitaciones.tabAsignaciones, "Asignaciones")
			self.ventanahabitaciones.btnCerrar_Asignaciones.clicked.connect(self.cerrarAsignaciones)
			self.ventanahabitaciones.btnEliminar.clicked.connect(self.Eliminar)
			self.ventanahabitaciones.btnRecargar.clicked.connect(self.Recargar)
			self.ventanahabitaciones.leBuscarAsignaciones.textChanged.connect(self.BuscarAsignaciones)
			for i in range(self.ventanahabitaciones.tablaAsignaciones.rowCount()):
				self.ventanahabitaciones.tablaAsignaciones.removeRow(i)
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM AsignarHabitaciones")
			self.ventanahabitaciones.tablaAsignaciones.setColumnCount(7)
			self.ventanahabitaciones.tablaAsignaciones.setHorizontalHeaderLabels(['N°', 'CI_RIF', 'Habitacion', 'Fecha_Entrada', 'Fecha_Salida', 'Costo_Dia', 'Total'])
			row = 0
			while consulta.next():
				self.ventanahabitaciones.tablaAsignaciones.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				CI_RIF = QTableWidgetItem(str(consulta.value(1)))
				Habitaciones = QTableWidgetItem(str(consulta.value(2)))
				Fecha_Entrada = QTableWidgetItem(str(consulta.value(3)))
				Fecha_Salida = QTableWidgetItem(str(consulta.value(4)))
				Costo_Dia = QTableWidgetItem(str(consulta.value(5)))
				Total = QTableWidgetItem(str(consulta.value(6)))
				self.ventanahabitaciones.tablaAsignaciones.setItem(row, 0, Numero)
				self.ventanahabitaciones.tablaAsignaciones.setItem(row, 1, CI_RIF)
				self.ventanahabitaciones.tablaAsignaciones.setItem(row, 2, Habitaciones)
				self.ventanahabitaciones.tablaAsignaciones.setItem(row, 3, Fecha_Entrada)
				self.ventanahabitaciones.tablaAsignaciones.setItem(row, 4, Fecha_Salida)
				self.ventanahabitaciones.tablaAsignaciones.setItem(row, 5, Costo_Dia)
				self.ventanahabitaciones.tablaAsignaciones.setItem(row, 6, Total)
				row = row + 1
			self.db.close()

	def Recargar(self):
		for i in range(self.ventanahabitaciones.tablaAsignaciones.rowCount()):
			self.ventanahabitaciones.tablaAsignaciones.removeRow(i)
		self.db.open()
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT * FROM AsignarHabitaciones")
		row = 0
		while consulta.next():
			self.ventanahabitaciones.tablaAsignaciones.insertRow(row)
			Numero = QTableWidgetItem(str(consulta.value(0)))
			CI_RIF = QTableWidgetItem(str(consulta.value(1)))
			Habitaciones = QTableWidgetItem(str(consulta.value(2)))
			Fecha_Entrada = QTableWidgetItem(str(consulta.value(3)))
			Fecha_Salida = QTableWidgetItem(str(consulta.value(4)))
			Costo_Dia = QTableWidgetItem(str(consulta.value(5)))
			Total = QTableWidgetItem(str(consulta.value(6)))
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 0, Numero)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 1, CI_RIF)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 2, Habitaciones)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 3, Fecha_Entrada)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 4, Fecha_Salida)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 5, Costo_Dia)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 6, Total)
			row = row + 1
		self.db.close()
	def Eliminar(self):
		row = self.ventanahabitaciones.tablaAsignaciones.currentRow()
		print(row)
		if row > -1:
			Pregunta = QMessageBox(self)
			Pregunta.setText("¿Desea eliminar la asignacion?")
			Pregunta.setIconPixmap(QPixmap("Iconos/pregunta.png"))
			SI = Pregunta.addButton("Si", QMessageBox.ActionRole)
			NO = Pregunta.addButton("No", QMessageBox.ActionRole)
			SI.setIcon(QIcon("Iconos/aceptar-ico.png"))
			NO.setIcon(QIcon("Iconos/cancelar.png"))
			Pregunta.setWindowTitle("Eliminar")
			Pregunta.exec_()
			if Pregunta.clickedButton() == SI:
				self.db.open()
				consulta = QtSql.QSqlQuery()
				numero = self.ventanahabitaciones.tablaAsignaciones.item(row, 0).text()
				consulta.exec_("DELETE FROM AsignarHabitaciones WHERE N° = %d" %(int(numero)))
				habitacion = self.ventanahabitaciones.tablaAsignaciones.item(row, 2).text()
				consulta.exec_("SELECT Asignado From Habitaciones WHERE Numero_Codigo = %d" %(int(habitacion)))
				asignado = 0
				while consulta.next():
					asignado = int(consulta.value(0))
				asignado -= 1
				consulta.exec_("UPDATE Habitaciones SET Asignado = %d WHERE Numero_Codigo = %d" %(asignado,int(habitacion)))
				if asignado == 0:
					consulta.exec_("UPDATE Habitaciones SET Estado = 'Desocupada' WHERE Numero_Codigo = %d" %(int(habitacion)))
				QMessageBox.information(self,"Eliminado", "Asignacion Eliminada!!!")
				self.db.close()
			else:
				Pregunta.close()
	def Recargar_Habitaciones(self):
		self.db.open()
		self.ventanahabitaciones.tablaEstado.clearContents()
		for i in range(self.ventanahabitaciones.tablaEstado.rowCount()):
			self.ventanahabitaciones.tablaEstado.removeRow(i)
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT * FROM Habitaciones")
		row = 0
		while consulta.next():
			self.ventanahabitaciones.tablaAsignaciones.insertRow(row)
			Numero_Codigo = QTableWidgetItem(str(consulta.value(0)))
			Piso = QTableWidgetItem(str(consulta.value(1)))
			Estado = QTableWidgetItem(str(consulta.value(2)))
			Capacidad = QTableWidgetItem(str(consulta.value(3)))
			Asignado = QTableWidgetItem(str(consulta.value(4)))

			self.ventanahabitaciones.tablaEstado.setItem(row, 0, Numero_Codigo)
			self.ventanahabitaciones.tablaEstado.setItem(row, 1, Piso)
			self.ventanahabitaciones.tablaEstado.setItem(row, 2, Estado)
			self.ventanahabitaciones.tablaEstado.setItem(row, 3, Capacidad)
			self.ventanahabitaciones.tablaEstado.setItem(row, 4, Asignado)
			row = row + 1
		self.db.close()
	def BuscarAsignaciones(self):
		codigo = self.ventanahabitaciones.leBuscarAsignaciones.text()
		self.db.open()
		for i in range(self.ventanahabitaciones.tablaAsignaciones.rowCount()):
			self.ventanahabitaciones.tablaAsignaciones.removeRow(i)
		consulta = QtSql.QSqlQuery()
		if codigo != "":
			consulta.exec_("SELECT * FROM AsignarHabitaciones WHERE Habitaciones = %d" % (int(codigo)))
		row = 0
		while consulta.next():
			self.ventanahabitaciones.tablaAsignaciones.insertRow(row)
			Numero = QTableWidgetItem(str(consulta.value(0)))
			CI_RIF = QTableWidgetItem(str(consulta.value(1)))
			Habitacion = QTableWidgetItem(str(consulta.value(2)))
			Fecha_Entrada = QTableWidgetItem(str(consulta.value(3)))
			Fecha_Salida = QTableWidgetItem(str(consulta.value(4)))
			Costo_Dia = QTableWidgetItem(str(consulta.value(5)))
			Total = QTableWidgetItem(str(consulta.value(6)))
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 0, Numero)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 1, CI_RIF)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 2, Habitacion)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 3, Fecha_Entrada)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 4, Fecha_Salida)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 5, Costo_Dia)
			self.ventanahabitaciones.tablaAsignaciones.setItem(row, 6, Total)
			row = row + 1
		self.db.close()
	def cerrarAsignar(self):
		index = self.ventanahabitaciones.tabHabitaciones.indexOf(self.ventanahabitaciones.tabAsignar)
		self.ventanahabitaciones.tabHabitaciones.removeTab(index)
	def cerrarEstado(self):
		index = self.ventanahabitaciones.tabHabitaciones.indexOf(self.ventanahabitaciones.tabEstado)
		self.ventanahabitaciones.tabHabitaciones.removeTab(index)
		for i in range(self.ventanahabitaciones.tablaEstado.rowCount()):
			self.ventanahabitaciones.tablaEstado.removeRow(i)
	def cerrarAsignaciones(self):
		index = self.ventanahabitaciones.tabHabitaciones.indexOf(self.ventanahabitaciones.tabAsignaciones)
		self.ventanahabitaciones.tabHabitaciones.removeTab(index)
		for i in range(self.ventanahabitaciones.tablaAsignaciones.rowCount()):
			self.ventanahabitaciones.tablaAsignaciones.removeRow(i)
	def AcercaDe(self):
		acerca = AcercaDe(self)
		acerca.show()
#app = QApplication([])
#window = VentanaHabitaciones(None)
#window.show()
#app.exec__()
