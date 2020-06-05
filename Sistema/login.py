# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5 import QtSql
from PyQt5.QtGui import QIcon
from loginWin import Ui_loginWin
from Validaciones import Validaciones
from acercaDe import AcercaDe
from sistema import Sistema


class Login(QMainWindow):
	def __init__(self, padre=None, db=None):
		QMainWindow.__init__(self, padre)
		self.window = Ui_loginWin()
		self.window.setupUi(self)
		self.validacion = Validaciones(self.window)
		self.db = db
		self.window.btnAcercaDe.clicked.connect(self.muestraAcerca)
		self.window.btnIngresar.clicked.connect(self.Ingresar)
		self.window.leUsuario.textChanged.connect(self.validacion.validar_usuario)
		self.window.leContrasena.textChanged.connect(self.validacion.validar_contrasena)
		self.setWindowTitle("Ingreso al Sistema")
		self.setWindowIcon(QIcon("Iconos/clave.png"))
		self.setFixedSize(366, 143)
	def muestraAcerca(self):
		self.acercaDe = AcercaDe(self)
		self.acercaDe.show()


	def Ingresar(self):
		if self.validacion.validar_usuario() and self.validacion.validar_contrasena():
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("select Usuario, Contrasena from Registro")
			while consulta.next():
				if self.window.leUsuario.text() == consulta.value(0) and self.window.leContrasena.text() == consulta.value(1):
					self.setVisible(False)
					self.db.close()
					sistema = Sistema(self,self.db)
					sistema.show()
				elif self.window.leUsuario.text() != consulta.value(0) and self.window.leContrasena.text() != consulta.value(1):
					QMessageBox.warning(self, "Acceso Denegado", "Usuario y contraseña incorrectos!!!", QMessageBox.Ok)
				elif self.window.leUsuario.text() != consulta.value(0):
					QMessageBox.warning(self, "Acceso Denegado", "El usuario no existe!!!", QMessageBox.Ok)
				else:
					QMessageBox.warning(self, "Acceso Denegado", "La contraseña es incorrecta!!!", QMessageBox.Ok)
		else:
			if not self.window.leUsuario.text() and not self.window.leContrasena.text():
				QMessageBox.warning(self, "Error!!!", "No ha llenado ninguno de los campos!!!", QMessageBox.Ok)
			else:
				if not self.window.leContrasena.text():
					QMessageBox.warning(self, "Error!!!", "Falta la contraseña!!!", QMessageBox.Ok)
				else:
					QMessageBox.warning(self, "Error!!!", "Falta el usuario!!!", QMessageBox.Ok)
				

#app = QApplication([])
#window = Login(None)
#window.show()
#app.exec_()


