class Retangulo ():
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base
    
    def calcArea (self):
        area = self.base * self.altura
        return area
    
    def Equadrado(self):
        if self.base == self.altura:
            return "É quadrado"
        else:
            return "Não é quadrado"

ret1 = Retangulo(3,6)
ret2 = Retangulo(10,10)
print(f'Dimensões do retangulo 1: {ret1.altura}, {ret1.base}')
print(f'Dimensões do retangulo 2: {ret2.altura}, {ret2.base}')
print(f'Área do retangulo 1: {ret1.calcArea()}')
print(f'Área do retangulo 2: {ret2.calcArea()}')
print(f'{ret1.Equadrado()}')
print(f'{ret2.Equadrado()}')