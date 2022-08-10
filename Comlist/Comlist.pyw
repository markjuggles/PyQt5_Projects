# Program:  comlist.py
# Date:     04/18/2022
# Purpose:  1. Button to capture all of the Windows COM Ports.
#           2. Add the new COM Port. 
#           3. Button to report the added COM Port.
#
# Designer: Comlist_UI.ui
# Compile:  pyuic5 -x Comlist_UI.ui -o Comlist_UI.py

from PyQt5 import QtCore, QtGui, QtWidgets
import Comlist_UI
import os
import subprocess

class Ui_MainWindow(Comlist_UI.Ui_MainWindow):
    
    comlist = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.btnExisting.clicked.connect(self.btnExisting_clicked)
        self.btnAdded.clicked.connect(self.btnAdded_clicked)
        self.btnExisting.setDisabled(False)
        self.btnAdded.setDisabled(True)
        self.textBrowser.setText("Ready.")
        

    def btnExisting_clicked(self):
        global comlist

        self.btnExisting.setDisabled(True)
        self.btnAdded.setDisabled(False)
        self.textBrowser.setText("Searching...")
        cmd = 'mode | find "COM"'
        cmd_output = subprocess.check_output(cmd, shell=True)       # Run the command and capture the output as a byte list.
        val = cmd_output.decode("utf-8")                            # Convert the output to a big string.
        comlist = val.split('\n')                                   # Create a list of each line of output as a string.
        self.textBrowser.setText("Plug in new COM Port.")
 

    def btnAdded_clicked(self):
        global comlist
        found = False

        self.btnAdded.setDisabled(True)

        self.textBrowser.setText("")
        cmd = 'mode | find "COM"'
        cmd_output = subprocess.check_output(cmd, shell=True)       # Run the command and capture the output as a byte list.
        val = cmd_output.decode("utf-8")                            # Convert the output to a big string.
        newlist = val.split('\n')                                   # Create a list of each line of output as a string.

        for port in newlist:
            if port not in comlist:
                port_id = port.replace('Status for device ', '')
                self.textBrowser.setText(port_id)
                found = True

        if not found:
            self.textBrowser.setText("COM Port not detected.")

        self.btnExisting.setDisabled(False)
       

    def file_exit(self):
        os._exit(0)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Comlist")
    MainWindow.setWindowIcon(QtGui.QIcon('acorn.png'))
    MainWindow.show()
    sys.exit(app.exec_())
