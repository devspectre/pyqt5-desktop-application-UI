import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#types for customzied buttons
class BUTTON_TYPE:
	INSTALL = 0
	DELETE = 1
	LAUNCH = 2
	ALL = 3

#predefined styles to stylize the button
class BUTTON_STYLE:
	INSTALL = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(15, 157, 88, 255), stop:1 rgba(55, 157, 88, 225)); border-radius: 3px; padding: 5px 25px 5px 25px}"
	INSTALL_HOVER = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(15, 175, 88, 255), stop:1 rgba(55, 175, 88, 225)); border-radius: 3px; padding: 5px 25px 5px 25px}"
	INSTALL_DOWN = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(15, 195, 88, 255), stop:1 rgba(55, 195, 88, 225)); border-radius: 3px; padding: 5px 25px 5px 25px}"
	DELETE = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(200, 50, 34, 255), stop:1 rgba(200, 50, 34, 225)); border-radius: 3px; padding: 5px 5px 5px 5px}"
	DELETE_HOVER = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(239, 50, 34, 255), stop:1 rgba(239, 50, 34, 225)); border-radius: 3px; padding: 5px 5px 5px 5px}"
	DELETE_DOWN = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(255, 50, 34, 255), stop:1 rgba(255, 50, 34, 225)); border-radius: 3px; padding: 5px 5px 5px 5px}"
	LAUNCH = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(15, 157, 88, 255), stop:1 rgba(15, 157, 88, 225)); border-radius: 3px; padding: 5px 5px 5px 5px}"
	LAUNCH_HOVER = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(15, 175, 88, 255), stop:1 rgba(15, 175, 88, 225)); border-radius: 3px; padding: 5px 5px 5px 5px}"
	LAUNCH_DOWN = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(15, 195, 88, 255), stop:1 rgba(15, 195, 88, 225)); border-radius: 3px; padding: 5px 5px 5px 5px}"
	ALL = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(17, 147, 245, 255), stop:1 rgba(17, 147, 245, 255)); border-radius: 3px; padding: 5px 5px 5px 5px}"
	ALL_HOVER = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(17, 174, 245, 255), stop:1 rgba(17, 174, 245, 255)); border-radius: 3px; padding: 5px 5px 5px 5px}"
	ALL_DOWN = "#Button{color: white;background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(17, 194, 245, 255), stop:1 rgba(17, 194, 245, 255)); border-radius: 3px; padding: 5px 5px 5px 5px}"

class Button(QPushButton):
	"""Button with customized styles"""
	BUTTON_TYPE = BUTTON_TYPE
	Q_ENUM(BUTTON_TYPE)

	BUTTON_STYLE = BUTTON_STYLE
	Q_ENUM(BUTTON_STYLE)

	def __init__(self, text = "", parent = None):
		QPushButton.__init__(self, text, parent)

		self.type = BUTTON_TYPE.INSTALL
		self.shadow = True
		self.shadowEffect = QGraphicsDropShadowEffect()
		self.shadowEffect.setBlurRadius(3)
		self.shadowEffect.setOffset(1, 1)
		self.shadowEffect.setColor(QColor(155, 155, 155))
		self.shadowEffect.setEnabled(self.shadow)

		self.setGraphicsEffect(self.shadowEffect)
		self.setText(text)
		self.setObjectName("Button")
		self.setFont(QFont("Roboto", 10, QFont.Bold))
		self.setCustomStyle()

	#set the button type to install, delete and all
	def setButtonType(self, newtype):
		self.type = newtype
		self.setCustomStyle()

	#set custmoized styles according to the button types
	def setCustomStyle(self):
		if self.type == BUTTON_TYPE.INSTALL:
			self.setStyleSheet(BUTTON_STYLE.INSTALL)
		elif self.type == BUTTON_TYPE.DELETE:
			self.setStyleSheet(BUTTON_STYLE.DELETE)
		elif self.type == BUTTON_TYPE.LAUNCH:
			self.setStyleSheet(BUTTON_STYLE.LAUNCH)
		elif self.type == BUTTON_TYPE.ALL:
			self.setStyleSheet(BUTTON_STYLE.ALL)

		self.setText(self.text().upper())

	#show/hide shadow
	def setShadowEnabled(self, flag):
		self.shadow = flag
		self.shadowEffect.setEnabled(self.shadow)
		self.setCustomStyle()

	#button effect
	def enterEvent(self,event):
		if self.type == BUTTON_TYPE.INSTALL:
			self.setStyleSheet(BUTTON_STYLE.INSTALL_HOVER)
		elif self.type == BUTTON_TYPE.DELETE:
			self.setStyleSheet(BUTTON_STYLE.DELETE_HOVER)
		elif self.type == BUTTON_TYPE.LAUNCH:
			self.setStyleSheet(BUTTON_STYLE.LAUNCH_HOVER)
		elif self.type == BUTTON_TYPE.ALL:
			self.setStyleSheet(BUTTON_STYLE.ALL_HOVER)

	#button effect
	def leaveEvent(self,event):
		if self.type == BUTTON_TYPE.INSTALL:
			self.setStyleSheet(BUTTON_STYLE.INSTALL)
		elif self.type == BUTTON_TYPE.DELETE:
			self.setStyleSheet(BUTTON_STYLE.DELETE)
		elif self.type == BUTTON_TYPE.LAUNCH:
			self.setStyleSheet(BUTTON_STYLE.LAUNCH)
		elif self.type == BUTTON_TYPE.ALL:
			self.setStyleSheet(BUTTON_STYLE.ALL)

		if self.shadow:
			self.shadowEffect.setEnabled(True)

	#button effect
	def mousePressEvent(self, event):
		QPushButton.mousePressEvent(self, event)
		if self.type == BUTTON_TYPE.INSTALL:
			self.setStyleSheet(BUTTON_STYLE.INSTALL_DOWN)
		elif self.type == BUTTON_TYPE.DELETE:
			self.setStyleSheet(BUTTON_STYLE.DELETE_DOWN)
		elif self.type == BUTTON_TYPE.LAUNCH:
			self.setStyleSheet(BUTTON_STYLE.LAUNCH_DOWN)
		elif self.type == BUTTON_TYPE.ALL:
			self.setStyleSheet(BUTTON_STYLE.ALL_DOWN)

		if self.shadow:
			self.shadowEffect.setEnabled(False)
		

	#button effect
	def mouseReleaseEvent(self, event):
		QPushButton.mouseReleaseEvent(self, event)	
		if self.type == BUTTON_TYPE.INSTALL:
			self.setStyleSheet(BUTTON_STYLE.INSTALL)
		elif self.type == BUTTON_TYPE.DELETE:
			self.setStyleSheet(BUTTON_STYLE.DELETE)
		elif self.type == BUTTON_TYPE.LAUNCH:
			self.setStyleSheet(BUTTON_STYLE.LAUNCH)
		elif self.type == BUTTON_TYPE.ALL:
			self.setStyleSheet(BUTTON_STYLE.ALL)

		if self.shadow:
			self.shadowEffect.setEnabled(True)	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	button = Button("Launch", widget)
	button.setButtonType(BUTTON_TYPE.LAUNCH)
	widget.show()
	sys.exit(app.exec())