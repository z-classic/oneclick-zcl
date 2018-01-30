#!/usr/bin/python

# Import PySide classes
import sys
from subprocess import call

from PySide.QtCore import *
from PySide.QtGui import *


class App:
  def __init__(self):
    # Create a Qt application
    self.app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)

    startedIcon = QIcon("zcl-started.svg")
    stoppedIcon = QIcon("zcl-stopped.svg")

    menu = QMenu()

    startAction = menu.addAction("Start")
    startAction.triggered.connect(self.start)

    menu.addSeparator()

    configureAction = menu.addAction("Configure")
    configureAction.triggered.connect(self.configure)

    aboutAction= menu.addAction("About")
    aboutAction.triggered.connect(self.about)

    menu.addSeparator()

    exitAction = menu.addAction("Exit")
    exitAction.triggered.connect(sys.exit)

    self.tray = QSystemTrayIcon()
    self.tray.setIcon(stoppedIcon)
    self.tray.setContextMenu(menu)

    self.tray.show()

    # TODO Alert Dialogs as needed
    #self.tray.showMessage("traymessage1_1", "traymessage1_2")

  def run(self):
    # Enter Qt application main loop
    self.app.exec_()
    sys.exit()

  def start(self):
    call('./start.sh --miningArgs')

    #self.tray.showMessage("started", "mining")
    self.tray.setIcon(startedIcon)

  def stop(self):
    call('./stop.sh')

    #self.tray.showMessage("stopped", "mining")
    self.tray.setIcon(stoppedIcon)

  def configure(self):
    self.dialog = QDialog(None, Qt.WindowStaysOnTopHint)
    self.dialog.setWindowTitle("Configure")

    poolLabel = QLabel("Pool:")

    self.poolComboBox = QComboBox()
    self.poolComboBox.addItem("None", QSystemTrayIcon.NoIcon)
    self.poolComboBox.addItem("Pool 1")
    self.poolComboBox.addItem("Pool 2")
    self.poolComboBox.addItem("Pool 3")
    
    self.poolComboBox.setCurrentIndex(1)

    startOnOpenLabel = QLabel("Start Mining on Open?")
    startOnOpenCheckBox = QCheckBox()

    addressLabel = QLabel("Your Address:")
    addressTextEdit = QTextEdit()


    # Create layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(poolLabel)
    layout.addWidget(self.poolComboBox)
    layout.addWidget(startOnOpenLabel)
    layout.addWidget(startOnOpenCheckBox)
    layout.addWidget(addressLabel)
    layout.addWidget(addressTextEdit)

    self.dialog.setLayout(layout)

    self.dialog.show()

  def about(self):
    self.dialog = QDialog(None, Qt.WindowStaysOnTopHint)
    self.dialog.setWindowTitle("About")

    teamLabel = QLabel("Zclassic One-Click Miner (Equihash)")
    donateLabel = QLabel("Donate:  t1Wq2HdXZ7G9uYd1HppewSoMahGBt6ZVNUD")

    feeLabel = QLabel("The Optiminer used by this software takes a 1% dev fee. Read more: https://github.com/Optiminer/OptiminerEquihash")

    # Create layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(teamLabel)
    layout.addWidget(donateLabel)

    self.dialog.setLayout(layout)

    self.dialog.show()


if __name__ == "__main__":

  if not QSystemTrayIcon.isSystemTrayAvailable():
    QMessageBox.critical(None, "Systray",
        "Couldn't detect a system tray on this computer...")
    sys.exit(1)


  app = App()
  app.run()
