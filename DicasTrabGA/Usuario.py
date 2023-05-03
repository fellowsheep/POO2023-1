

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.album = None

    def getNomeUsuario(self):
        return self.nome()
    
    def verificar(self,nome,senha):
        if self.nome == nome:
            if self.senha == senha:
                return True
            else:
                print('Senha invalida!')
                return False
        else:
            print('Nome de usuario invalido!')
            return False
    
    def getAlbum(self):
        return self.album 
