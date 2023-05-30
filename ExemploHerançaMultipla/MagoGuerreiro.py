class Mago:
    def __init__(self, nome, escola_de_magia):
        self.nome = nome
        self.escola_de_magia = escola_de_magia

    def andar(self):
        print("O mago está andando.")

    def invocar_magia(self):
        print("O mago está invocando uma magia.")


class Guerreiro:
    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca

    def andar(self):
        print("O guerreiro está andando.")

    def atacar(self):
        print("O guerreiro está atacando.")


class MagoGuerreiro(Mago, Guerreiro):
    def __init__(self, nome, escola_de_magia, forca):
        Mago.__init__(self, nome, escola_de_magia)
        Guerreiro.__init__(self, nome, forca)

    def andar(self):
        print("O Mago Guerreiro está andando,")

# Exemplo de uso
mago_guerreiro = MagoGuerreiro("Merlin", "Escola de Magia de Avalon", 10)
mago_guerreiro.andar()  # Chamando o método 'andar' da classe MagoGuerreiro
mago_guerreiro.invocar_magia()  # Chamando o método 'invocar_magia' da classe Mago
mago_guerreiro.atacar()  # Chamando o método 'atacar' da classe Guerreiro