import sys
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItemIterator
from PyQt5.QtCore import QSize

class AutoTreeWidget(QTreeWidget):
	"""Treewidget derived from QTreeWidget that automatically adjust its height without scrollbar
	scrollbar is removed to make it look good"""
	def sizeHint(self):
		height = 2 * self.frameWidth() # border around tree
		header = self.header()
		if not self.isHeaderHidden():
			headerSizeHint = header.sizeHint()
			height += headerSizeHint.height()
		rows = 0
		it = QTreeWidgetItemIterator(self)
		while it.value() is not None:
			rows += 1
			index = self.indexFromItem(it.value())
			height += self.rowHeight(index)
			it += 1
		return QSize(header.length() + 2 * self.frameWidth(), height)

	#automatically adjust height of widget according to the sum of child items within it
	def autoAdjust(self):
		ml, mt, mr, mb = self.getContentsMargins()
		self.setFixedSize(self.width(), self.sizeHint().height() + 10)