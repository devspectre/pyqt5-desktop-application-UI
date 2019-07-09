import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class ClickableLabel(QLabel):
	""" A widget derived from QLabel for category or filter caption and is clickable"""
	clicked = pyqtSignal()
	def __init__(self, text = "", parent = None):
		QLabel.__init__(self, text, parent)
		self.pressed = False
		self.setObjectName("#Caption")
		self.setStyleSheet("""#Caption{color: #ff8c00; background-color: #e7e7e7}
			#Caption:hover{background-color: #d7d7d7}""")

	# override mousePressEvent
	def mousePressEvent(self, event):
		QLabel.mousePressEvent(self, event)
		self.pressed = True

	# override mouseReleaseEvent
	def mouseReleaseEvent(self, event):
		QLabel.mouseReleaseEvent(self, event)
		if self.pressed:
			self.clicked.emit()
