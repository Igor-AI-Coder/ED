class Motor:
    def __init__(self, motorizacao, combustivel = 'flex'):
        self.__motorizacao = motorizacao
        self.__combustivel = combustivel
    @property
    def motorizacao (self):
        return self.__motorizacao
    @property
    def combustivel(self):
        return self.__combustivel
    @motorizacao.setter
    def motorizacao(self, nova_motorizacao):
        self.__motorizacao = nova_motorizacao
    @combustivel.setter
    def combustivel(self, novo_combustivel):
        self.__combustivel = novo_combustivel
    def __str__(self):
        return f'Motorização: {self.__motorizacao}, Combustível: {self.__combustivel}'
motor = Motor('1.6','gasolina')
print(motor)