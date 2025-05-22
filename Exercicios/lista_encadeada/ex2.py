class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, valor):
        novo = No(valor)
        novo.proximo = self.topo
        self.topo = novo

    def desempilhar(self):
        if not self.topo:
            return None
        valor = self.topo.valor
        self.topo = self.topo.proximo
        return valor

    def exibir(self):
        atual = self.topo
        elementos = []
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        return elementos

pilha = Pilha()
pilha.empilhar(100)
pilha.empilhar(200)
pilha.empilhar(300)

print("Pilha após empilhamentos:", pilha.exibir())

print("Desempilhado:", pilha.desempilhar())
print("Pilha após desempilhar:", pilha.exibir())
