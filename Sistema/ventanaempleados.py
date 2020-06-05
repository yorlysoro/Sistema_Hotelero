# -*- coding: utf-8 -*-
from ventanaempleadoswin import Ui_VentanaEmpleados
from PyQt5.QtWidgets import QApplication, QMainWindow,  QTableWidgetItem, QMessageBox, QFileDialog
from Validaciones import Validaciones
from PyQt5 import QtSql
from PyQt5.QtGui import QIcon, QPixmap
import csv
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.lib.enums import TA_CENTER
from acercaDe import AcercaDe
import time

class VentanaEmpleados(QMainWindow):
	def __init__(self, padre=None, db=None):
		QMainWindow.__init__(self, padre)
		self.ventanaempleados = Ui_VentanaEmpleados()
		self.ventanaempleados.setupUi(self)
		self.db = db
		self.validacion = Validaciones(self.ventanaempleados)
		self.ventanaempleados.btnAgregar.clicked.connect(self.Agregar)
		self.ventanaempleados.btnTurnos.clicked.connect(self.Turnos)
		self.ventanaempleados.btnLista.clicked.connect(self.Lista)
		self.ventanaempleados.actionSalir.triggered.connect(self.close)
		self.ventanaempleados.actionAgregar.triggered.connect(self.Agregar)
		self.ventanaempleados.actionTurnos.triggered.connect(self.Turnos)
		self.ventanaempleados.actionLista.triggered.connect(self.Lista)
		self.ventanaempleados.actionAcercaDe.triggered.connect(self.acercaDe)
		self.setWindowTitle("Empleados")
		self.setWindowIcon(QIcon("Iconos/empleados-ico.png"))
		self.ventanaempleados.actionAcercaDe.setIcon(QIcon("Iconos/estrella.png"))
		self.ventanaempleados.actionAgregar.setIcon(QIcon("Iconos/usuario.png"))
		self.ventanaempleados.actionLista.setIcon(QIcon("Iconos/bloc.png"))
		self.ventanaempleados.actionSalir.setIcon(QIcon("Iconos/cancelar.png"))
		self.ventanaempleados.actionTurnos.setIcon(QIcon("Iconos/turnos.png"))
		self.setFixedSize(1086, 600)
	def Agregar(self):
		if not self.ventanaempleados.tabAgregar.isVisible():
			self.ventanaempleados.tabEmpleados.addTab(self.ventanaempleados.tabAgregar, "Agregar")
			self.ventanaempleados.leCI_RIF.textChanged.connect(self.validacion.validar_cedula)
			self.ventanaempleados.leNombre.textChanged.connect(self.validacion.validar_nombre)
			self.ventanaempleados.leApellido.textChanged.connect(self.validacion.validar_apellido)
			self.ventanaempleados.leCorreo.textChanged.connect(self.validacion.validar_correo)
			self.ventanaempleados.leTelefono.textChanged.connect(self.validacion.validar_telefono)
			self.ventanaempleados.teDireccion.textChanged.connect(self.validacion.validar_direccion_2)
			self.ventanaempleados.leSueldo.textChanged.connect(self.validacion.validar_sueldo)
			self.ventanaempleados.btnAgregar_2.clicked.connect(self.AgregarBtn)
			self.ventanaempleados.btnCerrar_Agregar.clicked.connect(self.Cerrar_Agregar)
	def AgregarBtn(self):
		if self.validacion.validar_cedula() and self.validacion.validar_apellido() and self.validacion.validar_correo() and self.validacion.validar_telefono() and self.validacion.validar_direccion_2() and self.validacion.validar_sueldo():
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT CI_RIF FROM Empleados WHERE CI_RIF = '%s'" %(self.ventanaempleados.leCI_RIF.text()))
			ci = ""
			while consulta.next():
				ci = consulta.value(0)
			if ci == "":
				consulta.exec_("INSERT INTO Empleados (CI_RIF, Nombre, Apellido, Correo, Telefono, Direccion, Sueldo) VALUES('%s', '%s', '%s', '%s', '%s', '%s', %f)" %(self.ventanaempleados.leCI_RIF.text(), self.ventanaempleados.leNombre.text(), self.ventanaempleados.leApellido.text(), self.ventanaempleados.leCorreo.text(), self.ventanaempleados.leTelefono.text(), self.ventanaempleados.teDireccion.toPlainText(), float(self.ventanaempleados.leSueldo.text())))
				QMessageBox.information(self, "Aviso", "El Empleado %s ha sido agreagado" %(self.ventanaempleados.leCI_RIF.text()), QMessageBox.Ok)
			elif ci == self.ventanaempleados.leCI_RIF.text():
				QMessageBox.warning(self, "Error1/1/00", "El empleado ya existe!!!", QMessageBox.Ok)
			self.db.close()
		elif not self.validacion.validar_cedula():
			QMessageBox.warning(self, "Error", "Falta la cedula", QMessageBox.Ok)
		elif not self.validacion.validar_nombre():
			QMessageBox.warning(self, "Error", "Falta el nombre", QMessageBox.Ok)
		elif not self.validacion.validar_apellido():
			QMessageBox.warning(self, "Error", "Falta el apellido", QMessageBox.Ok)
		elif not self.validacion.validar_correo():
			QMessageBox.warning(self, "Error", "Falta el correo", QMessageBox.Ok)
		elif not self.validacion.validar_direccion_2():
			QMessageBox.warning(self, "Error", "Falta la direccion", QMessageBox.Ok)
		elif not self.validacion.validar_sueldo():
			QMessageBox.warning(self, "Error", "Falta el sueldo", QMessageBox.Ok)
		elif not self.validacion.validar_sueldo():
			QMessageBox.warning(self, "Error", "Falta el telefono", QMessageBox.Ok)
		elif not self.validacion.validar_cedula() and not self.validacion.validar_apellido() and not self.validacion.validar_correo() and not self.validacion.validar_telefono() and not self.validacion.validar_direccion_2() and not self.validacion.validar_sueldo():
			QMessageBox.warning(self, "Error", "No ha llenado ningun campo", QMessageBox.Ok)
		
	def Cerrar_Agregar(self):
		index = self.ventanaempleados.tabEmpleados.indexOf(self.ventanaempleados.tabAgregar)
		self.ventanaempleados.tabEmpleados.removeTab(index)
	def Turnos(self):
		if not self.ventanaempleados.tabTurnos.isVisible():
			self.ventanaempleados.tabEmpleados.addTab(self.ventanaempleados.tabTurnos, "Turnos")
			self.ventanaempleados.cbTodos.currentIndexChanged.connect(self.Todos)
			self.ventanaempleados.cbEmpleados.currentIndexChanged.connect(self.Empleados)
			self.ventanaempleados.cbGuardar.currentIndexChanged.connect(self.Guardar_Turnos)
			self.ventanaempleados.btnCerrar_Turnos.clicked.connect(self.Cerrar_Turnos)
			self.ventanaempleados.btnAsignar.clicked.connect(self.Asignar)
			self.ventanaempleados.leCI_RIF_2.textChanged.connect(self.validacion.validar_cedula_2)
			self.ventanaempleados.leCI_RIF_3.textChanged.connect(self.validacion.validar_cedula_3)
			self.ventanaempleados.tablaTurnos.setColumnCount(5)
			self.ventanaempleados.tablaTurnos.setHorizontalHeaderLabels(['N°', 'CI_RIF', 'Hora_Inicio', 'Hora_Fin', 'Fecha'])
			for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
				self.ventanaempleados.tablaTurnos.removeRow(i)
	def Todos(self):
		tipo = self.ventanaempleados.cbTodos.currentText()
		dia = time.strftime("%d/%m/%y")
		mes = time.strftime("%m/%y")
		anio = time.strftime("%y")
		for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
			self.ventanaempleados.tablaTurnos.removeRow(i)
		if tipo == "Dia":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Turnos WHERE Fecha BETWEEN '%s' and '%s'" % (dia, dia))
			row = 0
			for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
				self.ventanaempleados.tablaTurnos.removeRow(i)
			while consulta.next():
				self.ventanaempleados.tablaTurnos.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				CI_RIF = QTableWidgetItem(str(consulta.value(1)))
				Inicio = QTableWidgetItem(str(consulta.value(2)))
				Fin = QTableWidgetItem(str(consulta.value(3)))
				Fecha = QTableWidgetItem(str(consulta.value(4)))
				 
				self.ventanaempleados.tablaTurnos.setItem(row, 0, Numero)
				self.ventanaempleados.tablaTurnos.setItem(row, 1, CI_RIF)
				self.ventanaempleados.tablaTurnos.setItem(row, 2, Inicio)
				self.ventanaempleados.tablaTurnos.setItem(row, 3, Fin)
				self.ventanaempleados.tablaTurnos.setItem(row, 4, Fecha)

				row = row + 1
			self.db.close()
		elif tipo == "Mes":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Turnos WHERE Fecha BETWEEN '%s' and '%s'" % ('1/'+mes,'31/'+mes))
			row = 0
			for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
				self.ventanaempleados.tablaTurnos.removeRow(i)
			while consulta.next():
				self.ventanaempleados.tablaTurnos.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				CI_RIF= QTableWidgetItem(str(consulta.value(1)))
				Inicio = QTableWidgetItem(str(consulta.value(2)))
				Fin = QTableWidgetItem(str(consulta.value(3)))
				Fecha = QTableWidgetItem(str(consulta.value(4)))
				

				self.ventanaempleados.tablaTurnos.setItem(row, 0, Numero)
				self.ventanaempleados.tablaTurnos.setItem(row, 1, CI_RIF)
				self.ventanaempleados.tablaTurnos.setItem(row, 2, Inicio)
				self.ventanaempleados.tablaTurnos.setItem(row, 3, Fin)
				self.ventanaempleados.tablaTurnos.setItem(row, 4, Fecha)

				row = row + 1
			self.db.close()
		elif tipo == "Año":
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Turnos WHERE Fecha BETWEEN '%s' and '%s'" % ('1/1/'+anio,'31/12/'+anio))
			row = 0
			for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
				self.ventanaempleados.tablaTurnos.removeRow(i)
			while consulta.next():
				self.ventanaempleados.tablaTurnos.insertRow(row)
				Numero = QTableWidgetItem(str(consulta.value(0)))
				CI_RIF= QTableWidgetItem(str(consulta.value(1)))
				Inicio = QTableWidgetItem(str(consulta.value(2)))
				Fin = QTableWidgetItem(str(consulta.value(3)))
				Fecha = QTableWidgetItem(str(consulta.value(4)))
				

				self.ventanaempleados.tablaTurnos.setItem(row, 0, Numero)
				self.ventanaempleados.tablaTurnos.setItem(row, 1, CI_RIF)
				self.ventanaempleados.tablaTurnos.setItem(row, 2, Inicio)
				self.ventanaempleados.tablaTurnos.setItem(row, 3, Fin)
				self.ventanaempleados.tablaTurnos.setItem(row, 4, Fecha)

				row = row + 1
			self.db.close()
		else:
			for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
				self.ventanaempleados.tablaTurnos.removeRow(i)
	def Empleados(self):
		tipo = self.ventanaempleados.cbEmpleados.currentText()
		dia = time.strftime("%d/%m/%y")
		mes = time.strftime("%m/%y")
		anio = time.strftime("%y")
		for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
			self.ventanaempleados.tablaTurnos.removeRow(i)
		self.db.open()
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT CI_RIF FROM Empleados WHERE CI_RIF = '%s'" %(self.ventanaempleados.leCI_RIF_2.text()))
		ci = ""
		while consulta.next():
			ci = consulta.value(0)
		if ci == "":
			QMessageBox.warning(self, "Error", "El empleado no existe", QMessageBox.Ok)
		else:
			if tipo == "Dia":
				consulta.exec_("SELECT * FROM Turnos WHERE CI_RIF = '%s' and Fecha BETWEEN '%s' and '%s'" % (self.ventanaempleados.leCI_RIF_2.text(), dia, dia))
				row = 0
				for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
					self.ventanaempleados.tablaTurnos.removeRow(i)
				while consulta.next():
					self.ventanaempleados.tablaTurnos.insertRow(row)
					Numero = QTableWidgetItem(str(consulta.value(0)))
					CI_RIF = QTableWidgetItem(str(consulta.value(1)))
					Inicio = QTableWidgetItem(str(consulta.value(2)))
					Fin = QTableWidgetItem(str(consulta.value(3)))
					Fecha = QTableWidgetItem(str(consulta.value(4)))
					 
					self.ventanaempleados.tablaTurnos.setItem(row, 0, Numero)
					self.ventanaempleados.tablaTurnos.setItem(row, 1, CI_RIF)
					self.ventanaempleados.tablaTurnos.setItem(row, 2, Inicio)
					self.ventanaempleados.tablaTurnos.setItem(row, 3, Fin)
					self.ventanaempleados.tablaTurnos.setItem(row, 4, Fecha)

					row = row + 1
			elif tipo == "Mes":
				consulta.exec_("SELECT * FROM Turnos WHERE CI_RIF = '%s' and Fecha BETWEEN '%s' and '%s'" % (self.ventanaempleados.leCI_RIF_2.text(),'1/'+mes,'31/'+mes))
				row = 0
				for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
					self.ventanaempleados.tablaTurnos.removeRow(i)
				while consulta.next():
					self.ventanaempleados.tablaTurnos.insertRow(row)
					Numero = QTableWidgetItem(str(consulta.value(0)))
					CI_RIF= QTableWidgetItem(str(consulta.value(1)))
					Inicio = QTableWidgetItem(str(consulta.value(2)))
					Fin = QTableWidgetItem(str(consulta.value(3)))
					Fecha = QTableWidgetItem(str(consulta.value(4)))
					

					self.ventanaempleados.tablaTurnos.setItem(row, 0, Numero)
					self.ventanaempleados.tablaTurnos.setItem(row, 1, CI_RIF)
					self.ventanaempleados.tablaTurnos.setItem(row, 2, Inicio)
					self.ventanaempleados.tablaTurnos.setItem(row, 3, Fin)
					self.ventanaempleados.tablaTurnos.setItem(row, 4, Fecha)

					row = row + 1
			elif tipo == "Año":
				consulta.exec_("SELECT * FROM Turnos WHERE CI_RIF = '%s' and Fecha BETWEEN '%s' and '%s'" % (self.ventanaempleados.leCI_RIF_2.text(),'1/1/'+anio,'31/12/'+anio))
				row = 0
				for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
					self.ventanaempleados.tablaTurnos.removeRow(i)
				while consulta.next():
					self.ventanaempleados.tablaTurnos.insertRow(row)
					Numero = QTableWidgetItem(str(consulta.value(0)))
					CI_RIF= QTableWidgetItem(str(consulta.value(1)))
					Inicio = QTableWidgetItem(str(consulta.value(2)))
					Fin = QTableWidgetItem(str(consulta.value(3)))
					Fecha = QTableWidgetItem(str(consulta.value(4)))
					

					self.ventanaempleados.tablaTurnos.setItem(row, 0, Numero)
					self.ventanaempleados.tablaTurnos.setItem(row, 1, CI_RIF)
					self.ventanaempleados.tablaTurnos.setItem(row, 2, Inicio)
					self.ventanaempleados.tablaTurnos.setItem(row, 3, Fin)
					self.ventanaempleados.tablaTurnos.setItem(row, 4, Fecha)

					row = row + 1
			else:
				for i in range(self.ventanaempleados.tablaTurnos.rowCount()):
					self.ventanaempleados.tablaTurnos.removeRow(i)
			self.db.close()
	def Guardar_Turnos(self):
		tipo = self.ventanaempleados.cbGuardar.currentText()
		row = self.ventanaempleados.tablaTurnos.rowCount()
		if self.ventanaempleados.tablaTurnos.item(0,0) != None:
			if tipo == "CSV":
				ruta_guardar = ""
				NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
				if NombreArchivo[0]:
					file = open(NombreArchivo[0]+'.csv', 'w')
					fieldnames = ["N°", "CI_RIF", "Hora_Inicio", "Hora_Fin", "Fecha"]
					csvsalida = csv.DictWriter(file, fieldnames)
					for i in range(row):
						csvsalida.writerow({fieldnames[0] : self.ventanaempleados.tablaTurnos.item(i, 0).text(),
						fieldnames[1] : self.ventanaempleados.tablaTurnos.item(i, 1).text(),
						fieldnames[2] : self.ventanaempleados.tablaTurnos.item(i, 2).text(),
						fieldnames[3] : self.ventanaempleados.tablaTurnos.item(i, 3).text(),
						fieldnames[4] : self.ventanaempleados.tablaTurnos.item(i, 4).text()})
					file.close()
			elif tipo == "PDF":
				ruta_guardar = ""
				NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
				if NombreArchivo[0]:
					estiloHoja = getSampleStyleSheet()
					story = []
					cuerpo = estiloHoja["BodyText"]
					cuerpo.alignment=TA_CENTER

					col = ["N°", "CI_RIF", "Hora_Inicio", "Hora_Fin", "Fecha"]
					fil = []
					fil.insert(0, col)
					filasTabla = 0
					for fila in range(row):
						fil.insert(fila+1, [self.ventanaempleados.tablaTurnos.item(filasTabla, 0).text(), self.ventanaempleados.tablaTurnos.item(filasTabla, 1).text(), self.ventanaempleados.tablaTurnos.item(filasTabla, 2).text(), self.ventanaempleados.tablaTurnos.item(filasTabla, 3).text(), self.ventanaempleados.tablaTurnos.item(filasTabla, 4).text()])
						filasTabla += 1
					datos = [i for i in fil]
					tabla = Table(data=datos,colWidths=[20,60,60,60,60])
					story.append(tabla)
					doc = SimpleDocTemplate(NombreArchivo[0]+'.pdf',pagesize=portrait(LETTER), leftMargin=3, rightMargin=4, topMargin=3, bottomMargin=4)
					doc.build(story)
	def Cerrar_Turnos(self):
		index = self.ventanaempleados.tabEmpleados.indexOf(self.ventanaempleados.tabTurnos)
		self.ventanaempleados.tabEmpleados.removeTab(index)
	def Asignar(self):
		self.db.open()
		consulta = QtSql.QSqlQuery()
		ci = ""
		consulta.exec_("SELECT CI_RIF FROM Empleados WHERE CI_RIF = '%s'" %(self.ventanaempleados.leCI_RIF_3.text()))
		while consulta.next():
			ci = consulta.value(0)
		if ci == "":
			QMessageBox.warning(self, "Error", "La cedula no existe", QMessageBox.Ok)
		else:
			ultimafecha = ""
			consulta.exec_("SELECT Fecha FROM Turnos WHERE CI_RIF = '%s'" %(self.ventanaempleados.leCI_RIF_3.text()))
			while consulta.next():
				ultimafecha = consulta.value(0)
			consulta.exec_("SELECT Hora_Inicio, Hora_Fin From Turnos WHERE CI_RIF = '%s'" %(self.ventanaempleados.leCI_RIF_3.text()))
			while consulta.next():
				Hora_Inicio = consulta.value(0)
				Hora_Fin = consulta.value(1)
			fechaActual = time.strftime("%d/%m/%y")
			listFecha = fechaActual.split('/')
			anioEntrada = self.ventanaempleados.dateFecha.text().split('/')
			if fechaActual == ultimafecha and Hora_Inicio == self.ventanaempleados.timeInicio.text() and Hora_Fin == self.ventanaempleados.timeFin.text():
				QMessageBox.warning(self, "Error", "El empleado ya tiene asignado un turno", QMessageBox.Ok)
			elif anioEntrada[2] != listFecha[2]:
				QMessageBox.warning(self, "Error", "Error en asignar las fecha", QMessageBox.Ok)
			elif self.ventanaempleados.timeFin.text() == self.ventanaempleados.timeInicio.text():
				QMessageBox.warning(self, "Error", "Error al asignar las horas", QMessageBox.Ok)
			else:
				consulta.exec_("INSERT INTO Turnos (CI_RIF, Hora_Inicio, Hora_Fin, Fecha) VALUES('%s', '%s', '%s', '%s')" %(self.ventanaempleados.leCI_RIF_3.text(), self.ventanaempleados.timeInicio.text(), self.ventanaempleados.timeFin.text(), self.ventanaempleados.dateFecha.text()))
				QMessageBox.information(self, "Aviso", "Se le ha asignado un turno al empleado %s" %(self.ventanaempleados.leCI_RIF_3.text()), QMessageBox.Ok)
	def Lista(self):
		if not self.ventanaempleados.tabLista.isVisible():
			self.ventanaempleados.tabEmpleados.addTab(self.ventanaempleados.tabLista, "Lista")
			self.ventanaempleados.leBuscar_Lista.textChanged.connect(self.Buscar)
			self.ventanaempleados.tablaLista.itemChanged.connect(self.Actualizar)
			self.ventanaempleados.btnEliminar.clicked.connect(self.Eliminar)
			self.ventanaempleados.btnRecargar.clicked.connect(self.Recargar)
			self.ventanaempleados.btnCerrar_Lista.clicked.connect(self.Cerrar_Lista)
			self.ventanaempleados.cbGuardar_Lista.currentIndexChanged.connect(self.Guardar_Lista)
			self.ventanaempleados.tablaLista.setColumnCount(7)
			self.ventanaempleados.tablaLista.setHorizontalHeaderLabels(['CI_RIF', 'Nombre', 'Apellido', 'Correo', 'Telefono', 'Direccion', 'Sueldo'])
			for i in range(self.ventanaempleados.tablaLista.rowCount()):
				self.ventanaempleados.tablaLista.removeRow(i)
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Empleados")
			row = 0
			while consulta.next():
				self.ventanaempleados.tablaLista.insertRow(row)
				CI_RIF = QTableWidgetItem(str(consulta.value(0)))
				nombre = QTableWidgetItem(str(consulta.value(1)))
				apellido = QTableWidgetItem(str(consulta.value(2)))
				correo = QTableWidgetItem(str(consulta.value(3)))
				telefono = QTableWidgetItem(str(consulta.value(4)))
				direccion = QTableWidgetItem(str(consulta.value(5)))
				sueldo = QTableWidgetItem(str(consulta.value(6)))
				self.ventanaempleados.tablaLista.setItem(row, 0, CI_RIF)
				self.ventanaempleados.tablaLista.setItem(row, 1, nombre)
				self.ventanaempleados.tablaLista.setItem(row, 2, apellido)
				self.ventanaempleados.tablaLista.setItem(row, 3, correo)
				self.ventanaempleados.tablaLista.setItem(row, 4, telefono)
				self.ventanaempleados.tablaLista.setItem(row, 5, direccion)
				self.ventanaempleados.tablaLista.setItem(row, 6, sueldo)
				row = row + 1
			self.db.close()
	def Buscar(self):
		Cedula = self.ventanaempleados.leBuscar_Lista.text()
		self.db.open()
		for i in range(self.ventanaempleados.tablaLista.rowCount()):
			self.ventanaempleados.tablaLista.removeRow(i)
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT * FROM Empleados WHERE CI_RIF LIKE '%s'" % (Cedula+'%'))
		row = 0
		while consulta.next():
			self.ventanaempleados.tablaLista.insertRow(row)
			CI_RIF = QTableWidgetItem(str(consulta.value(0)))
			nombre = QTableWidgetItem(str(consulta.value(1)))
			apellido = QTableWidgetItem(str(consulta.value(2)))
			correo = QTableWidgetItem(str(consulta.value(3)))
			telefono = QTableWidgetItem(str(consulta.value(4)))
			direccion = QTableWidgetItem(str(consulta.value(5)))
			sueldo = QTableWidgetItem(str(consulta.value(6)))
			self.ventanaempleados.tablaLista.setItem(row, 0, CI_RIF)
			self.ventanaempleados.tablaLista.setItem(row, 1, nombre)
			self.ventanaempleados.tablaLista.setItem(row, 2, apellido)
			self.ventanaempleados.tablaLista.setItem(row, 3, correo)
			self.ventanaempleados.tablaLista.setItem(row, 4, telefono)
			self.ventanaempleados.tablaLista.setItem(row, 5, direccion)
			self.ventanaempleados.tablaLista.setItem(row, 6, sueldo)
			row = row + 1
		self.db.close()
	def Actualizar(self):
		column = self.ventanaempleados.tablaLista.currentColumn()
		row = self.ventanaempleados.tablaLista.currentRow()
		self.db.open()
		consulta = QtSql.QSqlQuery()
		if row > -1:
			CI_RIF = self.ventanaempleados.tablaLista.item(row, 0).text()
			valor = self.ventanaempleados.tablaLista.currentItem().text()
			columns = ['CI_RIF', 'Nombre', 'Apellido', 'Correo', 'Telefono', 'Direccion', 'Sueldo']
			consulta.exec_("UPDATE Empleados SET "+columns[column]+" = '"+valor+"' WHERE CI_RIF = '"+CI_RIF+"'" )
		self.db.close()
	def Eliminar(self):
		row = self.ventanaempleados.tablaLista.currentRow()
		print(row)
		if row > -1:
			Pregunta = QMessageBox(self)
			Pregunta.setText("¿Desea eliminar al cliente?")
			SI = Pregunta.addButton("Si", QMessageBox.ActionRole)
			NO = Pregunta.addButton("No", QMessageBox.ActionRole)
			Pregunta.setIconPixmap(QPixmap("Iconos/pregunta.png"))
			SI.setIcon(QIcon("Iconos/aceptar-ico.png"))
			NO.setIcon(QIcon("Iconos/cancelar.png"))
			Pregunta.setWindowTitle("Eliminar")
			Pregunta.exec_()
			if Pregunta.clickedButton() == SI:
				self.db.open()
				consulta = QtSql.QSqlQuery()
				CI_RIF = self.ventanaempleados.tablaLista.item(row, 0).text()
				consulta.exec_("DELETE FROM Empleados WHERE CI_RIF = '%s'" %(CI_RIF))
				consulta.exec_("DELETE FROM Turnos WHERE CI_RIF = '%s'" %(CI_RIF))
				QMessageBox.information(self,"Eliminado", "Cliente eliminado!!!")
				self.db.close()
			else:
				Pregunta.close()
	def Recargar(self):
		for i in range(self.ventanaempleados.tablaLista.rowCount()):
				self.ventanaempleados.tablaLista.removeRow(i)
		self.db.open()
		self.ventanaempleados.tablaLista.setColumnCount(7)
		self.ventanaempleados.tablaLista.setHorizontalHeaderLabels(['CI_RIF', 'Nombre', 'Apellido', 'Correo', 'Telefono', 'Direccion', 'Sueldo'])
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT * FROM Empleados")
		row = 0
		while consulta.next():
			self.ventanaempleados.tablaLista.insertRow(row)
			CI_RIF = QTableWidgetItem(str(consulta.value(0)))
			nombre = QTableWidgetItem(str(consulta.value(1)))
			apellido = QTableWidgetItem(str(consulta.value(2)))
			correo = QTableWidgetItem(str(consulta.value(3)))
			telefono = QTableWidgetItem(str(consulta.value(4)))
			direccion = QTableWidgetItem(str(consulta.value(5)))
			sueldo = QTableWidgetItem(str(consulta.value(6)))
			self.ventanaempleados.tablaLista.setItem(row, 0, CI_RIF)
			self.ventanaempleados.tablaLista.setItem(row, 1, nombre)
			self.ventanaempleados.tablaLista.setItem(row, 2, apellido)
			self.ventanaempleados.tablaLista.setItem(row, 3, correo)
			self.ventanaempleados.tablaLista.setItem(row, 4, telefono)
			self.ventanaempleados.tablaLista.setItem(row, 5, direccion)
			self.ventanaempleados.tablaLista.setItem(row, 6, sueldo)
			row = row + 1
		self.db.close()
		
	def Guardar_Lista(self):
		tipo = self.ventanaempleados.cbGuardar_Lista.currentText()
		print(tipo)
		self.db.open()
		consulta = QtSql.QSqlQuery()
		if tipo == "CSV":
			ruta_guardar = ""
			NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
			if NombreArchivo[0]:
				file = open(NombreArchivo[0]+'.csv', 'w')
				fieldnames = ["CI_RIF", "Nombre", "Apellido", "Correo", "Telefono", "Direccion", "Sueldo"]
				csvsalida = csv.DictWriter(file, fieldnames)
				consulta.exec_("SELECT * FROM Empleados")
				while consulta.next():
					csvsalida.writerow({fieldnames[0] : consulta.value(0),
					fieldnames[1] : consulta.value(1),
					fieldnames[2] : consulta.value(2),
					fieldnames[3] : consulta.value(3),
					fieldnames[4] : consulta.value(4),
					fieldnames[5] : consulta.value(5),
					fieldnames[6] : consulta.value(6)
					})
				file.close()
		elif tipo == "PDF":
			ruta_guardar = ""
			NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
			if NombreArchivo[0]:
				estiloHoja = getSampleStyleSheet()
				story = []
				cuerpo = estiloHoja["BodyText"]
				cuerpo.alignment=TA_CENTER

				col = ["CI_RIF", "Nombre", "Apellido", "Correo", "Telefono", "Direccion", "Sueldo"]
				fil = []
				fil.insert(0, col)
				filasTabla = 0
				consulta.exec_("SELECT * FROM Empleados")
				while consulta.next():
					fil.insert(filasTabla+1, [consulta.value(0), consulta.value(1), consulta.value(2), consulta.value(3), consulta.value(4), consulta.value(5), consulta.value(6)])
					filasTabla += 1
				datos = [i for i in fil]
				tabla = Table(data=datos,colWidths=[60,80,90,140,110,120,130])
				story.append(tabla)
				doc = SimpleDocTemplate(NombreArchivo[0]+'.pdf',pagesize=landscape(LETTER), leftMargin=3, rightMargin=4, topMargin=3, bottomMargin=4)
				doc.build(story)
	def Cerrar_Lista(self):
		index = self.ventanaempleados.tabEmpleados.indexOf(self.ventanaempleados.tabLista)
		self.ventanaempleados.tabEmpleados.removeTab(index)
	def acercaDe(self):
		acerca = AcercaDe(self)
		acerca.show()
#app = QApplication([])
#window = VentanaEmpleados(None)
#window.show()
#app.exec_()
