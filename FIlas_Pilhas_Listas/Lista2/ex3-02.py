class Disciplina:
    def __init__(self, nome, carga_horaria):
        self.__nome = nome
        self.__carga_horaria = carga_horaria
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome (self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    @carga_horaria.setter
    def carga_horaria(self, nova_ch):
        self.__carga_horaria = nova_ch
    def __str__(self):
        return f'{self.__nome}({self.__carga_horaria}h)'
    
    
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


disciplina = Disciplina('Estrutura de Dados', 67)
print(disciplina)