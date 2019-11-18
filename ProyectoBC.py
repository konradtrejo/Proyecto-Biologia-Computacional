################################################################################3
#           PROYECTO DE BIOLOGIA COMPUTACIONAL 
#NOMBRES:  TALLA CHUMPITAZ, REEWOS ERWIN 
#          TREJO CHAVEZ, KONRAD BENJAMIN
#
#2019-2
# Logica del Proyecto BioPython
#20/10/19
###############################################################################


from  Interfaz.ventana_ui import *
from Bio import AlignIO
import csv
from Bio import SeqIO
import os

from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
from Bio.Phylo.PhyloXML import Phylogeny
from Bio.Phylo import PhyloXML
from Bio import Entrez

import matplotlib
import matplotlib.pyplot as plt

from Interfaz.MenuAyuda_ui  import Ui_MenuAyuda
from Interfaz.MenuAcercaDe_ui import Ui_MenuAcercaDe

class MainWindows(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)

        #self.label.setText("Haz click en el boton")
        #self.pushButton.setText("Presioname")

        #evento del button
        self.actionAyuda.triggered.connect(self.ayuda)
        self.actionAcerca_de.triggered.connect(self.acercaDe)
        self.pushButton.clicked.connect(self.actualizar)
        self.comboBox.currentTextChanged.connect(self.selectionchange)
        self.pushButton_2.clicked.connect(self.alinemiento_Multiple)
        self.pushButton_3.clicked.connect(self.arbol_filogenetico)
        self.elements_especies = []
        self.tabla_accession = []
        self.records = []
        self.outputFilenameFasta = "CYTB_Especies.fasta"
        self.outputFilenameAln = "CYTB_Especies.aln"
        self.outputFilenameDnd = "CYTB_Especies.dnd"
        #self.elements_genes =[]
        #self.elements_protein = []

    def ayuda(self):
       self.mAyuda=QtWidgets.QMainWindow()
       self.ui = Ui_MenuAyuda()
       self.ui.setupUi(self.mAyuda)
       
       f = open ('Interfaz/ayuda.txt','r')
       mensaje = f.read()
       f.close()
       self.ui.textEdit.append(str(mensaje))
       self.mAyuda.show()
    
    def acercaDe(self):
       self.mAcercaDe=QtWidgets.QMainWindow()
       self.ui = Ui_MenuAcercaDe()
       self.ui.setupUi(self.mAcercaDe)
       f = open ('Interfaz/acercaDe.txt','r')
       mensaje = f.read()
       f.close()
       self.ui.textEdit.append(str(mensaje))
       self.mAcercaDe.show()
    
    def listar(self):
        with open('lista.csv') as File:  
            reader = csv.reader(File, delimiter = ';')
            for row in reader:
                self.tabla_accession.append(row[1])
                self.elements_especies.append(row[0])
            #print(self.elements_especies)

    def actualizar(self):
        text = "adf "
        self.textEdit.append(text)
    
    def selectionchange(self):
        
        if str(self.comboBox.currentText())=="Especies":
            self.listWidget.clear()
            self.listar()
            self.listWidget.addItems(self.elements_especies)
            self.textEdit.clear()
            

        elif str(self.comboBox.currentText())=="Genes":
            self.listWidget.clear()
            self.listWidget.addItem("CYTB")
            self.textEdit.clear()
        else:
            self.listWidget.clear()
            
    def Nombre(self,accession):                     #Devuelve el nombre del organismo
        verdad = accession in self.tabla_accession  #con solo su numero de acceso
        if(verdad):
            lugar = self.tabla_accession.index(accession)
            animal = self.elements_especies[lugar]
            animal = str(animal)
            return animal
        else:
            Entrez.email = 'gajar85485@itymail.com'
            handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
            result=handle.read().split('\n')
            
            for line in result:
                if 'ORGANISM' in line:
                   animal = ' '.join(line.split()[1:])
            return animal

            
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
            
            self.textEdit.append("* Se cargaron los archivos FASTA")
            SeqIO.write(self.records,self.outputFilenameFasta,"fasta")
            fasta_name = self.outputFilenameFasta
            self.textEdit.append("* Se creo el archivo "+ str(fasta_name) +", donde se encuentran todos los archivos FASTA a analizar ," )
            clustalw_exe = "clustalw\clustalw2.exe"
            clustalw_cline = ClustalwCommandline(clustalw_exe, infile=self.outputFilenameFasta)
            self.textEdit.append("* Se procede a realizar el alineamiento con ClustalW")
            clustalw_cline()
            aln_name = self.outputFilenameAln
            dnd_name = self.outputFilenameDnd
            self.textEdit.append("* Se crearon dos archivos: "+ aln_name +" y "+ dnd_name)
            #------Para linux descomentar la siguiente linea--------
            #action= os.system("clustalw self.outputFilenameFasta")
            
            alingnment = AlignIO.read(open(self.outputFilenameAln),"clustal")
            
            self.textEdit.append("* Longitud del Alineamiento multiple: %i " %alingnment.get_alignment_length())
            #print(len(self.records))
            self.records.clear()

    def arbol_filogenetico(self):
        self.textEdit.append("* Se presentará el árbol filogenético en otra ventana")
        tree = Phylo.read(self.outputFilenameDnd, "newick")
        new_tree = tree.as_phyloxml()
        
        for clade in new_tree.get_terminals():
            key = clade.name
            accession = str(key)
            accession = accession[:11]
            animal = self.Nombre(accession)
            clade.name = animal
        #self.textEdit.append(str(new_tree))
        fig = plt.figure(figsize=(10, 20), dpi=100)
        axes = fig.add_subplot(1, 1, 1)
        Phylo.draw(new_tree, axes=axes)
        self.textEdit.append("* Ahora puede visualizarlo mejor")



if __name__=="__main__":
    
    app = QtWidgets.QApplication([])
    windows = MainWindows()
    windows.move(250,0)
    windows.show()
    app.exec_()
