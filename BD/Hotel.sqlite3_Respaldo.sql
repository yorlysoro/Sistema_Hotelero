BEGIN TRANSACTION;
CREATE TABLE `Turnos` (
	`N°`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`CI_RIF`	TEXT NOT NULL,
	`Hora_Inicio`	TEXT NOT NULL,
	`Hora_Fin`	TEXT NOT NULL,
	`Fecha`	TEXT NOT NULL
);
INSERT INTO `Turnos` VALUES (1,'V14236954','8:00 A. M.','10:00 A. M.','24/11/17');
INSERT INTO `Turnos` VALUES (2,'V14236954','11:00 A. M.','1:00 P. M.','24/11/17');
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
INSERT INTO `Registro` VALUES ('Yorlys','25142034','Yorlys','Oropeza','25142034','Carora','yorlysoro@gmail.com','Hotel La Estancia','Cabudare');
CREATE TABLE `Ingresos` (
	`N°`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Fecha`	TEXT NOT NULL,
	`Ingreso`	REAL NOT NULL
);
INSERT INTO `Ingresos` VALUES (1,'24/11/17',75000.0);
INSERT INTO `Ingresos` VALUES (2,'24/11/17',75000.0);
INSERT INTO `Ingresos` VALUES (3,'24/11/17',75000.0);
INSERT INTO `Ingresos` VALUES (4,'24/11/17',75000.0);
INSERT INTO `Ingresos` VALUES (5,'24/11/17',100000.0);
INSERT INTO `Ingresos` VALUES (6,'24/11/17',100000.0);
INSERT INTO `Ingresos` VALUES (7,'24/11/17',100000.0);
INSERT INTO `Ingresos` VALUES (8,'28/11/17',20000.0);
CREATE TABLE `Habitaciones` (
	`Numero_Codigo`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Piso`	INTEGER NOT NULL,
	`Estado`	TEXT NOT NULL,
	`Capacidad`	INTEGER NOT NULL,
	`Asignado`	INTEGER NOT NULL
);
INSERT INTO `Habitaciones` VALUES (1,1,'Ocupada',4,2);
INSERT INTO `Habitaciones` VALUES (2,1,'Ocupada',1,1);
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
INSERT INTO `Empleados` VALUES ('V14236954','Jose','Rodriguez','joserodriguez@gmail.com','04161325696','Carora Estado Lara',200000.0);
INSERT INTO `Empleados` VALUES ('V15885963','Carlos','Rodriguez','joserodriguez@hotmail.com','04161235896','Carora Estado Lara',200000.0);
INSERT INTO `Empleados` VALUES ('V7658963','Juan','Fernandez','juanfernandez@gmail.com','04148596331','Carora Estado Lara',200000.0);
INSERT INTO `Empleados` VALUES ('V14855746','Jose','Perez','joseperez1234@gmail.com','04145896932','Barquisimeto Estado Lara',200000.0);
INSERT INTO `Empleados` VALUES ('V12369854','Andrez','Fernandez','andrezfernandez1325@gmail.com','04268596321','Barquisimeto Estado Lara',200000.0);
INSERT INTO `Empleados` VALUES ('V21236589','Alicia','Garcia','alicia_garci1425@gmail.com','04128547963','Carora Estado Lara',200000.0);
INSERT INTO `Empleados` VALUES ('V4856985','Juana','Mendez','juanamendez@hotmail.com','04125863214','Barquisimeto Estado Lara',200000.0);
CREATE TABLE `Egreso` (
	`N°`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Fecha`	TEXT NOT NULL,
	`Egreso`	REAL NOT NULL
);
INSERT INTO `Egreso` VALUES (1,'28/11/17',1400000.0);
CREATE TABLE `Clientes` (
	`CI_RIF`	TEXT NOT NULL,
	`Nombre`	TEXT NOT NULL,
	`Apellido`	TEXT NOT NULL,
	`Correo`	TEXT NOT NULL,
	`Telefono`	TEXT NOT NULL,
	PRIMARY KEY(`CI_RIF`)
);
INSERT INTO `Clientes` VALUES ('V25142034','Yorlys','Oropeza','yorlysoro@gmail.com','04261316285');
INSERT INTO `Clientes` VALUES ('J12345876900','Juan','Perez','juanperez@gmail.com','04162587896');
INSERT INTO `Clientes` VALUES ('V14258965','Andres','Perez','andresp@gmail.com','04145896358');
INSERT INTO `Clientes` VALUES ('v28524785','Juana','Escalona','juanaescalo123@hotmail.com','04168523698');
INSERT INTO `Clientes` VALUES ('V25478965','Jose','Roca','joseroca145@hotmail.com','04147859632');
INSERT INTO `Clientes` VALUES ('V15478963','Carlos','Rodriguez','carlosrodriguez1478@gmail.com','04125893254');
INSERT INTO `Clientes` VALUES ('V14875963','Maria','Escalona','maria_escalona147@gmail.com','04128574963');
INSERT INTO `Clientes` VALUES ('V18963854','Marta','Garcia','martagarcia_145@gmail.com','04148574236');
INSERT INTO `Clientes` VALUES ('V12222145','Jhonny','Perez','Jhonny_Pe1230@gmail.com','04168514796');
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
INSERT INTO `AsignarHabitaciones` VALUES (1,'V25142034',1,'24/11/17','25/11/17',25000.0,25000.0);
INSERT INTO `AsignarHabitaciones` VALUES (4,'J12345876900',1,'24/11/17','26/11/17',25000.0,50000.0);
INSERT INTO `AsignarHabitaciones` VALUES (8,'V14258965',2,'29/11/17','30/11/17',20000.0,20000.0);
COMMIT;
