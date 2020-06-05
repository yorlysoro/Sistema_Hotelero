# -*- coding: utf-8 -*-
import re
class Validaciones(object):
	def __init__(self, ventana=None):
		self.ventana = ventana
	def validar_correo(self):
		correo = self.ventana.leCorreo.text()
		validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', correo, re.I)
		if correo == "":
			self.ventana.leCorreo.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leCorreo.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leCorreo.setStyleSheet("border: 4px solid green;")
			return True
	
	def validar_usuario(self):
		usuario = self.ventana.leUsuario.text()
		validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', usuario, re.I)
		if usuario == "":
			self.ventana.leUsuario.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leUsuario.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leUsuario.setStyleSheet("border: 4px solid green;")
			return True
	
	def validar_contrasena(self):
		contrasena = self.ventana.leContrasena.text()
		if contrasena == "":
			self.ventana.leContrasena.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leContrasena.setStyleSheet("border: 4px solid green;")
			return True
	
	def validar_nombre(self):
		nombre = self.ventana.leNombre.text()
		validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
		if nombre == "":
			self.ventana.leNombre.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leNombre.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leNombre.setStyleSheet("border: 4px solid green;")
			return True
	
	def validar_apellido(self):
		apellido = self.ventana.leApellido.text()
		validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', apellido, re.I)
		if apellido == "":
			self.ventana.leApellido.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leApellido.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leApellido.setStyleSheet("border: 4px solid green;")
			return True
	
	def validar_cedula(self):
		cedula = self.ventana.leCI_RIF.text()
		validar = re.match('^[V|J|0-9]+$', cedula, re.I)
		if cedula == "":
			self.ventana.leCI_RIF.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leCI_RIF.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leCI_RIF.setStyleSheet("border: 4px solid green;")
			return True
	def validar_cedula_2(self):
		cedula = self.ventana.leCI_RIF_2.text()
		validar = re.match('^[V|J|0-9]+$', cedula, re.I)
		if cedula == "":
			self.ventana.leCI_RIF_2.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leCI_RIF_2.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leCI_RIF_2.setStyleSheet("border: 4px solid green;")
			return True
	def validar_cedula_3(self):
		cedula = self.ventana.leCI_RIF_3.text()
		validar = re.match('^[V|J|0-9]+$', cedula, re.I)
		if cedula == "":
			self.ventana.leCI_RIF_3.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leCI_RIF_3.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leCI_RIF_3.setStyleSheet("border: 4px solid green;")
			return True
	def validar_direccion(self):
		direccion = self.ventana.leDireccion.toPlainText()
		if direccion == "":
			self.ventana.leDireccion.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leDireccion.setStyleSheet("border: 4px solid green;")
			return True
	
	def validar_hotel(self):
		hotel = self.ventana.leHotel.text()
		if hotel == "":
			self.ventana.leHotel.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leHotel.setStyleSheet("border: 4px solid green;")
			return True
	
	def validar_direccion_hotel(self):
		direccion = self.ventana.leDireccion_Hotel.toPlainText()
		if direccion == "":
			self.ventana.leDireccion_Hotel.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leDireccion_Hotel.setStyleSheet("border: 4px solid green;")
			return True
	def validar_telefono(self):
		telefono = self.ventana.leTelefono.text()
		validar = re.match('^[0-9]+$', telefono, re.I)
		if telefono == "":
			self.ventana.leTelefono.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leTelefono.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leTelefono.setStyleSheet("border: 4px solid green;")
			return True
	def validar_sueldo(self):
		sueldo = self.ventana.leSueldo.text()
		validar = re.match('^[0-9\._0-9]+$', sueldo, re.I)
		if sueldo == "":
			self.ventana.leSueldo.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leSueldo.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leSueldo.setStyleSheet("border: 4px solid green;")
			return True

	def validar_habitacion(self):
		habitacion = self.ventana.leHabitacion.text()
		if habitacion == "":
			self.ventana.leHabitacion.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leHabitacion.setStyleSheet("border: 4px solid green;")
			return True
	def validar_costo(self):
		costo = self.ventana.leCostoDia.text()
		validar = re.match('^[0-9\._0-9]+$', costo, re.I)
		if costo == "":
			self.ventana.leCostoDia.setStyleSheet("border: 4px solid yellow;")
			return False
		elif not validar:
			self.ventana.leCostoDia.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.leCostoDia.setStyleSheet("border: 4px solid green;")
			return True
	def validar_direccion_2(self):
		direccion = self.ventana.teDireccion.toPlainText()
		if direccion == "":
			self.ventana.teDireccion.setStyleSheet("border: 4px solid red;")
			return False
		else:
			self.ventana.teDireccion.setStyleSheet("border: 4px solid green;")
			return True
	
