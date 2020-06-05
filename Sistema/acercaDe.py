# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QIcon
from acercaDeWin import Ui_acercaDeWin

class AcercaDe(QDialog):
	def __init__(self, padre=None):
		QDialog.__init__(self, padre)
		self.dialog = Ui_acercaDeWin()
		self.dialog.setupUi(self)
		self.setWindowTitle("Informacion")
		self.setWindowIcon(QIcon("Iconos/estrella.png"))
		self.setModal(False)
