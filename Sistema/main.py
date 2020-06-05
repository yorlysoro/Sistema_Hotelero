# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from formularioregistro import FormularioRegistro
from login import Login
from PyQt5 import QtSql
import time
app = QApplication(sys.argv)
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("../BD/Hotel.sqlite3")
def ActualizarEgresos(db):
	db.open()
	ultimaFecha = ""
	fechaActual = time.strftime("%d/%m/%y")
	consulta = QtSql.QSqlQuery()
	consulta.exec_("select Fecha from Egreso")
	while consulta.next():
		ultimaFecha = consulta.value(0)
	dia = fechaActual.split('/')
	if dia[0] == "28":
		if ultimaFecha == fechaActual:
			consulta.exec_("SELECT SUM(Sueldo) FROM Empleados")
			Egreso = 0.0
			while consulta.next():
				Egreso = float(consulta.value(0))
			consulta.exec_("UPDATE Egreso SET Egreso = %f WHERE Fecha = '%s'" %(Egreso, ultimaFecha))
		else:
			consulta.exec_("SELECT SUM(Sueldo) FROM Empleados")
			Egreso = 0.0
			while consulta.next():
				Egreso = float(consulta.value(0))
			consulta.exec_("INSERT INTO Egreso (Fecha, Egreso) VALUES('%s', %f)" %(fechaActual, Egreso))
db.open()
consulta = QtSql.QSqlQuery()
consulta.exec_("select CI_RIF from Registro")
ci = ""
while consulta.next():
	ci = consulta.value(0)
if ci == "":
	Formulario = FormularioRegistro(None, db)
	Formulario.show()
else:
	login = Login(None,db)
	login.show()

ActualizarEgresos(db)
#stl = open("Estilos/Estilos.qss")
#app.setStyleSheet(stl.read())
db.close()
app.exec_()
