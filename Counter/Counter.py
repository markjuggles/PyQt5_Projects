# Program:  Counter_App.py
# Date:     04/10/2022
# Purpose:  Demonstrate how a the output of Qt5 Designer can be imported so that the GUI can be
#           refactored without losing application changes.
# Designer: Counter_UI.ui
# Compile:  pyuic5 -x Counter_UI.ui -o Counter_UI.py

from PyQt5 import QtCore, QtGui, QtWidgets
import Counter_UI
import os

class Ui_MainWindow(Counter_UI.Ui_MainWindow):
    
    count_value = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.pb_up.clicked.connect(self.pb_up_clicked)
        self.pb_down.clicked.connect(self.pb_down_clicked)
        self.actionExit.triggered.connect(self.file_exit)
        self.actionClear.triggered.connect(self.count_clear)

    def pb_up_clicked(self):
        self.count_value = self.count_value + 1
        self.lbl_count.setText(str(self.count_value))


    def pb_down_clicked(self):
        if self.count_value > 0:
            self.count_value = self.count_value - 1
            self.lbl_count.setText(str(self.count_value))

    def file_exit(self):
        os._exit(0)

    def count_clear(self):
        self.count_value = 0
        self.lbl_count.setText(str(self.count_value))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
