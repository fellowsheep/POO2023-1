def cumprimentar(nome):
    print('Ola, ', nome)


#--------

cumprimentar('Rossana')

nome = 'Rafael'
nome2 = 'Valentina'

cumprimentar(nome)
cumprimentar(nome2)

nome3 = input('Digite um nome: ')

cumprimentar(nome3)

nomes = [ 'Ana', 'Pedro', 'Maria', 'Joao', 'Francisca']

for i in nomes:
    cumprimentar(i)

for i in range(len(nomes)):
    cumprimentar(nomes[i])


