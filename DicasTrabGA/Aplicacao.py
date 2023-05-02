from Figurinha import Figurinha # para poder usar a classe Figurinha
from Menus import *
import csv

class Aplicacao:

    # Método construtor
    def __init__(self):
        self.tela = 0
        self.carregarFigurinhas()
        # Fazer os outros carregamentos pertinentes
        #carregarUsuarios()

    
    # Método que possui o loop principal
    def executar(self):
        opcao = -1
        terminou = False
        while not terminou:
            ##########################################
            if self.tela == 0: #tela entrada
                opcao = menuEntrada()
                if opcao == '0':
                    terminou = True
                else:
                    self.msgErro(1)
            ##########################################        

            elif self.tela == 1: #tela gerenciar album
                pass

            ##########################################
            elif self.tela == 2: #tela gerenciar colecao
                pass

    # Método que prepara a aplicação para seu término
    def finalizar(self):
        # executar os salvamentos nos arquivos
        pass

    # Carregamento do arquivo com as informações das figurinhas do album
    def carregarFigurinhas(self):
        # Abre o arquivo com as infos
        arqFigurinhas = open('FigurinhasDino.csv')
        # Faz a leitora do csv, agora com o delimitador certo
        leitor = csv.reader(arqFigurinhas,delimiter=';')
        # Transforma em lista 
        listaFig = list(leitor)
        # Nunca esqueça de fechar o arquivo!
        arqFigurinhas.close()

        # Aqui será a lista de todas as figurinhas que o album possui
        self.listaFigurinhas = []

        for i in range(len(listaFig)): #percorre linhas
            # Instancia um objeto da classe Figurinha, passando por parâmetro as colunas da tabela (já convertendo os nros para int)
            figurinha = Figurinha(int(listaFig[i][0]),listaFig[i][1],listaFig[i][2],int(listaFig[i][3]))                        
            # Adiciona na lista de figurinhas
            self.listaFigurinhas.append(figurinha)               

        # Manda imprimir o conteudo da lista de figurinhas -- apenas DEBUG, pode apagar depois
        for i in range(len(self.listaFigurinhas)):
            self.listaFigurinhas[i].imprimir()

    
    def msgsErro(self, codigo):
        if codigo == 1:
            print('Opcao invalida!')
            input('Pressione qualquer tecla para continuar')