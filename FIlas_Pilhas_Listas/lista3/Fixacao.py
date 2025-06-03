class Data:
    def __init__(self,dia,mes,ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    @property
    def dia(self):
        return self.__dia
    @property
    def mes(self):
        return self.__mes
    @property
    def ano(self):
        return self.__ano
    @dia.setter
    def novo_dia(self, ndia):
        self.__dia = ndia
    @mes.setter
    def novo_mes(self, nmes):
        self.__mes = nmes
    @ano.setter
    def novo_ano(self, nano):
        self.__ano = nano
    def __str__(self):
        return f'A data escolhida: {self.__dia}/{self.__mes}/{self.__ano}'
dia = Data(29, 4 ,2025)
print (dia)
