class Deque:
    def __init__(self):
        self.__deque = []
    
    def vazia(self):
        return len(self.__deque) == 0
    