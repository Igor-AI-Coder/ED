class No:
    def __init__(self, dado, prox=None):
        self.__dado = dado
        self.__prox = prox
    
    @property
    def dado(self):
        return self.__dado
    
    @dado.setter
    def dado (self,dado):
        self.__dado = dado
    
    @property
    def prox(self):
        return self.__prox
    
    @prox.setter
    def prox(self, prox):
        self.__prox = prox

class Lista:
    def __init__(self):
        self.__inicio = None
    
    def vazia(self):
        return self.__inicio == None
    
    def tamanho(self):
        cont = 0
        #O p é o ponteiro do próximo
        p = self.__inicio
        while p != None:
            cont += 1
            p = p.prox
        return cont
    
    def inserir_inicio(self, dado):
        novo = No(dado)
        novo.prox = self.__inicio
        self.__inicio = novo
    
    def inserir_final(self,dado):
        novo = No(dado)
        if self.vazia():
            self.__inicio = novo
        else:
            p = self.__inicio
            while p.prox != None:
                p = p.prox
        p.prox = novo
    
    def inserir_posição(self,dado, pos):
        if self.tamanho() < pos:
            print('Essa posição não existe')
            return
        if pos == 0:
            self.inserir_inicio(dado)
        novo = No(dado)
        # a sendo anterior, i sendo o index
        a = None
        p = self.__inicio
        i = 0
        while i < pos:
            a = p
            p = p.prox
            i += 1
        a.prox = novo
        novo.prox = p

    def buscar(self, dado): 
        p = self.__inicio
        pos = 0
        while p is not None:
            if p.dado == dado:
                return pos
            p = p.prox
            pos += 1
        return -1  # Retorna -1 se o dado não for encontrado na lista
    def remover(self, dado):
        if self.vazia() == True:
            print ('Não há itens na lista')
            return
        anterior = None
        p = self.__inicio
        while p is not None:
            if p.dado == dado:
                if anterior is None:
                    self.__inicio = p.prox
                else:
                    anterior.prox = p.prox
                return
            anterior = p
            p = p.prox
        print('O dado não foi encontrado na lista')
        
    def imprimir(self):
        p = self.__inicio
        while p != None:
            print(p.dado,end=' ')
            p = p.prox
        print()
    