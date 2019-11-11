################################################################################3
#           PROYECTO DE BIOLOGIA COMPUTACIONAL 
#NOMBRES: TALLA CHUMPITAZ, ERWIN 
#          TREJO CHAVEZ, KONRAD BENJAMIN
#
#2019-2
# Logica del Proyecto BioPython
#20/10/19
###############################################################################


from ventana_ui import *
from Bio import AlignIO
import csv
from Bio import SeqIO
import os

class MainWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)

        #self.label.setText("Haz click en el boton")
        #self.pushButton.setText("Presioname")

        #evento del button
        self.pushButton.clicked.connect(self.actualizar)
        self.comboBox.currentTextChanged.connect(self.selectionchange)
        self.pushButton_2.clicked.connect(self.alinemiento_Multiple)
        self.pushButton_3.clicked.connect(self.arbol_filogenetico)
        self.elements_especies = []
        self.records = []
        self.outputFilename = "CYTB_Especies.fasta"
        #self.elements_genes =[]
        #self.elements_protein = []

    def listar(self):
        with open('lista.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                self.elements_especies.append(row[0])
            #print(self.elements_especies)

    def actualizar(self):
        self.textEdit.append("Uno de los principales problemas que tuvo Universitario para mantener el liderato del Torneo Clausura fue la falta de gol de sus atacantes. Y las estadísticas son contundentes para ratificar dicho déficit: es el tercer cuadro con menos tantos a favor (11) del segundo torneo del año , marcó una sola conquista en los últimos cinco encuentros, y Alejandro Hohberg es el único que cumplió con la cuota goleadora (8 tantos en 30 partidos) que exige su posición ofensiva en el campo de juego.")
    
    def selectionchange(self):
        
        if str(self.comboBox.currentText())=="Especies":
            self.listar()
            self.listWidget.addItems(self.elements_especies)
            self.textEdit.clear()
            

        elif str(self.comboBox.currentText())=="Genes":
            self.listWidget.clear()
            self.listWidget.addItem("CYTB")
        else:
            self.listWidget.clear()
            
    def alinemiento_Multiple(self):
        if str(self.comboBox.currentText())=="Especies":
            for filename in os.listdir("Fastas/Camelidae/Genes"):
                handle = open("Fastas/Camelidae/Genes"+"/"+filename)
                record =SeqIO.read(handle,"fasta")
                self.records.append(record)
            
            for filename in os.listdir("Fastas/Felidae/Genes/CYTB"):
                handle = open("Fastas/Felidae/Genes/CYTB"+"/"+filename)
                record =SeqIO.read(handle,"fasta")
                self.records.append(record)
            
            SeqIO.write(self.records,self.outputFilename,"fasta")
            #-----Para windows no deja poner clustal como sub comado shell------
            #action= os.system("dir > algo.txt")
            #------Para linux descomentar la siguiente linea--------
            #action= os.system("clustalw self.outputFilename")
            alingnment = AlignIO.read(open("CYTB_Especies.aln"),"clustal")
            self.textEdit.append("longitud del Alineamiento multiple: \n %i " %alingnment.get_alignment_length())
            #print(len(self.records))
            self.records.clear()

    def arbol_filogenetico(self):
        pass 

    



if __name__=="__main__":

    app = QtWidgets.QApplication([])
    windows = MainWindows()
    windows.move(250,0)
    windows.show()
    app.exec_()
