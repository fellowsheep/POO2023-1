from Figurinha import Figurinha # para poder usar a classe Figurinha
import csv

# Abre o arquivo com as infos
arqFigurinhas = open('FigurinhasDino.csv')
# Faz a leitora do csv, agora com o delimitador certo
leitor = csv.reader(arqFigurinhas,delimiter=';')
# Transforma em lista 
listaFig = list(leitor)
# Nunca esqueça de fechar o arquivo!
arqFigurinhas.close()

# print(listaFig)

# Aqui será a lista de todas as figurinhas que o album possui
listaFigurinhas = []

for i in range(len(listaFig)): #percorre linhas
    # Instancia um objeto da classe Figurinha, passando por parâmetro as colunas da tabela (já convertendo os nros para int)
    figurinha = Figurinha(int(listaFig[i][0]),listaFig[i][1],listaFig[i][2],int(listaFig[i][3]))                        
    # Adiciona na lista de figurinhas
    listaFigurinhas.append(figurinha)               

# Manda imprimir o conteudo da lista de figurinhas
for i in range(len(listaFigurinhas)):
    listaFigurinhas[i].imprimir()