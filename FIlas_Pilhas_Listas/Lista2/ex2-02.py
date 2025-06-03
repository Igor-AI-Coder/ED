class Aluno:
    def __init__(self, nome, disciplina):
        self.__nome = nome
        self.__disciplina = disciplina
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome (self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def disciplina(self):
        return self.__disciplina
    @disciplina.setter
    def disciplina(self, nova_disciplina):
        self.__disciplina = nova_disciplina
