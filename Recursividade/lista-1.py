class No:
    def __init__(self, dado):
        self.__dado = dado
        self.__proximo = None
    @property
    def proximo(self):
        return self.__proximo
    @proximo.setter
    def proximo(self, valor):
        self.__proximo = valor
    @property
    def dado(self):
        return self.__dado
    @dado.setter
    def dado(self, valor):
        self.__dado = valor
    
def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n - 1)
def imprimir(L):
    if L == None:
        return
    print(L.dado)
    imprimir(L.proximo)
    return L

def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n -1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def somar(lista):
    if lista == []:
        return 0
    ult = lista.pop()
    return somar(lista) + ult

n=fat(5)
print(n)
m = potencia(4,2)
print(m)
print(fib(2))
print(somar([1,2,3,4,5]))

