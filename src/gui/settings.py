from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from qdarkstyle import load_stylesheet
import os
from networking.diverter import HarbDivert
from hctools.utils_gui import import_settings, export_settings, get_settings, \
                            add_to_startup, remove_from_startup, set_settings, restart_gui_app
from hctools.qtools import MsgType, Buttons
from hctools.utils import get_ifaces, get_default_iface, get_iface_by_name

from ui.ui_settings import Ui_MainWindow

from networking.nicknames import Nicknames

from constants import *

class Settings(QMainWindow, Ui_MainWindow):
    def __init__(self, harbcut, icon):
        super().__init__()
        self.harbcut = harbcut

        # Setup UI
        self.icon = icon
        self.setWindowIcon(icon)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.loadInterfaces()

        # Apply old settings on open
        self.currentSettings()

        self.sliderCount.valueChanged.connect(self.spinCount.setValue)
        self.spinCount.valueChanged.connect(self.sliderCount.setValue)
        self.sliderThreads.valueChanged.connect(self.spinThreads.setValue)
        self.spinThreads.valueChanged.connect(self.sliderThreads.setValue)
        self.btnApply.clicked.connect(self.Apply)
        self.btnDefaults.clicked.connect(self.Defaults)
        self.btnUpdate.clicked.connect(self.checkUpdate)
    
    def Apply(self, silent_apply=False):
        nicknames = Nicknames()

        count         =  self.spinCount.value()
        threads       =  self.spinThreads.value()
        is_dark       =  self.rdbDark.isChecked()
        is_autostart  =  self.chkAutostart.isChecked()
        is_minimized  =  self.chkMinimized.isChecked()
        is_remember   =  self.chkRemember.isChecked()
        is_autoupdate =  self.chkAutoupdate.isChecked()
        iface         =  self.comboInterface.currentText()
        is_ip_forward =  self.chkIpForwarding.isChecked()

        exe_path = os.path.join(os.getcwd(), 'harbcut.exe')
        if is_autostart:
            add_to_startup(exe_path)
        else:
            remove_from_startup()

        # Make sure that real-time killed devices are included
        # If its user's first time to apply remember option
        killed_from_json = get_settings('killed')
        killed_from_elmo = list(self.harbcut.killer.killed)
        killed_all = list(set(killed_from_json + killed_from_elmo)) * is_remember

        old_ip_forward = get_settings('ip_forwarding')

        export_settings(
            [
            is_dark,
            count,
            is_autostart,
            is_minimized,
            is_remember,
            killed_all,
            is_autoupdate,
            threads,
            iface,
            nicknames.nicknames_database,
            is_ip_forward
            ]
        )

        old_iface = self.harbcut.scanner.iface.name
        
        self.harbcut.iface = get_iface_by_name(iface)
        self.updateElmocutSettings()
        # Fix horizontal headerfont reverts to normal after applying settings
        self.harbcut.tableScan.horizontalHeader().setFont(QFont('Consolas', 11))

        if is_ip_forward and not old_ip_forward:
            HarbDivert.enable_ip_forwarding(self.harbcut.scanner.iface.name)
            self.harbcut.killer.unkill_all()
            set_settings('killed', [])

            MsgType.INFO(
                self,
                'IP Forwarding Enabled',
                'IP forwarding has been enabled.\n'
                'Killing devices will no longer be effective, and all '
                'previously killed devices have been unkilled.\n\n'
                'HarbCut needs to restart to apply this change.\n'
                'If it still does not take effect, please restart your PC.'
            )
            restart_gui_app(self.harbcut)
            self.harbcut.quit_all()
            return

        if not is_ip_forward and old_ip_forward:
            HarbDivert.disable_ip_forwarding(self.harbcut.scanner.iface.name)
            self.harbcut.stop_all_watching()

            MsgType.INFO(
                self,
                'IP Forwarding Disabled',
                'IP forwarding has been disabled.\n'
                'URL watching will no longer be effective, and all '
                'currently watched devices have been stopped.\n\n'
                'HarbCut needs to restart to apply this change.\n'
                'If it still does not take effect, please restart your PC.'
            )
            restart_gui_app(self.harbcut)
            self.harbcut.quit_all()
            return

        if not silent_apply:
            MsgType.INFO(
                self,
                'Apply Settings',
                'New settings have been applied.'
            )
        
        if old_iface != iface:
            MsgType.INFO(
                self,
                'Interface Changed',
                'HarbCut will restart to apply new interface.'
            )

            # Restart HarbCut via restart.exe
            restart_gui_app(self.harbcut)
            self.harbcut.quit_all()
        
        self.close()

    def Defaults(self):
        if MsgType.WARN(
            self,
            'Default settings',
            'All settings will be reset to default.\nAre you sure?',
            Buttons.YES | Buttons.NO
        ) == Buttons.NO:
            return
        
        nickname_prompt = MsgType.WARN(
            self,
            'Default settings',
            'Do you want to reset devices nicknames?',
            Buttons.YES | Buttons.NO
        )
        
        # Check if user wants to keep nicknames or not
        if nickname_prompt == Buttons.NO:
            nicknames = Nicknames()
            vals = SETTINGS_VALS[:]
            vals[-1] = nicknames.nicknames_database
            export_settings(vals)
        else:
            export_settings()
        
        self.currentSettings()
        self.Apply()

    def updateElmocutSettings(self):
        s = import_settings()
        self.currentSettings()
        
        self.harbcut.minimize = False # Force to NOT minimize
        self.harbcut.remember = s['remember']
        self.harbcut.autoupdate = s['autoupdate']
        self.harbcut.ip_forwarding_enabled = s['ip_forwarding']
        self.harbcut.scanner.device_count = s['count']
        self.harbcut.scanner.max_threads = s['threads']
        
        self.harbcut.scanner.iface = get_iface_by_name(s['iface'])
        self.harbcut.killer.iface = get_iface_by_name(s['iface'])
        
        self.harbcut.setStyleSheet(self.styleSheet())
        self.harbcut.about_window.setStyleSheet(self.styleSheet())

    def currentSettings(self):
        s = import_settings()
        [self.rdbLight, self.rdbDark][s['dark']].setChecked(True)
        self.chkIpForwarding.setChecked(s['ip_forwarding'])
        self.chkAutostart.setChecked(s['autostart'])
        self.chkMinimized.setChecked(s['minimized'])
        self.chkRemember.setChecked(s['remember'])
        self.chkAutoupdate.setChecked(s['autoupdate'])
        self.spinCount.setValue(s['count'])
        self.spinThreads.setValue(s['threads'])
        self.sliderCount.setValue(s['count'])
        self.sliderThreads.setValue(s['threads'])
        
        if not s['iface']:
            set_settings('iface', get_default_iface().name)
            s = import_settings()
        
        index = self.comboInterface.findText(s['iface'], Qt.MatchFlag.MatchFixedString)
        self.comboInterface.setCurrentIndex(index * (index >= 0))
        
        self.setStyleSheet(load_stylesheet() if s['dark'] else '')
    
    def checkUpdate(self):
        self.harbcut.update_thread.prompt_if_latest = True
        self.harbcut.update_thread.start()
    
    def loadInterfaces(self):
        self.comboInterface.clear()
        self.comboInterface.addItems(
            [iface.name for iface in get_ifaces()]
        )