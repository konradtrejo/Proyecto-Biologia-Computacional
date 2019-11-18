
import os

from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
from Bio.Phylo.PhyloXML import Phylogeny
from Bio.Phylo import PhyloXML
from Bio import Entrez
import csv
import os
import numpy as np


"""outputFilenameFasta = "CYTB_Especies.fasta"
clustalw_exe = "clustalw\clustalw2.exe"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile=outputFilenameFasta)
#print(clustalw_cline)
assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
clustalw_cline()"""


tabla_nombre_y_accession = []
elements_especies = []

with open('lista.csv') as File:  
    reader = csv.reader(File, delimiter = ';')
    for row in reader:
        tabla_nombre_y_accession.append(row[1])
        elements_especies.append(row[0])
    #print(self.elements_especies)

##for i in range(len(tabla_nombre_y_accession)):
#    tabla_nombre_y_accession[i][0] = tabla_nombre_y_accession[i][0].split(';')
aaa = np.array(tabla_nombre_y_accession)  
print(tabla_nombre_y_accession)
#print(aaa)

def Nombre(accession):
    verdad = accession in tabla_nombre_y_accession                           #tabla_nombre_y_accession.
    if(verdad):
        lugar = tabla_nombre_y_accession.index(accession)
        animal = elements_especies[lugar]
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

tree = Phylo.read("CYTB_Especies.dnd", "newick")
Phylo.draw_ascii(tree)

egfr_phy = tree.as_phyloxml()

for clade in egfr_phy.get_terminals():
    key = clade.name
    accession = str(key)
    accession = accession[:11]
    animal = Nombre(accession)
    clade.name = animal

Phylo.draw_ascii(egfr_phy)
   
"""

accession = str(key)
accession = accession[:11]
print(accession)


      
        
print(animal)
        

for clade in egfr_phy.get_terminals():
    key = clade.name
    accession = PhyloXML.Accession(key, 'NCBI')
    mol_seq = PhyloXML.MolSeq(lookup[key], is_aligned=True)
    sequence = PhyloXML.Sequence(type='aa', accession=accession, mol_seq=mol_seq)
    clade.sequences.append(sequence)

handle = Entrez.efetch(db="nucleotide", id="186972394", retmode="xml")
output = Entrez.read(handle)
print(output)


alingnment = AlignIO.read(open("CYTB_Especies.aln"),"clustal")

self.textEdit.append("longitud del Alineamiento multiple: \n %i " %alingnment.get_alignment_length())
#print(len(self.records))
self.records.clear()
"""
