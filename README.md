<h1 align="center">
  <br>
  <a href="https://github.com/a7medd7arbb2662/HarbCut"><img src="exe/icon.ico" alt="HarbCut icon" width="128" height="128"></a>
  <br>
  HarbCut
  <br>
</h1>
<h4 align="center">Eye candy ARP spoofer for Windows</h4>

<p align=center>
  <a target="_blank" href="https://github.com/a7medd7arbb2662/HarbCut/releases/latest" title="Latest release">
    <img src="https://img.shields.io/github/v/release/a7medd7arbb2662/HarbCut">
  </a>
  <a target="_blank" href="https://sourceforge.net/projects/harbcut/files/stats/timeline" title="SourceForge Downloads">
    <img src="https://img.shields.io/sourceforge/dt/harbcut?label=SourceForge">
  </a>
  <a target="_blank" href="https://github.com/a7medd7arbb2662/HarbCut/releases/latest" title="GitHub Downloads">
    <img src="https://img.shields.io/github/downloads/a7medd7arbb2662/HarbCut/total.svg?label=GitHub">
  </a>
  <a target="_blank" href="LICENSE" title="License: MIT">
    <img src="https://img.shields.io/github/license/a7medd7arbb2662/HarbCut">
  </a>
</p>
<p align=center>
  <a href="https://sourceforge.net/projects/harbcut/" target="_blank">
    <img src="https://sourceforge.net/cdn/syndication/badge_img/3324963/oss-open-source-excellence-black?achievement=oss-open-source-excellence&r=https://sourceforge.net/p/harbcut/admin/files/badges/" alt="HarbCut - Eye candy ARP spoofer for Windows | SourceForge" style="width: 120px; height: 120px;" width="120" height="120" />
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://sourceforge.net/projects/harbcut/" target="_blank">
    <img src="https://sourceforge.net/cdn/syndication/badge_img/3324963/oss-community-leader-black?achievement=oss-community-choice&r=https://sourceforge.net/p/harbcut/admin/files/badges/" alt="HarbCut - Eye candy ARP spoofer for Windows | SourceForge" style="width: 120px; height: 120px;" width="120" height="120" />
  </a>
</p>

<p align=center>
  <a href="#disclaimer">Disclaimer</a> &bull;
  <a href="#screenshots">Screenshots</a> &bull;
  <a href="#description">Description</a> &bull;
  <a href="#download">Download</a> &bull;
  <a href="#requirements">Requirements</a> &bull;
  <a href="#manual">Manual</a> &bull;
  <a href="#run-from-source">Run From Source</a> &bull;
  <a href="#build-from-source">Build From Source</a> &bull;
  <a href="#todo">TODO</a> &bull;
  <a href="#license">License</a>
</p>
<hr>

## Disclaimer
**The use of this software is done at your own discretion and risk and with agreement that you will be solely responsible for any damage to your/others computer system or loss of data that may/will result from such activities**

## Screenshots

<table>
  <tr>
    <th colspan="3">
      <samp><h3>Main window</h3></samp>
    </th>
  </tr>
  <tr>
    <th colspan="3">
      <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/data/preview.png?raw=true" alt="Main window">
    </th>
  </tr>
  <tr>
    <th>
      <samp><h3>Settings window</h3></samp>
    </th>
    <th>
      <samp><h3>Tray Icon</h3></samp>
    </th>
    <th>
      <samp><h3>Tray menu</h3></samp>
    </th>
  </tr>
  <tr>
    <th>
      <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/data/preview-settings.png?raw=true" alt="Settings window">
    </th>
    <th>
      <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/data/preview-tray.png?raw=true" alt="Tray icon">
    </th>
    <th>
      <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/data/preview-tray-menu.png?raw=true" alt="Tray icon menu">
    </th>
  </tr>
</table>

## Description
HarbCut aims to make ARP spoofing easy for all users with all the hard work done under the hood.

One of its main features is the ability to selectively block devices from accessing the internet while keeping the network connection alive for the attacker. It supports both ARP spoofing and ICMP (ping) scanning methods.

