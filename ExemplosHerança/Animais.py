import pygame

# Sons retirados de https://freeanimalsounds.org/
# Para instalar o Pygame (não obrigatório): https://www.pygame.org/wiki/GettingStarted 

# Inicializa a pygame
pygame.init()

# Classe base
class Animal:
    def __init__(self, nome, som=None):
        self.nome = nome
        # Carrega o arquivo de som
        if som != None:
            self.som_bicho = pygame.mixer.Sound(som)
        else:
            self.som_bicho = None
        print("Foi  criado um animal chamado ",self.nome)

    def fazer_som(self):
        if self.som_bicho != None:
            # Reproduz o som
            self.som_bicho.play()
        else: 
            print("Esse animal não possui som!")

# Classe derivada
class Gato(Animal):
    def __init__(self, nome): #especialização do construtor
        super().__init__(nome, "Katze_miaut.mp3") #se necessário, pode chamar o código do método na classe base
        print("Foi criado o gato ", self.nome) 
    def fazer_som(self): #especialização do método fazer som
        print(self.nome, " é um gato. O gato mia.")
        super().fazer_som()
    def arranhar(self):
        print(self.nome, "está arranhando.")

# Classe derivada
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Bluthund_jault.mp3")
        print("Foi criado o cachorro ", self.nome) 
         
    def fazer_som(self):
        print(self.nome, "é um cachorro. O cachorro late.")
        super().fazer_som()

    def darPatinha(self):
        print(self.nome, " esta dando a patinha.")

# Classe derivada
class Galinha(Animal):
    def __init__(self, nome):
        super().__init__(nome, "huehner.mp3")
        print("Foi criado a galinha ", self.nome) 
         
    def fazer_som(self):
        print(self.nome, "é uma galinha. A galinha cacareja.")
        super().fazer_som()
    
    def porOvo(self):
        print(self.nome, "colocou um ovo!")
        

# Criando objetos
animal = Animal("Animal")
gato = Gato("Garfield")
cao = Cachorro("Lassie")
galinha = Galinha("Marilu")

# Chamando os métodos
animal.fazer_som()  
gato.fazer_som()    
cao.fazer_som()
galinha.fazer_som()

gato.arranhar()
cao.darPatinha()
galinha.porOvo()

input("Pressione qualquer tecla para finalizar")

# Encerra a pygame
pygame.quit()