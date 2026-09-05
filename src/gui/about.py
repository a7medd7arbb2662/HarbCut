from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap

from ui.ui_about import Ui_MainWindow
from hctools.qtools import clickable
from hctools.utils import goto
from assets import twitter_icon, linkedin_icon, github_icon, reddit_icon, app_icon
from constants import VERSION

class About(QMainWindow, Ui_MainWindow):
    def __init__(self, harbcut, icon):
        super().__init__()
        self.harbcut = harbcut

        # Setup UI
        self.icon = icon
        self.setWindowIcon(icon)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.social_labels = [
            (self.lblAppIcon,  app_icon,      self.github_app),
            (self.lblTwitter,  twitter_icon,  self.twitter),
            (self.lblLinkedIn, linkedin_icon, self.linkedin),
            (self.lblGitHub,   github_icon,   self.github),
            (self.lblReddit,   reddit_icon,   self.reddit)
        ]

        for lbl, icon, url in self.social_labels:
            clickable(lbl).connect(url)
            self.setImage(lbl, icon)

        self.lblAppName.setText(f'HarbCut v{VERSION}')
        self.lblMyName.setText('Ahmed Harb')
        self.lblNickName.setText('(a7medd7arbb2662)')
    
    def showEvent(self, event):
        self.show()
        self.setWindowState(Qt.WindowState.WindowNoState)
        self.activateWindow()
        self.setStyleSheet(self.elmocut.styleSheet())
        event.accept()
    
    def setImage(self, label, icon):
        pix = QPixmap()
        pix.loadFromData(icon)
        label.setPixmap(pix)

    twitter    = lambda self: goto('https://twitter.com/___xpy___')
    linkedin   = lambda self: goto('https://www.linkedin.com/in/a7medd7arbb2662/')
    github     = lambda self: goto('https://github.com/a7medd7arbb2662')
    reddit     = lambda self: goto('https://www.reddit.com/user/a7medd7arbb2662')
    github_app = lambda self: goto('https://github.com/a7medd7arbb2662/harbcut')
