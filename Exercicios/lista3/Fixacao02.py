class Aluno:
    def __init__(self, matricula, nome, notas=[]):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas
    @property
    def matricula(self):
        return str(self.__matricula)
    @property
    def nome(self):
        return self.__nome
    @property
    def notas(self):
        return self.__notas
    @nome.setter
    def novo_nome(self, nnome):
        self.__nome = nnome
    def media(self):
        return sum(self.__notas) / len(self.__notas) 
    def adicionar(self, nota):
        self.__notas.append(nota)
    def __str__(self):
        return f'O nome do aluno é {self.__nome}, sua matrícula é {self.__matricula}, suas notas são {self.__notas} e sua média é de {self.media():.1f}'

aluno = Aluno(20242370041, 'Igor')
aluno.adicionar(80)
aluno.adicionar(90)
aluno.adicionar(40)
print (aluno)