# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuAcercaDe.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuAcercaDe(object):
    def setupUi(self, MenuAcercaDe):
        MenuAcercaDe.setObjectName("MenuAcercaDe")
        MenuAcercaDe.resize(434, 412)
        self.centralwidget = QtWidgets.QWidget(MenuAcercaDe)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 431, 381))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        MenuAcercaDe.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuAcercaDe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        MenuAcercaDe.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuAcercaDe)
        self.statusbar.setObjectName("statusbar")
        MenuAcercaDe.setStatusBar(self.statusbar)

        self.retranslateUi(MenuAcercaDe)
        QtCore.QMetaObject.connectSlotsByName(MenuAcercaDe)

    def retranslateUi(self, MenuAcercaDe):
        _translate = QtCore.QCoreApplication.translate
        MenuAcercaDe.setWindowTitle(_translate("MenuAcercaDe", "Acerca De"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuAcercaDe = QtWidgets.QMainWindow()
    ui = Ui_MenuAcercaDe()
    ui.setupUi(MenuAcercaDe)
    MenuAcercaDe.show()
    sys.exit(app.exec_())

