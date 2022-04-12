# Tech With Tim
# PyQt5 Tutorial - Setup a Basic GUI Application
# https://www.youtube.com/watch?v=Vde5SH8e1OQ
#


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
xpos = 0
ypos = 0
width = 400
height = 300

def b1_clicked():
    print("Button 1 Clicked.")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("Hello")

    label = QtWidgets.QLabel(win)
    label.setText("Hello There!")
    label.move(50, 50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Push Me")
    b1.clicked.connect(b1_clicked)




    win.show()
    sys.exit(app.exec_())


window()
