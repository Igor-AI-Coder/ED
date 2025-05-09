class Pilha:
    def __init__(self):
        self.__pilha = []
    
    def empilhar(self, item):
        self.__pilha.append(item)
        pass
    
    def desempilhar(self):
        if(self.vazia()):
            return None
        return self.__pilha.pop()
    
    def elemento_topo(self):
        return self.pilha[-1]
    
    def __str__(self):
        return f'Essa é a pilha: {self.__pilha}' 
    
    def vazia(self):
        return len(self.__pilha)== 0

        
