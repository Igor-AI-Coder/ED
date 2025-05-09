class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = 0.00
    @property
    def numero (self):
        return self.__numero
    @numero.setter
    def numero(self,numero):
        self.__numero = numero
    
    def get_agencia(self):
        return self._agencia
    def get_saldo (self):
        return self._saldo
    def set_agencia(self, agencia):
        self._agencia = agencia
    def set_saldo(self, saldo):
        self._saldo = saldo
    def sacar(self,valor):
        self.__saldo -= valor
    def depositar(self,valor):
        self.__saldo += valor
    def __str__(self):
        return f'{conta.__numero}, Saldo: R${conta.saldo: .2f}'
    conta = Conta(1)
    print (conta)
    conta.depositar(500)
    conta.sacar()
    print (conta)
    print(conta.numero)
    conta.numero = 2
    print(conta)