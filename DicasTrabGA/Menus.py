import os # Biblioteca de sistema operacional do Python

def menuEntrada():
    # Limpa a tela - Win/Linux/MacOS 
    os.system('cls') 
    print('----------------TELA PRINCIPAL----------------')
    print('1 - Novo Album')
    print('2 - Acessar Album')
    print('0 - Sair da Aplicacao\n')
    item = input('Escolha uma opcao: ')
    return item
