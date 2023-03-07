import random

baseDeDados = [
    ['Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05'],
    [ 'Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58' ],
    [ 'Rock’n Rolo', 'The Buns','Rock',	1984, '4:01' ],
    [ 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' ],
    ['Outra musica', 'Anira', 'Funk', 2019, '3:05']
]

def ExibirBaseDados():
    id = 0
    for i in baseDeDados:
        for j in i:
            print (id, '\t',j, end = '\t')
        id = id + 10
        print() #quebra de linha

# a) Visualizar base de dados: se escolhida esta opção, o programa deve mostrar ao usuário a tabela com todas as músicas
ExibirBaseDados()

#b) Montar uma playlist: quando o usuário escolher esta opção, o programa deve permitir, enquanto ele quiser, adicionar músicas da base de dados. Para isso, o usuário deve fornecer um ID válido da música do banco de dados e este ID deve ser armazenado na lista. Atenção! Só poderão ser adicionadas músicas que não estejam na playlist.
playlist = []

pararAdicionar = False
while not pararAdicionar:
    id = int(input('Digite o id da musica: '))
    jaExiste = False
    for i in range (len(playlist)):
        if playlist[i] == id:
            print('Musica já esta na playlist')
            jaExiste = True
            break
    if not jaExiste and id < len(baseDeDados): #nao encontrou e id é valido
        playlist.append(id)
    opcao = ''
    while opcao != 'S' and opcao != 'N':
        opcao = input('Deseja adicionar mais musicas? (S/N)')
        if opcao == 'N': 
            pararAdicionar = True
print(playlist) #print só para debug aqui

# c) Visualizar a playlist: se escolhida esta opção, o programa deve mostrar apenas as informações a respeito das músicas da playlist.
for i in playlist:
    print (baseDeDados[i])

# d)	Embaralhar playlist: se escolhida esta opção, o programa deve embaralhar a ordem das músicas da playlist e exibir o resultado.
random.shuffle(playlist)
print(playlist)

# e)	Mostrar a duração total da playlist, em minutos
totalTime = 0
for i in range(len(playlist)):
    timestr = baseDeDados[playlist[i]][4]
    mins = []
    mins =  timestr.split(':')
    m1 = float(mins[0])
    m2 = float(mins[1])
    m2 = m2/60.0
    totalTime += m1 + m2
print(totalTime)

# f)	Consultar música: o usuário entra com o título da música e o programa retorna o ID da música no banco de dados, se houver

titulo = input('Busca pelo titulo da musica. Digite o titulo a ser buscado: ')
encontrou = False
id = 0
while not encontrou and id < len(baseDeDados):
    if baseDeDados[id][0] == titulo:
        encontrou = True
    else:
        id = id + 1
if encontrou:
    print('A musica está na base de dados!')
else:
    print ('A musica nao está na base de dados')

# g)	Consultar por banda/artista: usuário entra com o nome da banda/artista e o programa retorna a lista da(s) ID(s) das música(s) encontradas, se houver.

nomeBanda = input('DIgite o nome da banda ou artista: ')
encontrou = False

for i in range(len(baseDeDados)):
            if baseDeDados[i][1] == nomeBanda:
                print (i, " ", baseDeDados[i])
                encontrou = True

if not encontrou:
    print('Nao encontramos nenhuma musica da banda/artista ', nomeBanda, ' em nossa base de dados')