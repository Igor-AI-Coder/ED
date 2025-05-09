class Aluno:
    def __init__(self,mat,nome,curso):
        self.mat = mat
        self.nome = nome
        self.curso = curso
    def falar(self):
        print(f'Olá, sou {self.nome} estou de calcinha, e faço {self.curso}')

aluno = Aluno(123,'Ian ', 'TSI')
aluno.falar()