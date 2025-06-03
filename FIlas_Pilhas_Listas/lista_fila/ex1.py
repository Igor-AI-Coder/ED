class Fila:
    def __init__(self):
        self.__fila = []

    def vazia (self):
        return len(self.__fila) == 0
    
    def enfileirar(self, fila):
        self.__fila.append(fila)
    def remover(self):
        if not self.vazia():
            return self.__fila.pop(0)
        return None
    def primeiro(self):
        if not self.vazia():
            return self.__fila[0]
        return None
    def tamanho(self):
        return len(self.__fila)
    def __str__(self):
        return str(self.__fila)
    
f = Fila()
print(f)
f.enfileirar(1)
print(f)
f.enfileirar(2)
print(f)
f.enfileirar(3)
print(f)
print(f.primeiro())
print(f.remover())
print(f)