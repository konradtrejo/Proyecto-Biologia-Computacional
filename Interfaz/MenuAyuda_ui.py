# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuAyuda.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuAyuda(object):
    def setupUi(self, MenuAyuda):
        MenuAyuda.setObjectName("MenuAyuda")
        MenuAyuda.resize(434, 412)
        self.centralwidget = QtWidgets.QWidget(MenuAyuda)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 431, 381))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        MenuAyuda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuAyuda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        MenuAyuda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuAyuda)
        self.statusbar.setObjectName("statusbar")
        MenuAyuda.setStatusBar(self.statusbar)

        self.retranslateUi(MenuAyuda)
        QtCore.QMetaObject.connectSlotsByName(MenuAyuda)

    def retranslateUi(self, MenuAyuda):
        _translate = QtCore.QCoreApplication.translate
        MenuAyuda.setWindowTitle(_translate("MenuAyuda", "Ayuda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuAyuda = QtWidgets.QMainWindow()
    ui = Ui_MenuAyuda()
    ui.setupUi(MenuAyuda)
    MenuAyuda.show()
    sys.exit(app.exec_())

