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


outraData = Data()

outraData.alterarDia(17)

dia = outraData.retornarDia()

print(dia)

print(outraData.retornarDia())

outraData.exibirData()

outraData.exibirDataPorExtenso('Sao Leopoldo')
# outraData.__dia = 17

# print(outraData._dia)