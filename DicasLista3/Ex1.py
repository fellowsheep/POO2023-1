class Pais:
    def __init__(self,codigo=None,nome=None,dimensao=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__dimensao = dimensao
        self.__populacao = 0
        self.__vizinhos = []

    def setCodigo(self,codigo):
        self.__codigo = codigo

    def getCodigo(self):
        return self.__codigo    
    
    def compararIgual(self,pais):
        #retorna true/false
        if self.__codigo == pais.getCodigo():
            return True
        else:
            return False

    def verificarVizinho(self,pais):
        for i in self.__vizinhos:
            if i.compararIgual(pais) == True:
                return True
        return False

    def calcularDensidade(self):
        pass

    #OBS.: este método está errado (em revisão) -- CORRIGIDO!!!!
    def vizinhosComuns(self,pais):
        vizinhosPais = pais.getVizinhos() #pega a listagem de vizinhos do outro pais
        vizinhosAmbos = [] #inicia a lista dos vizinhos comuns a ambos
        for i in vizinhosPais:  
            if self.verificarVizinho(i) == True: #verifica se o vizinho do outro país é vizinho do país
                vizinhosAmbos.append(i) #adiciona na lista de ambos se verdadeiro! :)
        return vizinhosAmbos #retorna a lista, como o exercício pede!


    def adicionarVizinho(self,pais):
        self.__vizinhos.append(pais)

    def getVizinhos(self):
        return self.__vizinhos
    
    def listarVizinhos(self):
        for i in self.__vizinhos:
            print(i.getCodigo())







#####################

pais01 = Pais('BRA','Brasil',100)

pais02 = Pais()

pais02.setCodigo('ARG')
pais03 = Pais('URU','Uruguai',100)
pais04 = Pais('PAR','Paraguai',100)
pais05 = Pais('CHI','Chile',100)
pais06 = Pais('PER','Peru',100)

#adicionando vizinhos ao BRA
pais01.adicionarVizinho(pais02)
pais01.adicionarVizinho(pais03)
pais01.adicionarVizinho(pais04)
pais01.adicionarVizinho(pais06)

#adicionando vizinhos a ARG

pais02.adicionarVizinho(pais01)
pais02.adicionarVizinho(pais03)
pais02.adicionarVizinho(pais04)
pais02.adicionarVizinho(pais05)

print(pais01.getCodigo())
print(pais02.getCodigo())

print(pais01.compararIgual(pais02))

pais01.listarVizinhos()
pais02.listarVizinhos()
# print(pais02.getVizinhos())

print('-----------------')

vizinhosComuns = pais01.vizinhosComuns(pais02)
for i in vizinhosComuns:
    print(i.getCodigo())