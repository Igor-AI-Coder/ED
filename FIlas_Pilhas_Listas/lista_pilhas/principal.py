from ex1 import Pilha
p1 = Pilha()

while True:
    opcao = input('''
        1-Empilhar
        2-Desempilhar
        3-Elemento do Topo
        4-Exibir a pilha
        5-Tamanho da pilha   
        6-Esvaziar
        7-Sair
    ''')
    if opcao == "1":
        valor = input("Digite o valor a ser adicionado: ")
        p1.empilhar(valor)
    elif opcao == "2":
        p1.desempilhar()
    elif opcao == "3":
        p1.elemento_topo()
    elif opcao == "4":
        print(p1)
    elif opcao == "5":
        cont = 0
        p2 = Pilha()
        while True:
            if p1.desempilhar():
                p2.empilhar(p1.desempilhar())
                cont += 1
            else:
                break
        while True:
            if p2.desempilhar():
                p1.empilhar(p2.desempilhar())
            else:
                break
        print(f'O tamanho é de:{cont} elementos')
    elif opcao == "6":
        p1.vazia()
    else:
        print('Saindo do programa')
        break