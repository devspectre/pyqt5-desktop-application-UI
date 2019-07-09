import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from autotreewidget import AutoTreeWidget
from clickablelabel import ClickableLabel

class ProductView(QFrame):
	""" Customized widget derived from QFrame which contains a caption and a treewidget"""
	stateChanged = pyqtSignal(int, str)

	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.setObjectName("Main")
		self.setStyleSheet("#Main{background-color: #f1f1f1}")

		self.currentItem = ""
		self.currentId = -1
		self.itemsVisible = True

		self.caption = ClickableLabel("Products", self)
		self.caption.setFont(QFont("Comic Sans MS", 16))
		self.caption.setObjectName("Caption")
		self.caption.setContentsMargins(10, 5, 10, 5)
		self.caption.clicked.connect(self.onCaptionClicked)

		self.list = AutoTreeWidget(self)
		self.list.setObjectName("List")
		self.list.setStyleSheet("#List{background-color: rgba(0, 0, 0, 0); selection-background-color: transparent}")
		self.list.setColumnCount(2)
		self.list.setColumnHidden(1, True)
		self.list.header().hide()
		self.list.setFrameShape(QFrame.NoFrame)
		self.list.itemClicked.connect(self.itemClicked)

		self.layout = QVBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignTop)

		self.layout.addWidget(self.caption)
		self.layout.addWidget(self.list)
		self.setLayout(self.layout)

	# show/hide treewidget on caption click
	def onCaptionClicked(self):
		self.caption.setFixedWidth(self.width())
		#self.caption.setFixedHeight(self.height())
		self.itemsVisible = not self.itemsVisible
		self.list.setVisible(self.itemsVisible)

	# emit a signal once an item on treewidget is selected
	def itemClicked(self):
		self.currentItem = self.list.currentItem().data(0, 0)
		self.currentId = int(self.list.currentItem().data(1, 0))
		# emit signal here
		self.stateChanged.emit(self.currentId, self.currentItem)
		
	# add items to the treewidget with a list of strings
	def addList(self, iList):
		for i in iList:
			parent = QTreeWidgetItem(self.list)
			parent.setText(0, i[0][0])
			parent.setText(1, i[0][1])
			parent.setExpanded(True)
			# parent.setChildIndicatorPolicy(QTreeWidgetItem.DontShowIndicator)
			for x in i[1:]:
				child = QTreeWidgetItem(parent)
				child.setText(0, x[0])
				child.setText(1, x[1])
		self.list.show()

	# set font for caption
	def setCaptionFont(self, font):
		self.caption.setFont(font)

	# set font for items on treewidget
	def setListFont(self, font):
		self.list.setFont(font)

	# automatically adjust 
	def autoAdjust(self):
		self.list.autoAdjust()
		self.list.setFixedWidth(self.width())

if __name__ == '__main__':
	def onProductClicked(value):
		QMessageBox.information(None, "Prodcut", str(value))

	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	tree = ProductView(widget)
	tree.setAutoFillBackground(True)
	tree.setGeometry(0, 0, 300, 200)
	plist = [[['Web Apps','1'], ['React', '2'],['Vue.js', '3']], 
			[['Add-Ins', '4'],['Dynamics 365', '5'], ['Office 365', '6'],
			 ['Power BI apps', '7'], ['Power BI visuals', '8'], ['Dynamics NAV', '9']]]
	tree.addList(plist)
	tree.setListFont(QFont("Comic Sans MS", 12))
	tree.setCaptionFont(QFont("Dubai", 20))
	tree.autoAdjust()

	tree.productItemClicked.connect(onProductClicked)
	widget.show()
	sys.exit(app.exec())