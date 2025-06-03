from ex1 import No
n1 = No('D')
n1.prox = No('E')
n1.prox.prox = No('F')
n1.prox.prox.prox = No('G')
n1.prox.prox.prox.prox = No('H')

noEF = No('EF')
noEF.prox = n1.prox.prox

q = n1
while (q != None):
    print(q.dado)
    q = q.prox  