class No:
    def __init__(self,dado):
        self.__dado = dado
        self.__esq = None
        self.__dir = None
        
    @property
    def dado(self):
        return self.__dado
    
    @dado.setter
    def dado(self, valor):
        self.__dado = valor
    
    @property
    def esq(self):
        return self.__esq
    
    @esq.setter
    def esq(self, valor):
        self.__esq = valor
    
    @property
    def dir(self):
        return self.__dir
    
    @dir.setter
    def dir(self, valor):
        self.__dir = valor
    
    def pre_ordem(self, no):
        if no == None:
            return
        print(no.dado, end=' ')
        self.pre_ordem(no.esq)
        self.pre_ordem(no.dir)

    def visualizar(self, no, n=0):
        if no == None:
            return
        print('_'*n, no.dado, sep='')
        self.visualizar(no.esq, n+2)
        self.visualizar(no.dir, n+2)
    
    def in_ordem(self, no):
        if no == None:
            return
        self.in_ordem(no.esq)
        print(no.dado, end=' ')
        self.in_ordem(no.dir)
    
    def pos_ordem(self, no):
        if no == None:
            return
        self.pos_ordem(no.esq)
        self.pos_ordem(no.dir)
        print(no.dado, end=' ')


class Arv_Bin:
    def __init__(self):
        self.__raiz = None
    
    @property
    def raiz(self):
        return self.__raiz
    
    def vazia(self):
        return self.__raiz == None
    
    def ins_raiz(self, valor):
        no = No(valor)
        self.__raiz = no
    
    def buscar(self, no, valor):
        if no == None:
            return None
        if no.dado == valor:
            return no
        achou = self.buscar (no.esq, valor)
        if not achou:
            achou = self.buscar(no.dir, valor)
        return achou
    
    def esvaziar(self):
        self.__raiz = None
    
    def ins_esq(self, pai, filho):
        no_pai = self.buscar(self.__raiz, pai)
        if no_pai == None:
            return False #pai não encontrado
        if no_pai.esq != None:
            return False #já existe filho à esquerda
        no_filho = No(filho)
        no_pai.esq = no_filho
        return True
    
    def ins_dir(self, pai, filho):
        no_pai = self.buscar(self.__raiz, pai)
        if no_pai == None:
            return False #pai não encontrado
        if no_pai.dir != None:
            return False #já existe filho à direita
        no_filho = No(filho)
        no_pai.dir = no_filho
        return True

# Exemplo de uso da classe No e Arv_Bin
a = No('A')
b = No('B')
c = No('C')
d = No('D')
e = No('E')
f = No('F')
g = No('G')
a.esq = b
a.dir = c
b.esq = d
b.dir = e
c.esq = f
c.dir = g

a.pre_ordem(a)
a.visualizar(a)

t = Arv_Bin()
t.ins_raiz('A')
t.ins_esq('A', 'B')
t.ins_dir('A', 'C')
t.ins_esq('B', 'D')
t.ins_dir('B', 'E')
t.ins_esq('C', 'F')
t.ins_dir('C', 'G')
t.visualizar(t.raiz)
t.pre_ordem(t.raiz)
t.in_ordem(t.raiz)
t.pos_ordem(t.raiz)