import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow

# Force a simple GUI
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Diagnostic Window")
window.resize(400, 300)
window.show()
window.activateWindow()
window.raise_()
print("GUI should be visible now.")
sys.exit(app.exec())
