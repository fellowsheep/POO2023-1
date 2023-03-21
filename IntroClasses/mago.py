# Definição da classe Mago 

class Mago:
    # Atributos de classe
    possuiMagia = True

    # Método construtor
    def __init__(self, nome, idade, escola):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola 
        print('Mago ', self.nome, ' foi criado!')

    # Outros métodos    
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 
        
        
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

del hp
del gd