class Musica:
    def __init__(self,titulo,banda,genero,ano,duracao):
        self.titulo = titulo
        self.banda = banda
        self.genero = genero
        self.ano = ano
        self.duracao = duracao
    
    def info(self): #exibe as informações (valores) dos atributos da música
        pass

    def retornarDuracao(self): #método de get da duração 
        return self.duracao
    

baseDeDados = []

# Criando um objeto da classe musica
    
musica = Musica('Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05')

baseDeDados.append(musica)

print(baseDeDados[0].titulo)
