class Pais:
    def __init__(self, nome, capital, dimensao):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteira = []
    @property
    def nome(self):
        return self.__nome
    @property
    def capital(self):
        return self.__capital
    @property
    def dimensao(self):
        return self.__dimensao
    @property
    def pais_fronteira(self):
        return self.__fronteira
    def adicionar(self, pais):
        if pais not in self.__fronteira:
            self.__fronteira.append(pais)

    def __str__(self):
        return f'O nome do país é {self.__nome}, o nome da capital do país é {self.__capital}, a dimensão do país é {self.__dimensao} e os países que fazem fronteira com ele são {self.__fronteira}'
    
pais = Pais('França', 'Paris', 551.695)
pais.adicionar('Espanha')
pais.adicionar('Andorra')
pais.adicionar('Itália')
print(pais)

