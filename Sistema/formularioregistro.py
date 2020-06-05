from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5.QtGui import QIcon
from formularioregistrowin import Ui_FormularioRegistroWin
from Validaciones import Validaciones
from login import Login
from PyQt5 import QtSql
class FormularioRegistro(QMainWindow):
	def __init__(self, padre=None, db=None):
		QMainWindow.__init__(self, padre)
		self.ventana = Ui_FormularioRegistroWin()
		self.ventana.setupUi(self)
		self.validacion = Validaciones(self.ventana)
		self.db = db
		self.ventana.leCorreo.textChanged.connect(self.validacion.validar_correo)
		self.ventana.leUsuario.textChanged.connect(self.validacion.validar_usuario)
		self.ventana.leContrasena.textChanged.connect(self.validacion.validar_contrasena)
		self.ventana.leNombre.textChanged.connect(self.validacion.validar_nombre)
		self.ventana.leApellido.textChanged.connect(self.validacion.validar_apellido)
		self.ventana.leCI_RIF.textChanged.connect(self.validacion.validar_cedula)
		self.ventana.leDireccion.textChanged.connect(self.validacion.validar_direccion)
		self.ventana.leDireccion_Hotel.textChanged.connect(self.validacion.validar_direccion_hotel)
		self.ventana.leHotel.textChanged.connect(self.validacion.validar_hotel)
		self.ventana.btnRegistrar.clicked.connect(self.Registrar)
		self.setWindowTitle("Registro")
		self.setWindowIcon(QIcon("Iconos/archivo.png"))
	
	def Registrar(self):
		if self.validacion.validar_correo() and self.validacion.validar_usuario() and self.validacion.validar_contrasena() and self.validacion.validar_nombre() and self.validacion.validar_apellido() and self.validacion.validar_cedula() and self.validacion.validar_direccion() and self.validacion.validar_direccion_hotel and self.validacion.validar_hotel():
			self.db.open()
			consulta = QtSql.QSqlQuery()
			consulta.exec_("insert into Registro values('%s', '%s' , '%s', '%s', %d, '%s', '%s', '%s', '%s')" % (self.ventana.leUsuario.text(), self.ventana.leContrasena.text(), self.ventana.leNombre.text(), self.ventana.leApellido.text(), int(self.ventana.leCI_RIF.text()), self.ventana.leDireccion.toPlainText(), self.ventana.leCorreo.text(), self.ventana.leHotel.text(), self.ventana.leDireccion_Hotel.toPlainText()))
			self.setVisible(False)
			login = Login(self, self.db)
			login.show()
		else:
			QMessageBox.warning(self, "Error!", "Faltan datos en el formulario", QMessageBox.Ok)
	

#app = QApplication([])
#window = FormularioRegistro(None)
#window.show()
#app.exec()
