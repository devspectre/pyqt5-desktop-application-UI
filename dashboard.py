import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from cardframe import CardFrame
from productview import ProductView
from checklist import CheckList
from verticalscrollarea import VerticalScrollArea
from verticalscrollarea import VSCROLL_STYLE

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		self.setObjectName("MainWindow")
		self.setStyleSheet("#MainWindow{background-color: white}")
		self.menuList = []
		self.frameList = []

		#centralwidget of mainwindow
		self.centralwidget = QWidget(self)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayout = QHBoxLayout(self.centralwidget)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.horizontalLayout.setSpacing(10)
		#self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)

		#sidemenu scrollable area
		self.menuArea = VerticalScrollArea(self.centralwidget)
		self.menuArea.setStyle(VSCROLL_STYLE.THIN)
		self.menuArea.setAutoFillBackground(True)
		self.menuArea.setObjectName("menuArea")
		self.menuArea.setContentsMargins(0, 0, 0, 0)
		self.menuArea.setFrameShape(QFrame.NoFrame)

		#sidemenu frame within the scroll area
		self.menuFrame = QFrame(self.centralwidget)
		self.menuFrame.setObjectName("SideMenu")
		self.menuFrame.setStyleSheet("#SideMenu{background-color: #f1f1f1;}")

		#sidemenu layout for responsive
		self.menuLayout = QVBoxLayout(self.menuFrame)
		self.menuLayout.setContentsMargins(0, 0, 0, 0)
		self.menuLayout.setSpacing(0)
		self.menuLayout.setObjectName("menuLayout")
		self.menuLayout.setAlignment(Qt.AlignTop)

		#widget with treewidget selector
		self.alist = ProductView(self.menuFrame)
		self.alist.setAutoFillBackground(True)
		alist_data = [[['Web Apps','1'], ['React', '2'],['Vue.js', '3']], 
				[['Add-Ins', '4'],['Dynamics 365', '5'], ['Office 365', '6'],
				 ['Power BI apps', '7'], ['Power BI visuals', '8'], ['Dynamics NAV', '9']]]
		self.alist.addList(alist_data)
		self.alist.setListFont(QFont("Roboto", 12))
		self.alist.setCaptionFont(QFont("Roboto", 16))
		self.alist.stateChanged.connect(self.onTreeWidgetChanged)
		
		#widget with checkable items
		self.plist = CheckList(self.menuFrame)
		self.plist.setCaption("Categories")
		self.plist.setAutoFillBackground(True)
		plist_data = [['Analytics','1'], ['Artificial Intelligence', '2'],['Collaboration', '3'], 
				['Customer service', '4'],['Finance', '5'], ['Human resources', '6'],
				 ['IT + administration', '7'], ['Internet of things', '8'], ['Marketing', '9'],
				 ['Operations + supply', '10'], ['Productivity', '11'], ['Sales', '12']]
		self.plist.addList(plist_data)
		self.plist.setListFont(QFont("Roboto", 12))
		self.plist.setCaptionFont(QFont("Roboto", 16))
		self.plist.stateChanged.connect(self.onCheckListChanged)
		#self.plist.autoAdjust()

		#widget with checkable items
		self.dlist = CheckList(self.menuFrame)
		self.dlist.setCaption("Industry")
		self.dlist.setAutoFillBackground(True)
		plist_data = [['Analytics','1'], ['Artificial Intelligence', '2'],['Collaboration', '3'], 
				['Customer service', '4'],['Finance', '5'], ['Human resources', '6'],
				 ['IT + administration', '7'], ['Internet of things', '8'], ['Marketing', '9'],
				 ['Operations + supply', '10'], ['Productivity', '11'], ['Sales', '12']]
		self.dlist.addList(plist_data)
		self.dlist.setListFont(QFont("Roboto", 12))
		self.dlist.setCaptionFont(QFont("Roboto", 16))
		self.dlist.stateChanged.connect(self.onCheckListChanged)

		#widget with checkable items
		self.ilist = CheckList(self.menuFrame)
		self.ilist.setCaption("Developers")
		self.ilist.setAutoFillBackground(True)
		plist_data = [['Analytics','1'], ['Artificial Intelligence', '2'],['Collaboration', '3'], 
				['Customer service', '4'],['Finance', '5'], ['Human resources', '6'],
				 ['IT + administration', '7'], ['Internet of things', '8'], ['Marketing', '9'],
				 ['Operations + supply', '10'], ['Productivity', '11'], ['Sales', '12']]
		self.ilist.addList(plist_data)
		self.ilist.setListFont(QFont("Roboto", 12))
		self.ilist.setCaptionFont(QFont("Roboto", 16))
		self.ilist.stateChanged.connect(self.onCheckListChanged)

		#container for the frames, you can easily access the frames with this
		self.menuList.append(self.alist)
		self.menuList.append(self.plist)
		self.menuList.append(self.ilist)

		self.menuLayout.addWidget(self.alist)
		self.menuLayout.addWidget(self.plist)
		self.menuLayout.addWidget(self.dlist)
		self.menuLayout.addWidget(self.ilist)
		self.menuLayout.addSpacerItem(QSpacerItem(0, 1000, QSizePolicy.Expanding, QSizePolicy.Expanding))
		self.menuArea.setWidget(self.menuFrame)
		self.menuArea.setWidgetResizable(True)

		#scrollable area for cardframes 
		self.appArea = VerticalScrollArea(self.centralwidget)
		self.appArea.setAutoFillBackground(True)
		self.appArea.setObjectName("appArea")
		self.appArea.setFrameShape(QFrame.NoFrame)

		#container for card frames within the scrollable area
		self.appFrame = QFrame(self.centralwidget)

		#cardframe for one category
		self.webapp = CardFrame(self.appFrame)
		self.webapp.setAutoFillBackground(True)
		self.webapp.setColumnCount(1)

		self.webapp.addNewApp(1, "AI ChatBot", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.3, 7)
		#self.webapp.addNewApp(2, "Call of Duty", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.5, 12)
		#self.webapp.addNewApp(3, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 3.75, 6, 1)
		#self.webapp.addNewApp(4, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 1.7, 3)
		#self.webapp.addNewApp(5, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.7, 14)
		#self.webapp.addNewApp(6, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 3.75, 17, 1)
		#self.webapp.addNewApp(7, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 5, 26)
		#self.webapp.addNewApp(8, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.7, 46, 1)
		#self.webapp.addNewApp(9, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 3.0, 23)
		#self.webapp.addNewApp(10, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 5, 98)
		#self.webapp.addNewApp(11, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.7, 90)
		self.frameList.append(self.webapp)

		#cardframe for one category
		self.dynamic = CardFrame(self.appFrame)
		self.dynamic.setCaption("Add-Ins")
		self.dynamic.setAutoFillBackground(True)

		self.dynamic.addNewApp(12, "AI ChatBot", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.3, 22, 1)
		self.dynamic.addNewApp(13, "Call of Duty", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.5, 34)
		self.dynamic.addNewApp(14, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 3.75, 11)
		self.dynamic.addNewApp(15, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 5, 99, 1)
		self.dynamic.addNewApp(16, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.7, 99)
		self.dynamic.addNewApp(17, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 3.75, 100)
		self.dynamic.addNewApp(18, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 5, 213, 1)
		self.dynamic.addNewApp(19, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.7, 245)
		self.frameList.append(self.dynamic)

		#cardframe for one category
		self.office = CardFrame(self.appFrame)
		self.office.setCaption("Office 365")
		self.office.setAutoFillBackground(True)

		self.office.addNewApp(21, "AI ChatBot", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.3, 1)
		self.office.addNewApp(22, "Call of Duty", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.5)
		self.office.addNewApp(23, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 3.75, 1)
		self.office.addNewApp(24, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 5)
		self.office.addNewApp(25, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.7)
		self.office.addNewApp(23, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 3.75, 1)
		self.office.addNewApp(24, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 5)
		self.office.addNewApp(25, "PROS Smart CPQ for Manufacturing", "default", "default","By PROS Web apps", "This card was generated by addNewApp within the card frame", 4.7)
		self.frameList.append(self.office)

		self.appLayout = QVBoxLayout(self.appFrame)
		self.appLayout.setObjectName("appLayout")
		self.appLayout.setContentsMargins(0, 0, 0, 0)
		self.appLayout.setSpacing(0)
		self.appLayout.setAlignment(Qt.AlignCenter)
		
		for frame in self.frameList:
			self.appLayout.addWidget(frame)

		self.appArea.setWidget(self.appFrame)
		self.appArea.setWidgetResizable(True)
		self.horizontalLayout.addWidget(self.menuArea, 1)
		self.horizontalLayout.addWidget(self.appArea, 50)
		self.setCentralWidget(self.centralwidget)

	#overrided method
	def resizeEvent(self, event):
		QMainWindow.resizeEvent(self, event)
		#Note: do not forget to call ProductView.autoAdjust for all ProductView Instances
		self.alist.autoAdjust()

	#automatically adjust necessary widgets to make it suitable for any resolution
	def autoAdjust(self):
		ml, mt, mr, mb = self.horizontalLayout.getContentsMargins()
		sp = self.horizontalLayout.spacing()
		maxCol = int((self.width() - self.menuFrame.width() - sp - ml - mr) / self.frameList[0].cardList[0].width()) - 1
		for frame in self.frameList:
			frame.setColumnCount(maxCol)

	@pyqtSlot(int, str)
	def onTreeWidgetChanged(self, cid, cstr):
		QMessageBox.information(self, "TreeWidgetChanged!", "ID: " + str(cid) + "\n" + cstr)

	@pyqtSlot(int, int)
	def onCheckListChanged(self, cid, cstate):
		QMessageBox.information(self, "TreeWidgetChanged!", "ID: " + str(cid) + "\nState: " + str(cstate))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	window = MainWindow()
	window.setWindowFlags(Qt.Window|Qt.WindowTitleHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
	window.show()

	screen_resolution = app.desktop().screenGeometry()
	diff = window.frameGeometry().height() - window.geometry().height()
	width, height = screen_resolution.width(), app.desktop().availableGeometry().height() - diff

	window.setFixedSize(width, height)
	window.setWindowState(Qt.WindowMaximized)
	#window.showMaximized()


	window.autoAdjust()
	sys.exit(app.exec())