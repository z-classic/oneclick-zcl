#!/usr/bin/python

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *


class App:
  def __init__(self):
    # Create a Qt application
    self.app = QApplication(sys.argv)

    icon = QIcon("zcl.svg")
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
    self.tray.setIcon(icon)
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
    self.dialog = QDialog()
    self.dialog.setWindowTitle("Title - Start Dialog")
    self.dialog.show()

  def configure(self):
    self.dialog = QDialog()
    self.dialog.setWindowTitle("Title - Configure Dialog")
    self.dialog.show()

  def about(self):
    self.dialog = QDialog()
    self.dialog.setWindowTitle("About - Contact & Donate Dialog")
    self.dialog.show()



if __name__ == "__main__":
  app = App()
  app.run()
