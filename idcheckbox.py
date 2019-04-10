from PyQt5.QtWidgets import QCheckBox, QStyle
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

class IDCheckBox(QCheckBox):
	"""Checkbox derived from QCheckBox which emits both its ID and current state"""
	stateChangedOnItem = pyqtSignal(int, int)
	
	@pyqtSlot(int)
	def redirectStateChangedSignal(self, state):
		self.stateChangedOnItem.emit(self.id, state)

	def __init__(self, text = "Undefined", parent = None, id = -1):
		QCheckBox.__init__(self, parent)

		self.id = id
		self.elideMode = 0
		self.textOrg = text
		self.setObjectName("CheckBox")
		self.setStyleSheet("#CheckBox{spacing: 9px}")
		self.stateChanged.connect(self.redirectStateChangedSignal)

	def setText(self, txt):
		QCheckBox.setText(self, txt)
		self.textOrg = txt

	def text(self):
		return self.textOrg

	def getID(self):
		return self.id

	def setID(self, newid):
		if newid != self.id:
			self.id = newid

	#to prevent text overflowing
	def setElideMode(self, mode):
		self.elideMode = mode

	#return current elide mode
	def getElideMode(self):
		return self.elideMode

	#set text font and elide the text
	def setFont(self, font):
		QCheckBox.setFont(self, font)
		if self.elideMode == 1:
			elidedText = self.fontMetrics().elidedText(self.text(), Qt.ElideRight, self.width() - QStyle.PM_IndicatorWidth)
			self.setText(elidedText)
		else:
			self.setText(self.textOrg)
		self.autoAdjust()

	#adjust widget size
	def autoAdjust(self):
		ml, mt, mr, mb = self.getContentsMargins()
		recommendWidth = self.fontMetrics().width(self.text()) + 10 + ml + mr + QStyle.PM_IndicatorWidth
		#print(recommendWidth)
		if (self.width() < recommendWidth):
			self.setFixedWidth(recommendWidth)

		recommendHeight = self.fontMetrics().height() + 5
		if self.height() < recommendHeight:
			self.setFixedHeight(recommendHeight)
		