from Figurinha import Figurinha 
import csv

arqFigurinhas = open('FigurinhasDino.csv')
leitor = csv.reader(arqFigurinhas,delimiter=';')
listaFig = list(leitor)
arqFigurinhas.close()

listaFigurinhas = []

for i in range(len(listaFig)): #percorre linhas
    figurinha = Figurinha(int(listaFig[i][0]),listaFig[i][1],listaFig[i][2],int(listaFig[i][3]))                        
    listaFigurinhas.append(figurinha)               

for i in range(len(listaFigurinhas)):
    listaFigurinhas[i].imprimir()