class Carro:
    def __init__(self,placa,cor,dimensao,motor):
        self.__placa = placa
        self.__cor = cor
        self.__dimensao = dimensao
        self.__motor = motor
    @property
    def cor(self):
        return self.__cor
    @property
    def placa(self):
        return self.__placa
    @property
    def dimensao(self):
        return self.__dimensao
    @property
    def motor(self):
        return self.__motor
    @placa.setter
    def placa (self, nova_placa):
        self.__placa = nova_placa
    def __str__(self):
        return f'Cor: {self.__cor}, Placa: {self.__placa}, Dimensao: {self.__dimensao}, Motor: {self.__motor}'
