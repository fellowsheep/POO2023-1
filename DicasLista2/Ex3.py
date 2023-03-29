class Data:
    # def __init__(self, dia, mes, ano):
    #     self.dia = dia
    #     self.mes = mes
    #     self.ano = ano

    def __init__(self):
        self.__dia = 1 #privado
        self._mes = 1  #protegido
        self.ano = 0   #público 

    def alterarDia(self, dia): #Método de setar o valor do atributo dia
        self.__dia = dia

    def alterarMes(self, mes):
        self._mes = mes

    def alterarAno(self, ano):
        self.ano = ano

    def retornarDia(self): #Método para retornar o valo do atributo dia
        return self.__dia
    
    def exibirData(self):
        print(self.__dia,'/',self._mes,'/',self.ano)

    def retornarStrMes(self): 
        if self._mes == 1:
            return 'janeiro'
        elif self._mes == 2:
            return 'fevereiro'
        else:
            return 'lalala'
    
    def exibirDataPorExtenso(self,cidade):
        mes = self.retornarStrMes() #método chamado de dentro da própria classe
        print(cidade, ', ', self.__dia, ' de ' , mes, ' de ', self.ano)


class CadastroCliente:
    def __init__(self):
        self.nome = ''
        self.sobrenome = ''
        self.dataNascimento = ''
        self.email = ''
        self.cpf = ''
        self.__senha = ''
        self.__bloqueado = False

    # Métodos de set (setters)
    def alterarNome(self, nome):
        self.nome = nome

    def alterarSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def alterarDataNascimento(self, dia, mes, ano):
        self.dataNascimento = Data()
        self.dataNascimento.alterarDia(dia)
        self.dataNascimento.alterarMes(mes)
        self.dataNascimento.alterarAno(ano)

    def alterarEmail(self,email):
        self.email = email
        #recomendável fazer uma validação do email (@,.)
    
    def alterarCPF(self, cpf):
        #recomendável fazer validação: nro de caracteres e 
        #verificar se caracteres são numéricos
        #asciiCode = ord(cpf[i]) //recupera o valor em ascii
        #if (asciiCode >= 48 and asciiCode <=57): //é um caracter numerico
        self.cpf = cpf

    def alterarSenha(self, senha):
        # recomendável validar senha (caracter numérico, maiúscula...)
        self.__senha = senha
    
    def validarSenha(self, senhaDigitada):
        if self.__senha == senhaDigitada:
            return True
        else:
            return False
        
    def bloquear(self):
        self.__bloqueado = True

    # Métodos de get (getters): retornam valores dos atributos
    def retornaNome(self):
        return self.nome
    
    def retornaSobrenome(self):
        return sobrenome



cliente = CadastroCliente()

nome = input('Digite nome: ')
cliente.alterarNome(nome)
sobrenome = input('Digite sobrenome: ')
cliente.alterarSobrenome(sobrenome)
#.. fazer a leitura do restante e alterar no objeto do cadastro
senhaCriada = input('Digite a nova senha: ')
cliente.alterarSenha(senhaCriada)


contTentativas = 0
acertouSenha = False

while contTentativas < 3 and not acertouSenha:
    senhaDigitada = input('Digite sua senha cadastrada: ')
    validacao = cliente.validarSenha(senhaDigitada)
    if validacao == True:
        acertouSenha = True
    else:
        print('Senha incorreta!')
    contTentativas = contTentativas + 1

if (acertouSenha == False):
    #bloqueia a conta
    cliente.bloquear()
    print('Conta bloqueada!')
else:
    print('Dados do cliente: ')
    print(cliente.retornaNome(), ' ', cliente.retornaSobrenome())



    

