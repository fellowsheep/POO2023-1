from Pagina import *

NRO_FIGURINHAS = 15
NRO_PAGINAS = 3

class Album:
    def __init__(self):
        self.paginas = [] 
        for i in range(NRO_PAGINAS):
            pagina = Pagina(i)
            self.paginas(pagina)
        self.colecao = []
        for i in range(NRO_FIGURINHAS):
            self.colecao[i].append(0)  #começa zerada
            self.colecao[i].append(False) #começa indisponível para troca

        self.requisicoes = []

    def exibirPagina(self,nro):
        self.pagina[nro].exibir()

    def exibirColecao():
        pass

    def exibirRequisicoes():
        pass

    def adicionarFigurinha(self,nro):
        self.colecao[nro]