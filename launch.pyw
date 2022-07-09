import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://search.networkchuck.coffee/'))
        self.setWindowIcon(QIcon('favicon.ico'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.setMovable(False)

        back_button = QAction('←', self)
        back_button.setStatusTip('Back')
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        forward_button = QAction('→', self)
        forward_button.setStatusTip('Forward')
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        reload_button = QAction('↻', self)
        reload_button.setStatusTip('Reload')
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        home_button = QAction('⌂', self)
        home_button.setStatusTip('Home')
        home_button.triggered.connect(self.connect_home)
        navbar.addAction(home_button)

        self.urlbar = QLineEdit()
        navbar.addWidget(self.urlbar)
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        self.browser.urlChanged.connect(self.update_urlbar)

    def update_urlbar(self, qurl):
        url = qurl.toString()
        self.urlbar.setText(url)
    
    def navigate_to_url(self):
        url = QUrl(self.urlbar.text())
        self.browser.setUrl(url)

    def connect_home(self):
        self.browser.setUrl(QUrl('https://search.networkchuck.coffee/'))



app = QApplication(sys.argv)
QApplication.setApplicationName("Searcksh Light")
QApplication.setApplicationVersion("1.0")
window = MainWindow()
app.exec_()