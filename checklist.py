import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from idcheckbox import IDCheckBox
from elidelabel import ElideLabel
from clickablelabel import ClickableLabel

# state enums
class CHECK_STATE:
	UNCHECKED = 0
	CHECKED = 1

class CheckList(QFrame):
	""" Checklist derived from QFrame which contains Filter Category as its caption and list of checkable items"""
	stateChanged = pyqtSignal(int, int)
	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.itemVisible = True

		self.setObjectName("Main")
		self.setStyleSheet("#Main{background-color: #f1f1f1}")

		self.caption = ClickableLabel("Undefined", self)
		self.caption.setFont(QFont("Comic Sans MS", 16))
		self.caption.setObjectName("Caption")
		self.caption.setContentsMargins(10, 5, 10, 5)
		self.caption.clicked.connect(self.onCaptionClicked)

		self.list = []
		self.listFont = QFont("Arial", 8)

		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.setAlignment(Qt.AlignTop)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.listFrame = QFrame(self)

		self.listLayout = QVBoxLayout(self.listFrame)
		self.listLayout.setContentsMargins(10, 5, 0, 5)
		self.listLayout.setSpacing(10)
		self.listLayout.setAlignment(Qt.AlignLeft)

		self.mainLayout.addWidget(self.caption)
		self.mainLayout.addWidget(self.listFrame)

	# emit a signal with two params when any checkable item is changed by state
	@pyqtSlot(int, int)
	def onItemStateChanged(self, cid, cstate):
		self.stateChanged.emit(cid, cstate)

	# show or hide all checkable items on caption click
	@pyqtSlot()
	def onCaptionClicked(self):
		self.caption.setFixedWidth(self.width())
		self.caption.setFixedHeight(self.caption.height())
		self.itemVisible = not self.itemVisible
		if self.itemVisible:
			self.listFrame.show()
		else:
			self.listFrame.hide()

	# add an item with its id and text
	def addNewItem(self, newid, text = "Undefined"):
		newItem = IDCheckBox(text, self, newid)
		newItem.setFont(self.listFont)
		newItem.stateChangedOnItem.connect(self.onItemStateChanged)
		self.list.append(newItem)
		self.listLayout.addWidget(newItem)

	# read from a list and add items
	def addList(self, ilist):
		for i in ilist:
			self.addNewItem(int(i[1]), str(i[0]))

	# remove items by id
	def removeItemById(self, id):
		for item in self.list:
			if item.getID() == id:
				list.remove(item)

	# remove items by text
	def removeItemByText(self, text):
		for item in self.list:
			if item.text() == text:
				list.remove(item)

	# set filter category caption
	def setCaption(self, cap):
		self.caption.setText(cap)

	# return filter category caption
	def getCaption(self):
		return self.caption.text()

	# set font of caption
	def setCaptionFont(self, font):
		self.caption.setFont(font)

	# set font of checkable items
	def setListFont(self, font):
		self.listFont = font
		for item in self.list:
			item.setFont(self.listFont)

	# note: call after setListFont
	def getMaximumItemWidth(self):
		maxWidth = 0
		for item in self.list:
			if item.width() > maxWidth:
				maxWidth = item.width()
		#print(maxWidth)
		return maxWidth

	# note: call after setListFont
	def autoAdjust(self):
		ml, mt, mr, mb = self.mainLayout.getContentsMargins()
		msp = self.mainLayout.spacing()
		lsp = self.listLayout.spacing()

		for item in self.list:
			item.setElideMode(0)
			item.autoAdjust()

if __name__ == '__main__':
	def onCheckItemClicked(cid, state):
		QMessageBox.information(None, "Check", str(cid) + ":" + str(state))

	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	clist = CheckList(widget)
	clist.setCaption("Categories")
	clist.setAutoFillBackground(True)
	clist.setGeometry(0, 0, 200, 200)
	plist = [['Analytics','1'], ['Artificial Intelligence', '2'],['Collaboration', '3'], 
			['Customer service', '4'],['Finance', '5'], ['Human resources', '6'],
			 ['IT + administration', '7'], ['Internet of things', '8'], ['Marketing', '9'],
			 ['Operations + supply', '10'], ['Productivity', '11'], ['Sales', '12']]
	clist.addList(plist)
	clist.setListFont(QFont("Comic Sans MS", 10))
	clist.setCaptionFont(QFont("Dubai", 16))
	clist.autoAdjust()

	clist.stateChanged.connect(onCheckItemClicked)

	widget.show()
	sys.exit(app.exec())

	
