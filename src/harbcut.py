from sys import argv, exit
from PyQt6.QtWidgets import QApplication, QStyleFactory
from PyQt6.QtCore import Qt

from hctools.utils import goto
from hctools.utils_gui import npcap_exists, duplicate_harbcut, repair_settings, migrate_settings_file
from hctools.qtools import msg_box, Buttons, MsgIcon

from gui.main import HarbCut

from assets import app_icon
from constants import *

import os

# os.environ["QT_QPA_PLATFORM"] = "windows:darkmode=0"

if __name__ == "__main__":
    print("Starting HarbCut...")
    app = QApplication(argv)
    print("QApplication created")
    app.setStyle(QStyleFactory.create('Fusion'))
    print("Style set")
    icon = HarbCut.processIcon(app_icon)
    print("Icon processed")
    is_restarting = '--restarting' in argv

    # Check if Npcap is installed
    print("Checking Npcap...")
    if not npcap_exists():
        print("Npcap not found!")
        if msg_box('HarbCut', 'Npcap is not installed\n\nClick OK to download',
                    MsgIcon.CRITICAL, icon, Buttons.OK | Buttons.CANCEL) == Buttons.OK:
            goto(NPCAP_URL)
    else:
        print("Npcap OK.")
        # Check if another HarbCut process is running
        if not is_restarting and duplicate_harbcut():
            print("Duplicate HarbCut detected!")
            msg_box('HarbCut', 'HarbCut is already running!', MsgIcon.WARN, icon)
        else:
            # Run the GUI
            print("Migrating settings...")
            migrate_settings_file()
            print("Migrate done. Repairing settings...")
            repair_settings()
            print("Repair done.")
            
            print("Initializing HarbCut GUI...")
            GUI = HarbCut()
            print("HarbCut GUI initialized.")
            
            # Force window to be visible and on top
            print("Showing window...")
            GUI.setWindowState(Qt.WindowState.WindowNoState)
            GUI.show()
            GUI.raise_()
            GUI.activateWindow()
            
            print("Scanner init...")
            GUI.resizeEvent()
            GUI.scanner.init()
            print("Scanner init done.")
            
            GUI.killer.iface = GUI.scanner.iface
            GUI.sync_ip_forwarding_state()
            GUI.scanner.flush_arp()
            GUI.scanEasy()
            print("Starting Update Thread...")
            GUI.UpdateThread_Starter()
            
            print("Ready.")
            exit(app.exec())