from Figurinha import Figurinha # para poder usar a classe Figurinha
from Menus import *
import csv

class Aplicacao:

    # Método construtor
    def __init__(self):
        self.tela = 0
        self.terminou = False
        self.carregarFigurinhas()
        # Fazer os outros carregamentos pertinentes
        #carregarUsuarios()

    
    # Método que possui o loop principal
    def executar(self):
        opcao = -1
        while not self.terminou:
            ##########################################
            if self.tela == 0: #tela entrada
                self.telaInicial()
            ##########################################        

            elif self.tela == 1: #tela gerenciar album
                self.telaGerenciarAlbum()

            ##########################################
            elif self.tela == 2: #tela gerenciar colecao
                self.telaGerenciarColecao()

    # Método que prepara a aplicação para seu término
    def finalizar(self):
        print('Finalizando a aplicacao!')
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

    def msgErro(self, codigo):
        if codigo == 1:
            print('Opcao invalida!')
            input('Pressione qualquer tecla para continuar')

    # Processa as opções da Tela Inicial - 0
    def telaInicial(self):
        opcao = menuInicial()
        if opcao == '0':
            self.terminou = True
        elif opcao == '1':
            self.cadastrarUsuario()
        elif opcao == '2':
            self.acessarAlbum()
        else:
            self.msgErro(1)
        

    # Processa as opções da Tela Gerenciar Album - 1
    def telaGerenciarAlbum(self):
        opcao = menuGerenciarAlbum()
        if opcao == '0':
            self.tela = 0  #muda para a tela inicial
        else:
            self.msgErro(1)

     # Processa as opções da Tela Gerenciar Colecao - 2
    def telaGerenciarColecao(self):
        opcao = menuGerenciarColecao()
        if opcao == '0':
            self.tela = 1  #muda para a tela Gerenciar Album
        else:
            self.msgErro(1)

    def cadastrarUsuario(self):
        print('Cadastrando usuario....')
        input('Pressione qualquer tecla para continuar...')

    def acessarAlbum(self):
        print('Verificando usuario e recuperando o album do usuario')
        # Se conseguiu acessar, mudar para tela de Gerenciamento do Album
        self.tela = 1
        input('Pressione qualquer tecla para continuar...')