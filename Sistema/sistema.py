from sistemawin import Ui_sistemawin
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtSql
from PyQt5.QtGui import QIcon
from ventanausuarios import VentanaUsuarios
from ventanahotel import VentanaHotel
from ventanaempleados import VentanaEmpleados
from ventanahabitaciones import VentanaHabitaciones
from  acercaDe import AcercaDe
class Sistema(QMainWindow):
	def __init__(self, padre=None, db=None):
		QMainWindow.__init__(self, padre)
		self.main = Ui_sistemawin()
		self.main.setupUi(self)
		self.main.btnClientes.clicked.connect(self.Clientes)
		self.main.btnEmpleados.clicked.connect(self.Empleados)
		self.main.btnHabitaciones.clicked.connect(self.Habitaciones)
		self.main.btnHotel.clicked.connect(self.Hotel)
		self.main.actionAcercaDe.triggered.connect(self.acercaDe)
		self.db = db
		self.db.open()
		consulta = QtSql.QSqlQuery()
		consulta.exec_("SELECT Hotel FROM Registro")
		Titulo = ""
		while consulta.next():
			Titulo = consulta.value(0)
		self.main.gbSistema.setTitle(Titulo)
		self.setWindowTitle(Titulo)
		self.setWindowIcon(QIcon("Iconos/hotel.png"))
		self.main.actionAcercaDe.setIcon(QIcon("Iconos/estrella.png"))
		self.setFixedSize(447, 187)
	def Clientes(self):
		 Clientes = VentanaUsuarios(self, self.db)
		 Clientes.show()
	def Empleados(self):
		Empleado = VentanaEmpleados(self, self.db)
		Empleado.show()
	def Habitaciones(self):
		Habitaciones = VentanaHabitaciones(self, self.db)
		Habitaciones.show()
	def Hotel(self):
		Hotel = VentanaHotel(self, self.db)
		Hotel.show()
	def acercaDe(self):
		acerca = AcercaDe(self)
		acerca.show()
#app = QApplication([])
#window = Sistema(None)
#window.show()
#app.exec_()
