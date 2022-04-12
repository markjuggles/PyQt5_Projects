# Tech With Tim
# PyQt5 Tutorial - Setup a Basic GUI Application
#   https://www.youtube.com/watch?v=Vde5SH8e1OQ
# PyQt5 Tutorial - PyQt5 Tutorial - Buttons and Events (Signals)
#   https://www.youtube.com/watch?v=-2uyzAqefyE&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj&index=2
#

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.count = 0
        self.xpos = 100
        self.ypos = 100
        self.width = 400
        self.height = 300
        self.setGeometry(self.xpos, self.ypos, self.width, self.height)
        self.setWindowTitle("Hello")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello There!")
        self.label.move(50, 50)
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Click Me')
        self.button1.clicked.connect(self.onClick)

    def onClick(self):
        self.count = self.count + 1
        self.label.setText("Press #" + str(self.count))
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
