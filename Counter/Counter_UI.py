# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Counter_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 156)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_count = QtWidgets.QLabel(self.centralwidget)
        self.lbl_count.setGeometry(QtCore.QRect(270, 21, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_count.setFont(font)
        self.lbl_count.setObjectName("lbl_count")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 211, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_up = QtWidgets.QPushButton(self.layoutWidget)
        self.pb_up.setObjectName("pb_up")
        self.horizontalLayout.addWidget(self.pb_up)
        self.pb_down = QtWidgets.QPushButton(self.layoutWidget)
        self.pb_down.setObjectName("pb_down")
        self.horizontalLayout.addWidget(self.pb_down)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCount = QtWidgets.QMenu(self.menubar)
        self.menuCount.setObjectName("menuCount")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.menuFile.addAction(self.actionExit)
        self.menuCount.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCount.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_count.setText(_translate("MainWindow", "0"))
        self.pb_up.setText(_translate("MainWindow", "Up"))
        self.pb_down.setText(_translate("MainWindow", "Down"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCount.setTitle(_translate("MainWindow", "Count"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the program."))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setStatusTip(_translate("MainWindow", "Clear the counter."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
