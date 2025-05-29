class Somar:
    def __init__(self, numero):
        self.__numero = numero
    
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, valor):
        if valor is not None and valor != '':
            self.__numero = valor
        else:
            return print("O valor deve ser um número.")
    def somar(self, outro_numero):
        if outro_numero != int and outro_numero != float:
            return print("O valor a ser somado deve ser um número.")
        else:
            return self.__numero + outro_numero
    def __str__(self): 
        return f"Somar: {self.__numero}"