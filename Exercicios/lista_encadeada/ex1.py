class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor):
        novo = No(valor)
        if not self.cabeca:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def remover(self, valor):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.valor == valor:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def exibir(self):
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        return elementos


lista = Lista()
lista.inserir(10)
lista.inserir(20)
lista.inserir(30)

print("Lista após inserções:", lista.exibir())

lista.remover(20)
print("Lista após remover 20:", lista.exibir())
