class No:
    def __init__(self, valor):
        self.__valor = valor
        self.__prox = None
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self, prox):
        self.__prox = prox

class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
    def empilhar(self, valor):
        novo_no = No(valor)
        novo_no.prox = self.topo
        self.__topo = novo_no
        self.__tamanho += 1
    def desempilhar(self):
        if self.__topo is None:
            raise IndexError("Pilha vazia")
        valor = self.__topo.valor
        self.__topo = self.__topo.prox
        self.__tamanho -= 1
        return valor
    def topo(self):
        if self.__topo is None:
            raise IndexError("Pilha vazia")
        return self.__topo.valor
    def vazia(self):
        return self.__topo is None
    def tamanho(self):
        return self.__tamanho
    def __str__(self):  
        if self.vazia():
            return "Pilha vazia"
        valores = []
        atual = self.__topo
        while atual:
            valores.append(str(atual.valor))
            atual = atual.prox
        return " -> ".join(valores)