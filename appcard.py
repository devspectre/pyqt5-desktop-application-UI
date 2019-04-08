import sys
from PyQt5.QtWidgets import QWidget, QFrame, QPushButton, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, Q_ENUM, pyqtSlot, QSize
from PyQt5.QtGui import QFont , QPixmap, QImage, QPalette, QBrush, QColor
from elidelabel import ElideLabel
from starrating import StarRating
from button import Button

#you can define necessary styles here
class STYLES:
	STYLE_DEFAULT = "#IconFrame{background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(0, 165, 255, 25), stop:1 rgba(0, 215, 255, 0));}"
	STYLE_PINK = "#IconFrame{background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(255, 20, 147, 25), stop:1 rgba(255, 20, 147, 0));}"
	STYLE_ORANGE = "#IconFrame{background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(255, 165, 0, 25), stop:1 rgba(255, 215, 0, 0));}"

class AppCard(QFrame):
	"""A Card widget derived from QFrame contains app icon, 
	app name, app developer, app description, app rating, etc"""

	STYLES = STYLES
	Q_ENUM(STYLES)

	def __init__(self, parent=None):
		QFrame.__init__(self, parent)

		self.setFixedSize(200, 300)

		self.setObjectName("Card")
		
		self.setAutoFillBackground(True)

		self.appId = -1
		self.appIcon = "./img/card/bird.png"
		self.appBack = "./img/card/card_back.png"
		self.appName = "PROS Smart CPQ for Manufacturing"
		self.appDev = "By PROS\nWeb apps"
		self.appRating = 0
		self.appFeedback = 0
		self.appState = 0
		self.style_str = "border: 1px solid #ddd; background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(225, 225, 225, 225));"
		self.appDesc = "Deliver Sales Automation and Profits Through Personalized Selling"
		self.setBackgroundImage(self.appBack)

		self.iconSize = 48, 48
		self.iconMargins = 10, 10, 10, 10
		self.iconFrameStyle = STYLES.STYLE_DEFAULT

		self.iconFrame = QLabel(self)
		self.iconFrame.setAutoFillBackground(True)
		self.iconFrame.setObjectName("IconFrame")
		self.iconFrame.setStyleSheet(self.iconFrameStyle)

		self.imgIcon = QLabel(self.iconFrame)
		self.imgIcon.setPixmap(QPixmap(self.appIcon))
		self.imgIcon.setFixedSize(48, 48)
		self.imgIcon.setScaledContents(True)

		self.iconLayout = QHBoxLayout(self.iconFrame)
		self.iconLayout.setContentsMargins(10, 10, 10, 10)
		self.iconLayout.setAlignment(Qt.AlignLeft)
		self.iconLayout.addWidget(self.imgIcon, Qt.AlignLeft)
		self.iconFrame.setLayout(self.iconLayout)

		self.txtName = ElideLabel("", self)
		self.txtName.setText(self.appName)
		self.txtName.setFont(QFont("Roboto", 15))
		self.txtName.setElideMode(1)
		self.txtName.setWordWrap(True)

		self.txtDev = ElideLabel("", self)
		self.txtDev.setWordWrap(True)
		self.txtDev.setText(self.appDev)
		self.txtDev.setFont(QFont("Roboto", 8))

		self.txtDesc = ElideLabel("", self)
		self.txtDesc.setText(self.appDesc)
		self.txtDesc.setAlignment(Qt.AlignTop)
		self.txtDesc.setFont(QFont("Roboto", 10))
		self.txtDesc.setElideMode(1)
		self.txtDesc.setWordWrap(True)	

		self.starRating = StarRating(self)

		self.feedbackGiven = QLabel(self)
		self.feedbackGiven.setObjectName("Feedback")
		self.feedbackGiven.setStyleSheet("#Feedback{color: #ababab}")
		self.feedbackGiven.setFont(QFont("Roboto", 12))
		self.feedbackGiven.setAlignment(Qt.AlignVCenter)
		self.feedbackGiven.setText("(" + str(self.appFeedback) + ")")

		self.btnInstall = Button('Install', self)
		self.btnInstall.clicked.connect(self.onInstallClicked)

		self.btnLaunch = Button('Launch', self)
		self.btnLaunch.setButtonType(Button.BUTTON_TYPE.LAUNCH)
		self.btnLaunch.clicked.connect(self.onLaunchClicked)
		self.btnLaunch.hide()

		self.btnUninstall = Button('Uninstall', self)
		self.btnUninstall.setButtonType(Button.BUTTON_TYPE.DELETE)
		self.btnUninstall.clicked.connect(self.onUninstallClicked)
		self.btnUninstall.hide()

		self.shadowEffect = QGraphicsDropShadowEffect(self)
		self.shadowEffect.setBlurRadius(9)
		self.shadowEffect.setColor(QColor(225, 225, 225))
		self.shadowEffect.setOffset(5, 5)
		self.setGraphicsEffect(self.shadowEffect)

		self.frameLayout = QVBoxLayout(self)
		self.frameLayout.setContentsMargins(0, 0, 0, 0)

		self.mainLayout = QVBoxLayout()
		self.mainLayout.setSpacing(5)
		self.mainLayout.setContentsMargins(10, 0, 10, 15)

		self.ratingLayout = QHBoxLayout()
		self.ratingLayout.setSpacing(5)
		self.ratingLayout.addWidget(self.starRating, 1, Qt.AlignLeft)
		self.ratingLayout.addWidget(self.feedbackGiven, 1, Qt.AlignLeft)

		self.separator = QFrame(self)
		self.separator.setObjectName("line")
		self.separator.setFixedHeight(2)
		self.separator.setFixedWidth(self.width())
		self.separator.setFrameShape(QFrame.HLine)
		self.separator.setFrameShadow(QFrame.Sunken)

		self.btnLayout = QHBoxLayout()
		self.btnLayout.setContentsMargins(5, 5, 5, 10)
		self.btnLayout.setSpacing(20)
		self.btnLayout.setAlignment(Qt.AlignHCenter)
		self.btnLayout.addWidget(self.btnInstall)
		self.btnLayout.addWidget(self.btnUninstall)
		self.btnLayout.addWidget(self.btnLaunch)

		self.mainLayout.addWidget(self.txtName, 1, Qt.AlignLeft)
		self.mainLayout.addWidget(self.txtDev, 1, Qt.AlignLeft)
		self.mainLayout.addWidget(self.txtDesc, 3, Qt.AlignLeft)
		self.mainLayout.addLayout(self.ratingLayout, Qt.AlignLeft)

		self.frameLayout.addWidget(self.iconFrame, 1)
		self.frameLayout.addLayout(self.mainLayout)
		self.frameLayout.addWidget(self.separator)
		self.frameLayout.addLayout(self.btnLayout)

		self.setLayout(self.frameLayout)
		self.setAppState(self.appState)
		self.show()

	#automatically adjust child widgets' sizes based on the frame's geometry
	#this might affect widgets' sizes
	def autoAdjust(self):
		self.starRating.adjustWidthByHeight(self.height()/15)
		self.feedbackGiven.setFixedHeight(self.height()/16)
		self.iconFrame.setFixedHeight(self.height()/5)
		self.setIconSize(self.iconFrame.height() * 4 / 5, self.iconFrame.height() *4 / 5)
		mm = self.iconFrame.height() / (5 * 2)
		self.setIconMargins(mm, mm, mm, mm)

	#set fixed size for the icon, maybe called logo or brand
	def setIconSize(self, aw, ah):
		self.iconSize = aw, ah
		self.imgIcon.setFixedSize(self.iconSize[0], self.iconSize[1])

	#set icon margins within the icon frame
	def setIconMargins(self, ml, mt = 0, mr = 0, mb = 0):
		self.iconMargins = ml, mt, mr, mb
		mml, mmt, mmr, mmb = self.mainLayout.getContentsMargins()
		self.iconLayout.setContentsMargins(mml, mt, mmr, mb)
	#set icon frame's style, you can stylize background(single color, gradient or image), border, etc
	def setIconFrameStyle(self, style):
		self.iconFrameStyle = style
		self.iconFrame.setStyleSheet(self.iconFrameStyle)

	@pyqtSlot()
	def onInstallClicked(self):
		QMessageBox.information(None, "ID: " + str(self.appId), "Install button clicked")

	@pyqtSlot()
	def onUninstallClicked(self):
		QMessageBox.information(None, "ID: " + str(self.appId), "Gonna uninstall the app?")

	@pyqtSlot()
	def onLaunchClicked(self):
		QMessageBox.information(None, "ID: " + str(self.appId), "Launch is not ready yet!")

	#set whether the app is already installed or not, accordingly show or hide appropriate buttons
	def setAppState(self, state):
		if state == 0:
			self.btnInstall.show()
			self.btnUninstall.hide()
			self.btnLaunch.hide()
		elif state == 1:
			self.btnInstall.hide()
			self.btnUninstall.show()
			self.btnLaunch.show()
		self.autoAdjust()

	#return current app state
	def getAppState(self):
		return self.appState

	#set applicaton name
	def setAppName(self, name):
		if name != self.appName:
			self.appName = name
			self.txtName.setText(self.appName)
	#return application name
	def getAppName(self):
		return self.appName

	#set developer name, or could be company name
	def setAppDevName(self, name):
		if name != self.appDev:
			self.appDev = name
			self.txtDev.setText(self.appDev)

	#return developer name
	def getAppDevName(self):
		return self.appDev

	#set description about application
	def setAppDesc(self, desc):
		if desc != self.appDesc:
			self.appDesc = desc
			self.txtDesc.setText(self.appDesc)

	#return description of application
	def getAppDesc(self):
		return self.appDesc

	#set application icon with appropriate file path
	def setAppIcon(self, imgPath):
		if imgPath != self.appIcon:
			self.appIcon = imgPath
			self.imgIcon.setPixmap(QPixmap(self.appIcon))

	#return QPixmap of icon
	def getAppIconPixmap(self):
		return QPixmap(self.appIcon)

	#return path to icon
	def getAppIconPath(self):
		return self.appIcon

	#set applicaiton star rating and count of given feedbacks
	def setAppRating(self, rating, feedback):
		if rating != self.appRating or feedback != self.appFeedback:
			self.appRating, self.appFeedback = rating, feedback
			self.starRating.setRating(rating)
			self.feedbackGiven.setText("(" + str(feedback) + ")")

	#return star rating value and the count of given feedbacks
	def getAppRating(self):
		return (self.appRating, self.appFeedback)

	#set path to background would be embedded into stylesheet string
	def setBackgroundImage(self, img):
		self.appBack = img
		self.setStyleSheet("#Card{" + self.style_str + " background-image: url(" + self.appBack + ")}")

	#set application ID
	def setAppId(self, id):
		self.appId = id

	#return app ID
	def getAppId(self):
		return self.appId

	#set blur radius of frame's shadow effect
	def setShadowBlurRadius(self, radius):
		self.shadowEffect.setBlurRadius(radius)

	#set shadow offset of frame's shadow effect
	def setShadowOffset(self, offX, offY):
		self.shadowEffect.setOffset(offX, offY)

	#set shadow color of frame's shadow effect
	def setShadowColor(self, color):
		self.shadowEffect.setColor(color)

	#set font of application name
	def setAppNameFont(self, font):
		self.txtName.setFont(font)

	#set font of developer name
	def setAppDevFont(self, font):
		self.txtDev.setFont(font)

	#set font of description to the app
	def setAppDescFont(self, font):
		self.txtDesc.setFont(font);

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	widget.setObjectName("widget")
	widget.setAutoFillBackground(True)
	widget.setStyleSheet("#widget{background-color: white}")
	appcard = AppCard(widget)
	#appcard.setBackgroundImage("./img/card/back.png")
	appcard.setGeometry(100, 100, appcard.width(), appcard.height())
	widget.show()
	sys.exit(app.exec())