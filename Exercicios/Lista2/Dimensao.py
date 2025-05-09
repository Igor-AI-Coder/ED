class Dimensao:
    def __init__(self, altura, comprimento, largura):
        self.altura = altura
        self.comprimento = comprimento	
        self.largura = largura
    @property
    def altura(self):
        return self.__altura
    @property
    def comprimento(self):
        return self.__comprimento
    @property
    def largura(self):
        return self.__largura
    @altura.setter
    def altura(self, nova_altura):
        self.__altura = nova_altura
    @largura.setter
    def largura(self, nova_largura):
        self.__largura = nova_largura
    @comprimento.setter
    def comprimento(self,novo_comprimento):
        self.__comprimento = novo_comprimento
    def __str__(self):
        return f'Altura: {self.__altura}, Largura: {self.__largura}, Comprimento: {self.__comprimento}'

dimensao = Dimensao(1.67,1.81,4.37)