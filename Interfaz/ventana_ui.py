# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        MainWindow.setStyleSheet("*{\n"
"    font: 16pt \"Pristina\";\n"
"}\n"
"\n"
"QLabel#label_2{\n"
"    font: 87 italic 11pt \"Segoe UI Black\";\n"
"}\n"
"\n"
"\n"
"QLabel#TextArea{\n"
"\n"
"    border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(238, 255, 253);\n"
"\n"
"}\n"
"\n"
"\n"
"QMainWindow{\n"
"background-color: rgb(218, 218, 163);\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: rgb(28, 195, 255);\n"
"    alternate-background-color: rgb(53, 53, 53);\n"
"    background-color: rgb(61, 123, 184);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 330, 221, 23))
        self.pushButton.setStyleSheet("")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 461, 61))
        self.label_2.setMinimumSize(QtCore.QSize(461, 0))
        self.label_2.setMaximumSize(QtCore.QSize(461, 16777215))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 370, 221, 23))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 410, 221, 23))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 80, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 150, 261, 131))
        self.listWidget.setStyleSheet("QWidget{Color:rgb(49, 97, 94)}")
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(460, 130, 311, 271))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.listWidget.raise_()
        self.textEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 35))
        self.menubar.setObjectName("menubar")
        self.menuhola = QtWidgets.QMenu(self.menubar)
        self.menuhola.setObjectName("menuhola")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCortar = QtWidgets.QAction(MainWindow)
        self.actionCortar.setObjectName("actionCortar")
        self.actionCopiar = QtWidgets.QAction(MainWindow)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionPegar = QtWidgets.QAction(MainWindow)
        self.actionPegar.setObjectName("actionPegar")
        self.actionAyuda = QtWidgets.QAction(MainWindow)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuhola.addSeparator()
        self.menuhola.addAction(self.actionNuevo)
        self.menuhola.addAction(self.actionAbrir)
        self.menuhola.addAction(self.actionGuardar)
        self.menuhola.addSeparator()
        self.menuhola.addAction(self.actionSalir)
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addAction(self.actionPegar)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuhola.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto Arboles Filogeneticos"))
        self.pushButton.setText(_translate("MainWindow", "Subir proteinas en formato fasta"))
        self.label_2.setText(_translate("MainWindow", "\n"
"Comparación de especies y generación de árboles \n"
" evolutivos de felinos y camélidos del Perú y de África"))
        self.pushButton_2.setText(_translate("MainWindow", "Realizar alineamiento múltiple "))
        self.pushButton_3.setText(_translate("MainWindow", "Árbol Filogenético"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Seleccionar"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Especies"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Genes"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Proteinas"))
        self.label_3.setText(_translate("MainWindow", "Salida"))
        self.menuhola.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar "))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionCortar.setText(_translate("MainWindow", "Cortar"))
        self.actionCopiar.setText(_translate("MainWindow", "Copiar"))
        self.actionPegar.setText(_translate("MainWindow", "Pegar"))
        self.actionAyuda.setText(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

