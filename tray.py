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
    #self.tray.showMessage("traymessage2_1", "traymessage2_2")

  def run(self):
    # Enter Qt application main loop
    self.app.exec_()
    sys.exit()

  def start(self):
    call('./start.sh --miningArgs')
    self.tray.setIcon(startedIcon)

  def stop(self):
    call('./stop.sh')
    self.tray.setIcon(stoppedIcon)

  def configure(self):
    self.dialog = QDialog()
    self.dialog.setWindowTitle("Configure")

    poolLabel = QLabel("Pool:")

    self.poolComboBox = QComboBox()
    self.poolComboBox.addItem("None", QSystemTrayIcon.NoIcon)

    self.poolComboBox.addItem(self.style().standardIcon(
            QStyle.SP_MessageBoxInformation), "Pool1",
            QSystemTrayIcon.Information)
    self.poolComboBox.addItem(self.style().standardIcon(
            QStyle.SP_MessageBoxWarning), "Pool2",
            QSystemTrayIcon.Warning)
    self.poolComboBox.addItem(self.style().standardIcon(
            QStyle.SP_MessageBoxCritical), "Pool3",
            QSystemTrayIcon.Critical)
    self.poolComboBox.setCurrentIndex(1)

    self.dialog.show()

  def about(self):
    self.dialog = QDialog()
    self.dialog.setWindowTitle("About the Zclassic One-Click Miner")

    poolLabel = QtGui.QLabel("2018 - The Zclassic Team")
    poolLabel = QtGui.QLabel("Donate - t1Wq2HdXZ7G9uYd1HppewSoMahGBt6ZVNUD")

    self.dialog.show()


if __name__ == "__main__":

  if not QSystemTrayIcon.isSystemTrayAvailable():
    QMessageBox.critical(None, "Systray",
        "I couldn't detect any system tray on this system.")
    sys.exit(1)

  QApplication.setQuitOnLastWindowClosed(False)

  app = App()
  app.run()
