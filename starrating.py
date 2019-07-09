import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFrame)
from PyQt5.QtGui import ( QPixmap, QImage, QPainter)
from PyQt5.QtCore import (QRectF, Qt, QSize)

class StarRating(QFrame):
	""" Star rating widget derived from QFrame based on two different images, one for grey stars and one for colored and possessed stars"""
	def __init__(self, parent = None):
		QFrame.__init__(self, parent)

		self.onImage = QPixmap("./img/card/star_on.png", "PNG")#this should be colored stars at back
		self.offImage = QPixmap("./img/card/star_off.png", "PNG")#grey stars at the back
		self.rating = 0.0#current rating
		self.max = 5.0

	def setOnImage(self, onimg):
		self.onImage = onimg
		self.update()

	def setOffImage(self, offpix):
		self.offImage = offimg
		self.update()

	# automatically adjust widget size keeping the aspect ratio
	def adjustWidthByHeight(self, ah):
		pw, ph = self.offImage.width(), self.offImage.height()
		aw = ah * (pw / ph)
		self.setFixedSize(aw, ah)

	# set rating and update view
	def setRating(self, rating):
		if rating != self.rating:
			self.rating = rating
			self.update()

	# actually draws the stars according to the rating value
	def paintEvent(self, event):
		painter = QPainter(self)
		# actually, this does not work at all
		painter.setRenderHints(QPainter.Antialiasing|QPainter.SmoothPixmapTransform|QPainter.HighQualityAntialiasing)
		
		painter.drawPixmap(QRectF(0, 0, self.width(), self.height()), self.offImage, QRectF(0, 0, self.offImage.width(), self.offImage.height()))
		rw = self.width() * self.rating / self.max
		painter.drawPixmap(QRectF(0, 0, rw, self.height()), self.onImage, QRectF(0, 0, self.onImage.width() * self.rating / self.max , self.onImage.height()))
		painter.end()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = QWidget()
	widget.setFixedSize(500, 500)
	starrating = StarRating(widget)
	starrating.adjustWidthByHeight(25)
	starrating.setGeometry(100, 100, starrating.width(), starrating.height())
	starrating.setRating(3.5)
	
	widget.show()
	sys.exit(app.exec())