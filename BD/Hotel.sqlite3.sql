BEGIN TRANSACTION;
CREATE TABLE `Turnos` (
	`N°`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`CI_RIF`	TEXT NOT NULL,
	`Hora_Inicio`	TEXT NOT NULL,
	`Hora_Fin`	TEXT NOT NULL,
	`Fecha`	TEXT NOT NULL
);
CREATE TABLE `Registro` (
	`Usuario`	TEXT NOT NULL,
	`Contrasena`	TEXT NOT NULL,
	`Nombre`	TEXT NOT NULL,
	`Apellido`	TEXT NOT NULL,
	`CI_RIF`	TEXT NOT NULL,
	`Direccion`	TEXT NOT NULL,
	`Correo`	TEXT NOT NULL,
	`Hotel`	TEXT NOT NULL,
	`Direccion_Hotel`	TEXT NOT NULL
);
CREATE TABLE `Ingresos` (
	`N°`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Fecha`	TEXT NOT NULL,
	`Ingreso`	REAL NOT NULL
);
CREATE TABLE `Habitaciones` (
	`Numero_Codigo`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Piso`	INTEGER NOT NULL,
	`Estado`	TEXT NOT NULL,
	`Capacidad`	INTEGER NOT NULL,
	`Asignado`	INTEGER NOT NULL
);
INSERT INTO `Habitaciones` VALUES (1,1,'Desocupada',4,0);
INSERT INTO `Habitaciones` VALUES (2,1,'Desocupada',1,0);
INSERT INTO `Habitaciones` VALUES (3,1,'Desocupada',3,0);
INSERT INTO `Habitaciones` VALUES (4,1,'Desocupada',2,0);
INSERT INTO `Habitaciones` VALUES (5,2,'Desocupada',2,0);
INSERT INTO `Habitaciones` VALUES (6,2,'Desocupada',1,0);
INSERT INTO `Habitaciones` VALUES (7,2,'Desocupada',3,0);
INSERT INTO `Habitaciones` VALUES (8,2,'Desocupada',2,0);
INSERT INTO `Habitaciones` VALUES (9,3,'Desocupada',4,0);
INSERT INTO `Habitaciones` VALUES (10,3,'Desocupada',1,0);
INSERT INTO `Habitaciones` VALUES (11,3,'Desocupada',1,0);
INSERT INTO `Habitaciones` VALUES (12,3,'Desocupada',2,0);
CREATE TABLE `Empleados` (
	`CI_RIF`	TEXT NOT NULL,
	`Nombre`	TEXT NOT NULL,
	`Apellido`	TEXT NOT NULL,
	`Correo`	TEXT NOT NULL,
	`Telefono`	TEXT NOT NULL,
	`Direccion`	TEXT NOT NULL,
	`Sueldo`	REAL NOT NULL,
	PRIMARY KEY(`CI_RIF`)
);
CREATE TABLE `Egreso` (
	`N°`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Fecha`	TEXT NOT NULL,
	`Egreso`	REAL NOT NULL
);
CREATE TABLE `Clientes` (
	`CI_RIF`	TEXT NOT NULL,
	`Nombre`	TEXT NOT NULL,
	`Apellido`	TEXT NOT NULL,
	`Correo`	TEXT NOT NULL,
	`Telefono`	TEXT NOT NULL,
	PRIMARY KEY(`CI_RIF`)
);
CREATE TABLE `CantClientes` (
	`N°`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Fecha`	TEXT NOT NULL,
	`Cantida`	INTEGER NOT NULL
);
CREATE TABLE `AsignarHabitaciones` (
	`N°`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`CI_RIF`	TEXT NOT NULL,
	`Habitacion`	INTEGER NOT NULL,
	`Fecha_Entrada`	TEXT NOT NULL,
	`Fecha_Salida`	TEXT NOT NULL,
	`Costo_Dia`	REAL NOT NULL,
	`Total`	REAL NOT NULL
);
COMMIT;
