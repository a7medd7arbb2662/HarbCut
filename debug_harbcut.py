import sys
import os

# Add the src directory to sys.path so we can import 'gui'
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from PyQt6.QtWidgets import QApplication
from gui.main import HarbCut

# Essential for Windows dark mode
os.environ["QT_QPA_PLATFORM"] = "windows:darkmode=0"

# Create and run the app directly
app = QApplication(sys.argv)
gui = HarbCut()
gui.show()
gui.activateWindow()
gui.raise_()
sys.exit(app.exec())
