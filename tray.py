#!/usr/bin/python

# Import PySide classes
import sys
import subprocess 

from PySide.QtCore import *
from PySide.QtGui import *

from ConfigParser import SafeConfigParser


class App:
  def __init__(self):
    # Create a Qt application
    self.app = QApplication(sys.argv)
    self.app.setApplicationName("ZCL Miner")

    # Closing Dialogs shouldn't kill app
    QApplication.setQuitOnLastWindowClosed(False)

    self.startedIcon = QIcon("zcl-started.svg")
    self.stoppedIcon = QIcon("zcl-stopped.svg")

    menu = QMenu()

    startAction = menu.addAction("Start")
    startAction.triggered.connect(self.start)

    menu.addSeparator()

    configureAction = menu.addAction("Configure")
    configureAction.triggered.connect(self.configure)

    aboutAction = menu.addAction("About")
    aboutAction.triggered.connect(self.about)

    menu.addSeparator()

    exitAction = menu.addAction("Exit")
    exitAction.triggered.connect(sys.exit)

    self.donationAddress = "t1Wq2HdXZ7G9uYd1HppewSoMahGBt6ZVNUD"
    self.pools = ["stratum+tcp://zcl.suprnova.cc:4042", "X", "Y"]

    self.configFileName = "config.ini"

    self.config = SafeConfigParser()

    def createDefaultConfig():
      if self.config.has_section('zcl') == False:
          self.config.add_section('zcl')
          self.config.set('zcl', 'pool', 'stratum+tcp://zcl.suprnova.cc:4042')
          self.config.set('zcl', 'autostart', 'false')
          self.config.set('zcl', 'address', self.donationAddress)

          with open(self.configFileName, 'w') as cfg:
              self.config.write(cfg)

    if self.config.read(self.configFileName) != self.configFileName:
      createDefaultConfig()

    self.tray = QSystemTrayIcon()
    self.tray.setIcon(self.stoppedIcon)
    self.tray.setContextMenu(menu)

    self.tray.show()

    # TODO Alert Dialogs as needed
    #self.tray.showMessage("traymessage1_1", "traymessage1_2")


  def run(self):
    # Enter Qt application main loop
    self.app.exec_()
    sys.exit()

  # Start the Miner
  def start(self):

    params = (self.config.get('zcl', 'pool', self.pools[0]), self.config.get('zcl', 'address', self.donationAddress), 'x', '30', 'equihash200_9', '') # '-i 5'

    cmd = "GPU_FORCE_64BIT_PTR=1 ./optiminer-equihash-2.1.2/optiminer-equihash -s %s -u %s -p %s --watchdog-timeout %s -a %s --watchdog-cmd './watchdog-cmd.sh' %s"
    cmdToRun = cmd % params

    subprocess.call(cmdToRun, shell=True)

    #self.tray.showMessage("started", "started mining")
    self.tray.setIcon(self.startedIcon)

  # Stop the Miner
  def stop(self):

    cmd = "killall optiminer-equihash"

    subprocess.call(cmd, shell=True)

    #self.tray.showMessage("stopped", "stopped mining")
    self.tray.setIcon(self.stoppedIcon)

  def configure(self):
    self.dialog = QDialog(None, Qt.WindowStaysOnTopHint)
    self.dialog.setWindowTitle("Configure")

    poolLabel = QLabel("Pool:")

    self.poolComboBox = QComboBox()
    for p in self.pools:
        self.poolComboBox.addItem(p)
    self.poolComboBox.setCurrentIndex(self.pools.index(self.config.get("zcl", "pool", self.pools[0])))

    startOnOpenLabel = QLabel("Start Mining on Open?")
    self.startOnOpenCheckBox = QCheckBox()
    self.startOnOpenCheckBox.setChecked(self.config.get("zcl", "autostart", "false") == "True")

    addressLabel = QLabel("Your Address:")
    self.addressLineEdit = QLineEdit()
    self.addressLineEdit.setText(self.config.get("zcl", "address", self.donationAddress))
    #TODO self.addressLineEdit.setValidator(QStringValidator(...))

    def onOK():
        self.config.set('zcl', 'pool', self.pools[self.poolComboBox.currentIndex()])
        self.config.set('zcl', 'autostart', str(self.startOnOpenCheckBox.isChecked()))
        self.config.set('zcl', 'address', self.addressLineEdit.text())

        with open(self.configFileName, 'w') as cfg:
            self.config.write(cfg)

        self.dialog.close()

    saveButton = QPushButton("OK")
    saveButton.clicked.connect(onOK)

    # Create layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(poolLabel)
    layout.addWidget(self.poolComboBox)
    layout.addWidget(startOnOpenLabel)
    layout.addWidget(self.startOnOpenCheckBox)
    layout.addWidget(addressLabel)
    layout.addWidget(self.addressLineEdit)
    layout.addWidget(saveButton)

    self.dialog.setLayout(layout)

    self.dialog.show()

  def about(self):
    self.dialog = QDialog(None, Qt.WindowStaysOnTopHint)
    self.dialog.setWindowTitle("About")

    teamLabel = QLabel("Zclassic One-Click Miner (Equihash)")
    donateLabel = QLabel("Donate: %s" % self.donationAddress)

    feeLabel = QLabel("The Optiminer used by this software takes a 1%% dev fee. Read more: https://github.com/Optiminer/OptiminerEquihash")

    # Create layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(teamLabel)
    layout.addWidget(donateLabel)

    self.dialog.setLayout(layout)

    self.dialog.show()


if __name__ == "__main__":

  if not QSystemTrayIcon.isSystemTrayAvailable():
    QMessageBox.critical(None, "Error - System Tray",
        "Couldn't detect a system tray on this computer...")
    sys.exit(1)


  app = App()
  app.run()
