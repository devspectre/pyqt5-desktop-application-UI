import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QPushButton, QApplication, QLabel, QBoxLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox, QGraphicsDropShadowEffect
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont , QPixmap, QImage, QPalette, QBrush, QColor
from appcard import AppCard
from button import Button

class CardFrame(QFrame):
	"""CardFrame widget derived from QFrame which contains category caption,<See All> button, and lots of cards"""
	def __init__(self, parent=None):
		QFrame.__init__(self, parent)

		self.cardList = []
		self.maxColCount = 3
		self.seeAll = True

		self.setObjectName("CardFrame")
		self.setStyleSheet("#CardFrame{background-color: white;}")

		#Category name for the frame
		self.caption = QLabel("Web apps", self)
		self.caption.setFont(QFont("Roboto", 16, QFont.Bold))

		#Button to show/hide cards
		self.btnAll = Button("See all", self)
		self.btnAll.setButtonType(Button.BUTTON_TYPE.ALL)
		self.btnAll.clicked.connect(self.onSeeAll)

		if self.seeAll:
			self.btnAll.setText("SEE ONE ROW")
		else:
			self.btnAll.setText("SEE ALL")


		self.mainLayout = QVBoxLayout(self)

		self.headerLayout = QHBoxLayout()

		self.cardLayout = QGridLayout()
		self.cardLayout.setAlignment(Qt.AlignLeft)
		#self.cardLayout.setHorizontalSpacing(20)
		self.cardLayout.setVerticalSpacing(30)
		self.cardLayout.setContentsMargins(5, 10, 5, 10)

		self.headerLayout.addWidget(self.caption, 0, Qt.AlignLeft)
		self.headerLayout.addWidget(self.btnAll, 0, Qt.AlignRight)

		self.mainLayout.addLayout(self.headerLayout)
		self.mainLayout.addLayout(self.cardLayout)

	#method for adding app cards to the frame itself
	#Note: Be carefull to set the app ID so that it won't be repeated.
	def addNewApp(self, appid, appname, icon = "default", background = "default", devname = "Unknown", desc = "Undefined", rating = 0, feedback = 0, state = 0):
		tmpCard = AppCard(self)
		tmpCard.setAutoFillBackground(True)
		tmpCard.setAppId(appid)
		tmpCard.setAppName(appname)

		if icon == "default":
			tmpCard.setAppIcon(QPixmap("./img/card/bird.png"))
		else:
			tmpCard.setAppIcon(icon)

		if background == "default":
			tmpCard.setBackgroundImage("./img/card/card_back.png")
		else:
			tmpCard.setBackgroundImage(background)

		tmpCard.setAppDevName(devname)
		tmpCard.setAppDesc(desc)
		tmpCard.setAppRating(rating, feedback)
		tmpCard.setAppState(state)

		#calculate row & col for the gridlayout based on maximum column count
		row, col = len(self.cardList) / self.maxColCount, len(self.cardList) % self.maxColCount
		self.cardLayout.addWidget(tmpCard, row, col)
		self.cardList.append(tmpCard)
		self.updateSeeAllButtonState()

	#please make sure you are not duplicating with the same AppCard.appId
	def addCard(self, card):
		row, col = len(self.cardList) / self.maxColCount, len(self.cardList) % self.maxColCount
		self.cardLayout.addWidget(card, row, col)
		self.cardList.append(card)
		self.updateSeeAllButtonState()

	#show or hide "See all" button
	def updateSeeAllButtonState(self):
		if len(self.cardList) >= self.maxColCount:
			self.btnAll.show()
		else:
			self.btnAll.hide()

	#set category text of the frame
	def setCaption(self, text):
		self.caption.setText(text)

	def setCaptionFont(self, font):
		self.caption.setFont(font)

	#remove app card by its name
	def removeApp(self, appname):
		for eCard in self.cardList:
			if eCard.getAppName == appname:
				self.cardList.remove(eCard)

	#automatically adjust column count of grid layout due to the frame width
	def autoAdjust(self):
		if len(self.cardList) > 0:
			recColCount = int(self.width() / self.cardList[0].width()) - 1
			if recColCount == 0:
				recColCount = 1

			self.setColumnCount(recColCount)

			#adjust horizontal spacing
			ml, mt, mr, mb = self.mainLayout.getContentsMargins()
			hl, ht, hr, hb = self.cardLayout.getContentsMargins()
			if self.maxColCount > 1:
				hspacing = ((self.width() - ml - mr - hl - hr) - self.cardList[0].width() * self.maxColCount) / (self.maxColCount - 1)
				self.cardLayout.setHorizontalSpacing(hspacing)

	#set column count of grid layout to count
	def setColumnCount(self, count):
		self.maxColCount = count
		self.updateSeeAllButtonState()
		for card in self.cardList:
			self.cardLayout.removeWidget(card)
		index = 0
		for card in self.cardList:
			row, col = int(index / self.maxColCount), int(index % self.maxColCount)
			self.cardLayout.addWidget(card, row, col)
			index += 1

	def setAppNameFont(self, font):
		for iCard in self.cardList:
			iCard.setAppNameFont(font)

	def setAppDevFont(self, font):
		for iCard in self.cardList:
			iCard.setAppDevFont(font)

	def setAppDescFont(self, font):
		for iCard in self.cardList:
			iCard.setAppDescFont(font)

	#slot for button click
	@pyqtSlot()
	def onSeeAll(self):
		self.setSeeAll()
		self.seeAll = not self.seeAll

	#show or hide app cards on button click
	def setSeeAll(self):
		col = self.cardLayout.columnCount()
		if not self.seeAll:
			self.btnAll.setText("SEE ONE ROW")
			for index in range(col, len(self.cardList)):
				self.cardList[index].show()
		else:
			self.btnAll.setText("SEE ALL")
			for index in range(col, len(self.cardList)):
				self.cardList[index].hide()
	#overrided method
	def resizeEvent(self, event):
		QFrame.resizeEvent(self, event)
		self.autoAdjust()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = QMainWindow()

	central = QWidget(widget)
	layout = QVBoxLayout(central)
	frame = CardFrame(widget)
	frame.setColumnCount(5)
	frame.setAutoFillBackground(True)
	frame.setGeometry(0, 0, frame.width(), frame.height())

	#you can add app card with this method
	frame.addNewApp(1, "AI ChatBot", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.3, 10, 0)
	frame.addNewApp(2, "Call of Duty", "default", "./img/card/back.png","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.5, 6, 0)
	frame.addNewApp(3, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 3.75, 5, 0)
	#frame.addNewApp(4, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 5)
	#frame.addNewApp(5, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.7)

	#you can also use this way to add a new app card
	newCard = AppCard(frame)
	newCard.setAppId(6)
	newCard.setAppName("FingerAI")
	newCard.setAppDevName("Igor Yal")
	newCard.setAppIcon("./img/card/finger.png")
	newCard.setAppDesc("This card was generated out of card frame and manually added to the card frame by addCard")
	newCard.setAppRating(4, 12)
	newCard.setAppState(1)

	bCard = AppCard(frame)
	bCard.setAppId(6)
	bCard.setAppName("Card with gradient background")
	bCard.setAppDevName("Igor Yal")
	bCard.setAppIcon("./img/card/kid.png")
	bCard.setAppDesc("Background is bad.This card was generated out of card frame and manually added to the card frame by addCard")
	bCard.setAppRating(2.4, 15)
	bCard.setAppState(1)

	cCard = AppCard(frame)
	cCard.setAppId(6)
	cCard.setAppName("Custom")
	cCard.setAppDevName("Igor Yal")
	cCard.setAppIcon("./img/card/kid.png")
	cCard.setAutoFillBackground(True)
	cCard.setBackgroundImage("./img/card/back.png")
	cCard.setAppDesc("This card was generated out of card frame and manually added to the card frame by addCard")
	cCard.setAppRating(0, 0)
	cCard.setAppState(1)

	frame.addCard(newCard)
	frame.addCard(bCard)
	frame.addCard(cCard)
	#frame.setAppNameFont(QFont("Comic Sans MS", 15))
	
	layout.addWidget(frame)

	widget.setCentralWidget(central)
	widget.show()
	sys.exit(app.exec())