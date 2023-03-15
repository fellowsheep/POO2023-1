# Definição da classe Mago 

class Mago:
    def __init__(self, nome, idade, escola):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola 
        
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')
        
        
#Intanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts')
gd = Mago('Gandalf', 2000, 'Magia Cinza')

print(hp.nome)
print(hp.idade)
print(hp.escola)

print(gd.escola)

hp.andar()
hp.falar()
hp.invocarMagia()

gd.falar()