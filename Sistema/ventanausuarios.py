# -*- coding: utf-8 -*-
from ventanausuarioswin import Ui_VentanaUsuarios
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from Validaciones import Validaciones
from PyQt5 import QtSql
import csv
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, portrait
from reportlab.lib.enums import TA_CENTER
from acercaDe import AcercaDe
import time

class VentanaUsuarios(QMainWindow):
	def __init__(self, padre=None, db=None):
		QMainWindow.__init__(self, padre)
		self.main = Ui_VentanaUsuarios()
		self.main.setupUi(self)
		self.main.btnAgregar.clicked.connect(self.Agregar)
		self.main.btnEstado.clicked.connect(self.Estado)
		self.main.btnReporte.clicked.connect(self.Reporte)
		self.validacion = Validaciones(self.main)
		self.main.actionSalir_2.triggered.connect(self.close)
		self.main.actionAgregar_2.triggered.connect(self.Agregar)
		self.main.actionEstado_2.triggered.connect(self.Estado)
		self.main.actionCSV.triggered.connect(self.CSV)
		self.main.actionPDF.triggered.connect(self.PDF)
		self.main.actionAcercaDe.triggered.connect(self.acercaDe)
		self.db = db
		self.setWindowTitle("Clientes")
		self.setWindowIcon(QIcon("Iconos/grupo-ico.png"))
		self.main.actionSalir_2.setIcon(QIcon("Iconos/cancelar.png"))
		self.main.actionAcercaDe.setIcon(QIcon("Iconos/estrella.png"))
		self.main.actionAgregar_2.setIcon(QIcon("Iconos/usuario.png"))
		self.main.actionEstado_2.setIcon(QIcon("Iconos/lista.png"))
		self.main.actionCSV.setIcon(QIcon("Iconos/csv.png"))
		self.main.actionPDF.setIcon(QIcon("Iconos/pdf.png"))
		self.main.menuReporte.setIcon(QIcon("Iconos/bloc.png"))
	def Agregar(self):
		if not self.main.tabAgregar.isVisible():
			self.main.tabClientes.addTab(self.main.tabAgregar, "Agregar")
			self.main.leCI_RIF.textChanged.connect(self.validacion.validar_cedula)
			self.main.leNombre.textChanged.connect(self.validacion.validar_nombre)
			self.main.leApellido.textChanged.connect(self.validacion.validar_apellido)
			self.main.leCorreo.textChanged.connect(self.validacion.validar_correo)
			self.main.leTelefono.textChanged.connect(self.validacion.validar_telefono)
			self.main.btnCerrar_Agregar.clicked.connect(self.cerrarAgregar)
			self.main.btnAgregar_2.clicked.connect(self.AgregarBtn)
			self.main.btnEstado.clicked.connect(self.Estado)
	def AgregarBtn(self):
		if self.validacion.validar_cedula() and self.validacion.validar_nombre() and self.validacion.validar_apellido() and self.validacion.validar_correo() and self.validacion.validar_telefono():
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT CI_RIF FROM CLIENTES WHERE CI_RIF = '%s'" % (self.main.leCI_RIF.text()))
			ci = ""
			while consulta.next():
				ci = consulta.value(0)
				if ci == self.main.leCI_RIF.text():
					QMessageBox.warning(self, "Error", "El cliente ya existe!!!!", QMessageBox.Ok)
					break
			if ci != self.main.leCI_RIF.text():
				consulta.exec_("INSERT INTO Clientes VALUES( '%s','%s','%s','%s','%s')" % (self.main.leCI_RIF.text(), self.main.leNombre.text(), self.main.leApellido.text(), self.main.leCorreo.text(), self.main.leTelefono.text()))
				consulta.exec_("SELECT COUNT(CI_RIF) FROM Clientes")
				cantidad = 0
				while consulta.next():
					cantidad = int(consulta.value(0))
				cantidad += 1
				consulta.exec_("SELECT Fecha FROM CantClientes")
				ultimafecha = ""
				while consulta.next():
					ultimafecha = consulta.value(0)
				fechaActual = time.strftime("%d/%m/%y")
				if ultimafecha == "" or fechaActual != ultimafecha:
					consulta.exec_("INSERT INTO CantClientes (Fecha, Cantidad) VALUES('%s', %d)" %(fechaActual,cantidad))
				elif ultimafecha == fechaActual:
					consulta.exec__("UPDATE CantClientes SET Cantidad = %d WHERE Fecha = '%s'" %(cantidad, fechaActual))
				QMessageBox.information(self, "Operacion exitosa", "Cliente %s %s %s fue agregado a la base datos" % (self.main.leCI_RIF.text(), self.main.leNombre.text(), self.main.leApellido.text()), QMessageBox.Ok)
		else:
			if not self.validacion.validar_cedula() and not self.validacion.validar_nombre() and not self.validacion.validar_apellido() and not self.validacion.validar_correo() and not self.validacion.validar_telefono():
				QMessageBox.warning(self, "Error", "No se ha llenado ningun campo!!!", QMessageBox.Ok)
			elif not self.validacion.validar_cedula():
				QMessageBox.warning(self, "Error", "No ha colocado la cedula!!!", QMessageBox.Ok)
			elif not self.validacion.validar_nombre():
				QMessageBox.warning(self, "Error", "No ha colocado el nombre!!!", QMessageBox.Ok)
			elif not self.validacion.validar_apellido():
				QMessageBox.warning(self, "Error", "No ha colocado el appellido!!!", QMessageBox.Ok)
			elif not self.validacion.validar_correo():
				QMessageBox.warning(self,"Error", "No ha colocado el correo!!!", QMessageBox.Ok)
			elif not self.validacion.validar_telefono():
				QMessageBox.warning(self, "Error", "No ha colocado el telefono", QMessageBox.Ok)
			else:
				QMessageBox.warning(self, "Error", "Todo los campos son obligatorios", QMessageBox.Ok)
		self.db.close()
	def Estado(self):
		if not self.main.tabEstado.isVisible():
			self.main.tabClientes.addTab(self.main.tabEstado, "Estado")
			self.main.tablaUsuarios.itemChanged.connect(self.Actualizar)
			self.main.btnCerrar_Estado.clicked.connect(self.cerrarEstado)
			self.main.btnRecargar.clicked.connect(self.Recargar)
			self.main.btnEliminar.clicked.connect(self.Eliminar)
			self.main.leBuscar.textChanged.connect(self.Buscar)
			for i in range(self.main.tablaUsuarios.rowCount()):
				self.main.tablaUsuarios.removeRow(i)
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Clientes")
			self.main.tablaUsuarios.setColumnCount(5)
			self.main.tablaUsuarios.setHorizontalHeaderLabels(['CI_RIF', 'Nombre', 'Apellido', 'Correo', 'Telefono'])
			while consulta.next():
				self.main.tablaUsuarios.insertRow(self.main.tablaUsuarios.rowCount())
				CI_RIF = QTableWidgetItem(str(consulta.value(0)))
				nombre = QTableWidgetItem(str(consulta.value(1)))
				apellido = QTableWidgetItem(str(consulta.value(2)))
				correo = QTableWidgetItem(str(consulta.value(3)))
				telefono = QTableWidgetItem(str(consulta.value(4)))
				self.main.tablaUsuarios.setItem(self.main.tablaUsuarios.rowCount()-1, 0, CI_RIF)
				self.main.tablaUsuarios.setItem(self.main.tablaUsuarios.rowCount()-1, 1, nombre)
				self.main.tablaUsuarios.setItem(self.main.tablaUsuarios.rowCount()-1, 2, apellido)
				self.main.tablaUsuarios.setItem(self.main.tablaUsuarios.rowCount()-1, 3, correo)
				self.main.tablaUsuarios.setItem(self.main.tablaUsuarios.rowCount()-1, 4, telefono)
			self.db.close()
	def Buscar(self):
		Cedula = self.main.leBuscar.text()
		self.db.open()
		for i in range(self.main.tablaUsuarios.rowCount()):
			self.main.tablaUsuarios.removeRow(i)
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT * FROM Clientes WHERE CI_RIF LIKE '%s'" % (Cedula+'%'))
		row = 0
		while consulta.next():
			self.main.tablaUsuarios.insertRow(row)
			CI_RIF = QTableWidgetItem(str(consulta.value(0)))
			nombre = QTableWidgetItem(str(consulta.value(1)))
			apellido = QTableWidgetItem(str(consulta.value(2)))
			correo = QTableWidgetItem(str(consulta.value(3)))
			telefono = QTableWidgetItem(str(consulta.value(4)))
			self.main.tablaUsuarios.setItem(row, 0, CI_RIF)
			self.main.tablaUsuarios.setItem(row, 1, nombre)
			self.main.tablaUsuarios.setItem(row, 2, apellido)
			self.main.tablaUsuarios.setItem(row, 3, correo)
			self.main.tablaUsuarios.setItem(row, 4, telefono)
			row = row + 1
		self.db.close()
	def Actualizar(self):
		column = self.main.tablaUsuarios.currentColumn()
		row = self.main.tablaUsuarios.currentRow()
		self.db.open()
		consulta = QtSql.QSqlQuery()
		if row > -1:
			CI_RIF = self.main.tablaUsuarios.item(row, 0).text()
			valor = self.main.tablaUsuarios.currentItem().text()
			columns = ['CI_RIF', 'Nombre', 'Apellido', 'Correo', 'Telefono']
			consulta.exec_("UPDATE Clientes SET "+columns[column]+" = '"+valor+"' WHERE CI_RIF = '"+CI_RIF+"'" )
		self.db.close()
	def Recargar(self):
		for i in range(self.main.tablaUsuarios.rowCount()):
				self.main.tablaUsuarios.removeRow(i)
		self.db.open()
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT * FROM Clientes")
		self.main.tablaUsuarios.setColumnCount(5)
		self.main.tablaUsuarios.setHorizontalHeaderLabels(['CI_RIF', 'Nombre', 'Apellido', 'Correo', 'Telefono'])
		row = 0
		while consulta.next():
			self.main.tablaUsuarios.insertRow(row)
			CI_RIF = QTableWidgetItem(str(consulta.value(0)))
			nombre = QTableWidgetItem(str(consulta.value(1)))
			apellido = QTableWidgetItem(str(consulta.value(2)))
			correo = QTableWidgetItem(str(consulta.value(3)))
			telefono = QTableWidgetItem(str(consulta.value(4)))
			self.main.tablaUsuarios.setItem(row, 0, CI_RIF)
			self.main.tablaUsuarios.setItem(row, 1, nombre)
			self.main.tablaUsuarios.setItem(row, 2, apellido)
			self.main.tablaUsuarios.setItem(row, 3, correo)
			self.main.tablaUsuarios.setItem(row, 4, telefono)
			row = row + 1
		self.db.close()
	def Reporte(self):
		Guardar = QMessageBox(self)
		CSV = Guardar.addButton("CSV", QMessageBox.ActionRole)
		PDF = Guardar.addButton("PDF", QMessageBox.ActionRole)
		Guardar.setWindowTitle("Guardar Reporte")
		Guardar.setText("Seleccione el formato en que desea guardar el reporte")
		Guardar.exec_()
		if Guardar.clickedButton() == CSV:
			ruta_guardar = ""
			NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
			if NombreArchivo[0]:
				self.db.open()
				file = open(NombreArchivo[0]+'.csv', 'w')
				consulta = QtSql.QSqlQuery()
				consulta.exec_("SELECT * FROM Clientes")
				fieldnames = ["CI_RIF", "Nombre", "Apellido", "Correo", "Telefono"]
				csvsalida = csv.DictWriter(file, fieldnames)
				while consulta.next():
					csvsalida.writerow( { fieldnames[0] : consulta.value(0),
							 fieldnames[1] : consulta.value(1),
							 fieldnames[2] : consulta.value(2),
							 fieldnames[3] : consulta.value(3),
							 fieldnames[4] : consulta.value(4)
							 })
				file.close()
				self.db.close()
			Guardar.close()
		elif Guardar.clickedButton() == PDF:
			ruta_guardar = ""
			NombreArchivo = QFileDialog.getSaveFileName(self, "Guarfar Archivo", ruta_guardar)
			if NombreArchivo[0]:
				self.db.open()
				consulta = QtSql.QSqlQuery()
				consulta.exec_("SELECT * FROM Clientes")
				estiloHoja = getSampleStyleSheet()
				story = []
				cuerpo = estiloHoja["BodyText"]
				cuerpo.alignment=TA_CENTER

				col = ["CI_RIF", "Nombre", "Apellido", "Correo", "Telefono"]
				fil = []
				fil.insert(0, col)
				fila = 1
				while consulta.next():
					fil.insert(fila, [consulta.value(0), consulta.value(1), consulta.value(2), consulta.value(3), consulta.value(4)])
					fila += 1
				datos = [i for i in fil]
				tabla = Table(data=datos,colWidths=[90,60,60,110,80])
				story.append(tabla)
				doc = SimpleDocTemplate(NombreArchivo[0]+'.pdf',pagesize=portrait(LETTER), leftMargin=3, rightMargin=4, topMargin=3, bottomMargin=4)
				doc.build(story)
				self.db.close()
			Guardar.close()
		else:
			Guardar.close()


	def cerrarAgregar(self):
		index = self.main.tabClientes.indexOf(self.main.tabAgregar)
		self.main.tabClientes.removeTab(index)
	def cerrarEstado(self):
		index = self.main.tabClientes.indexOf(self.main.tabEstado)
		self.main.tabClientes.removeTab(index)
	def cerrarModificar(self):
		index = self.main.tabClientes.indexOf(self.main.tabModififcar)
		self.main.tabClientes.removeTab(index)
	def Eliminar(self):
		row = self.main.tablaUsuarios.currentRow()
		print(row)
		if row > -1:
			Pregunta = QMessageBox(self)
			Pregunta.setText("¿Desea eliminar al cliente?")
			SI = Pregunta.addButton("Si", QMessageBox.ActionRole)
			NO = Pregunta.addButton("No", QMessageBox.ActionRole)
			Pregunta.setWindowTitle("Eliminar")
			Pregunta.setIconPixmap(QPixmap("Iconos/pregunta.png"))
			SI.setIcon(QIcon("Iconos/aceptar-ico.png"))
			NO.setIcon(QIcon("Iconos/cancelar.png"))
			Pregunta.exec_()
			if Pregunta.clickedButton() == SI:
				self.db.open()
				consulta = QtSql.QSqlQuery()
				CI_RIF = self.main.tablaUsuarios.item(row, 0).text()
				consulta.exec_("DELETE FROM Clientes WHERE CI_RIF = '%s'" %(CI_RIF))
				consulta.exec_("DELETE FROM AsignarHabitaciones WHERE CI_RIF = '%s'" %(CI_RIF))
				QMessageBox.information(self,"Eliminado", "Cliente eliminado!!!")
				self.db.close()
			else:
				Pregunta.close()
	def CSV(self):
		ruta_guardar = ""
		NombreArchivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", ruta_guardar)
		if NombreArchivo[0]:
			self.db.open()
			file = open(NombreArchivo[0]+'.csv', 'w')
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Clientes")
			fieldnames = ["CI_RIF", "Nombre", "Apellido", "Correo", "Telefono"]
			csvsalida = csv.DictWriter(file, fieldnames)
			while consulta.next():
				csvsalida.writerow( { fieldnames[0] : consulta.value(0),
						 fieldnames[1] : consulta.value(1),
						 fieldnames[2] : consulta.value(2),
						 fieldnames[3] : consulta.value(3),
						 fieldnames[4] : consulta.value(4)
						 })
			file.close()
			self.db.close()
	def PDF(self):
		ruta_guardar = ""
		NombreArchivo = QFileDialog.getSaveFileName(self, "Guarfar Archivo", ruta_guardar)
		if NombreArchivo[0]:
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("SELECT * FROM Clientes")
			estiloHoja = getSampleStyleSheet()
			story = []
			cuerpo = estiloHoja["BodyText"]
			cuerpo.alignment=TA_CENTER

			col = ["CI_RIF", "Nombre", "Apellido", "Correo", "Telefono"]
			fil = []
			fil.insert(0, col)
			fila = 1
			while consulta.next():
				fil.insert(fila, [consulta.value(0), consulta.value(1), consulta.value(2), consulta.value(3), consulta.value(4)])
				fila += 1
			datos = [i for i in fil]
			tabla = Table(data=datos,colWidths=[90,60,60,110,80])
			story.append(tabla)
			doc = SimpleDocTemplate(NombreArchivo[0]+'.pdf',pagesize=portrait(LETTER), leftMargin=3, rightMargin=4, topMargin=3, bottomMargin=4)
			doc.build(story)
			self.db.close()
	def acercaDe(self):
		acerca = AcercaDe(self)
		acerca.show()

#app = QApplication([])
#main = VentanaUsuarios()
#main.show()
#app.exec__()
