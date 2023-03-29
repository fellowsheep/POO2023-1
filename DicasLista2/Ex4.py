import random

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0
    
    def atualizar(self):
        pass # atualiza a posicao de acordo com as regras descritas abaixo 
    
    def getPos(self):
        return self.pos
    

#inicializar a lista de competidores
nomes = ['Pafuncio', 'Frederico', 'Genoveva', 'Gertrudes', 'Astolfo']
competidores = []
for i in range (5):
    competidor = Competidor(nomes[i])
    competidores.append(competidor)


