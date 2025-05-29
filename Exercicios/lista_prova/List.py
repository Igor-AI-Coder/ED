class Lista:
    def __init__(self):
        self.__lista = []
    
    def inserir(self,valor):
        self.__lista.append(valor)
    def remover(self, valor):
        if valor in self.__lista:
            self.__litas.remove(valor)
        else:
            print(f"Valor {valor} não encontrado na lista.")
    def remover(self, pos):
        if 0 <= pos <len(self.__lista):
             self.__lista.pop(pos)
        else:
            print(f"Posição {pos} inválida. A lista tem {len(self.__lista)} elementos.")
    def vazia(self):
        return len(self.__lista) == 0
    def tamanho(self):
        return len(self.__lista)
    def buscar(self, valor):
        if self.vazia():
            return -1
        if valor in self.__lista:
            return self.__lista.index(valor)
        else:
            return -1
    def __str__(self):
        if self.vazia():
            return "Lista vazia"
        return " -> ".join(str(x) for x in self.__lista)