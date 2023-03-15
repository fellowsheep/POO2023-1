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
        
        

hp = Mago('Harry Potter', 17, 'Hogwarts')

print(hp.nome)
print(hp.idade)
print(hp.escola)

hp.andar()
hp.falar()
hp.invocarMagia()