import random

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.numero_vitorias = 0

class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.competidores = []
        self.numero_vitorias = 0
        self.indice_competidor = 0

    def adicionar_competidor(self, competidor):
        self.competidores.append(competidor)

    def selecionar_competidor(self):
        selecionado = self.competidores[self.indice_competidor]
        self.indice_competidor = (self.indice_competidor + 1) % len(self.competidores)
        return selecionado

class JogoJoKenPo:
    def __init__(self, equipe1, equipe2):
        self.equipe1 = equipe1
        self.equipe2 = equipe2

    def jogar(self):
        houve_empate = True
        competidor1 = self.equipe1.selecionar_competidor()
        competidor2 = self.equipe2.selecionar_competidor()
        venceu_round = 1

        while self.equipe1.numero_vitorias < 10 and self.equipe2.numero_vitorias < 10:
            if houve_empate == False:
                if venceu_round == 2:
                    competidor1 = self.equipe1.selecionar_competidor()
                else: competidor2 = self.equipe2.selecionar_competidor()
            else: houve_empate = False

            escolha1 = random.choice(["Pedra", "Papel", "Tesoura"])
            escolha2 = random.choice(["Pedra", "Papel", "Tesoura"])

            print(f"Competidor {competidor1.nome} da Equipe {self.equipe1.nome}: {escolha1}")
            print(f"Competidor {competidor2.nome} da Equipe {self.equipe2.nome}: {escolha2}")

            if escolha1 == escolha2:
                print("Empate! Repetindo o round...\n")
                houve_empate = True
                continue
            elif (escolha1 == "Pedra" and escolha2 == "Tesoura") or (escolha1 == "Papel" and escolha2 == "Pedra") or (escolha1 == "Tesoura" and escolha2 == "Papel"):
                print(f"Equipe {self.equipe1.nome} venceu o round!")
                self.equipe1.numero_vitorias += 1
                competidor1.numero_vitorias += 1
                venceu_round = 1
            else:
                print(f"Equipe {self.equipe2.nome} venceu o round!")
                self.equipe2.numero_vitorias += 1
                competidor2.numero_vitorias += 1
                venceu_round = 2


        equipe_vencedora = self.equipe1 if self.equipe1.numero_vitorias >= 10 else self.equipe2
        competidor_mencao_honrosa = max(self.equipe1.competidores + self.equipe2.competidores, key=lambda c: c.numero_vitorias)

        print(f"\nA equipe vencedora é: {equipe_vencedora.nome}")
        print(f"Competidor com mais vitórias pessoais: {competidor_mencao_honrosa.nome}")

# Criando as equipes e competidores
equipe1 = Equipe("Equipe 1")
equipe2 = Equipe("Equipe 2")

competidor1 = Competidor("Alice")
competidor2 = Competidor("Bob")
competidor3 = Competidor("Carol")

equipe1.adicionar_competidor(competidor1)
equipe1.adicionar_competidor(competidor2)
equipe1.adicionar_competidor(competidor3)

competidor4 = Competidor("Dave")
competidor5 = Competidor("Eva")
competidor6 = Competidor("Frank")

equipe2.adicionar_competidor(competidor4)
equipe2.adicionar_competidor(competidor5)
equipe2.adicionar_competidor(competidor6)

jogo = JogoJoKenPo(equipe1, equipe2)
jogo.jogar()