### Features
- **ARP Spoofing** - Block/allow internet access for selected devices
- **ARP Scan** - Fast device discovery on local network
- **Ping Scan** - Alternative scanning method for isolated SSIDs/bands
- **URL Watcher** - Monitor URLs visited by devices on the network
- **Device Nicknames** - Custom names for recognized devices
- **Network Interface Selection** - Choose which adapter to use
- **System Tray Integration** - Minimize to tray, run in background
- **Dark/Light Theme** - User preference
- **Autostart** - Optional Windows startup registration
- **Taskbar Progress** - Visual feedback during operations

### Screenshots Table

| Feature | Icon | Description | Notes |
|---------|------|-------------|-------|
| ARP Scan | <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/assets/scan_arp.png?raw=true" alt="ARP Scan" width="80px"> | Perform ARP Scan | Fast, low CPU, misses some devices |
| Ping Scan | <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/assets/scan_hard.png?raw=true" alt="Ping Scan" width="80px"> | Perform Ping Scan | Slower than ARP but all devices are detected (HIGH CPU USAGE) |
| Kill | <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/assets/kill.png?raw=true" alt="Kill" width="80px"> | Block selected device from internet | - |
| Unkill | <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/assets/unkill.png?raw=true" alt="Unkill" width="80px"> | Allow blocked device internet access | - |
| Kill All | <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/assets/killall.png?raw=true" alt="Kill All" width="80px"> | Block all connected devices | - |
| Unkill All | <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/assets/unkillall.png?raw=true" alt="Unkill All" width="80px"> | Allow all blocked devices | - |
| Settings | <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/assets/settings.png?raw=true" alt="Settings" width="80px"> | View HarbCut settings window | - |
| About | <img src="https://github.com/a7medd7arbb2662/HarbCut/blob/main/assets/about.png?raw=true" alt="About" width="80px"> | View HarbCut about window | - |

## Download
Download the latest release from [GitHub Releases](https://github.com/a7medd7arbb2662/HarbCut/releases/latest) or [SourceForge](https://sourceforge.net/projects/harbcut/files/).

## Requirements
- Windows 10/11 (64-bit)
- **Administrator privileges** (required for ARP spoofing)
- [Npcap](https://nmap.org/npcap/) installed (WinPcap API compatibility mode)

## Manual
1. Install Npcap from [nmap.org/npcap](https://nmap.org/npcap/) (check "WinPcap API-compatible Mode")
2. Download `HarbCut.exe` from releases
3. **Right-click `HarbCut.exe` → "Run as administrator"**
4. Select network interface from dropdown
5. Click "Scan" to discover devices
6. Select devices and click "Kill" to block internet
7. Click "Unkill" to restore access

## Run From Source
- Install Python 3.11+
- Install dependencies: `pip install -r requirements.txt`
- Run: `python src/harbcut.py`

## Build From Source
**Dependencies:**
- Python 3.11+ (with `pyinstaller`)
- Qt6 (PyQt6)
- Npcap SDK

***Make sure that all of the above are in PATH in order to build HarbCut without issues***

Now run: `python build.py`

## TODO
- [ ] Work properly on any Windows language.
- [ ] Control download and upload limit of connected devices.
- [ ] Protect HarbCut user from other spoofers.
- [x] Select between available interfaces.
- [x] Dump traffic from any device.
- [ ] Background live connection checker.
- [ ] Background live devices discovery.
- [ ] Extend scan for all subnet masks.

## Donation
If you find this project helpful, you can give me a cup of coffee :)

<a href="https://www.buymeacoffee.com/a7medd7arbb2662" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>&nbsp;&nbsp;<a href="https://www.paypal.me/a7medd7arbb2662" target="_blank"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="Donate via PayPal" height="41" width="174"></a>

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)
HarbCut is Free Software: You can use, study, share and improve it at your will. Specifically you can redistribute and/or modify it under the terms of the [GNU General Public License](https://www.gnu.org/licenses/gpl.html) as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.