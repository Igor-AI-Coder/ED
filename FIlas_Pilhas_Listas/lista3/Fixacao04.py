class Conta:
    def __init__(self, numero, saldo, nome):
        self.__numero = numero
        self.__saldo = saldo
        self.__nome = nome
    @property
    def numero(self):
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo
    @property
    def nome(self):
        return self.__nome
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False

contas = []
print('Informe os dados da conta, por favor (para encerrar, digite 0 no número da conta).')
while True:
    numero = int(input('\nNúmero da conta: '))
    if numero == 0:
        break
    nome_titular = input('Nome do titular: ')
    conta = Conta(numero, nome_titular)
    contas.append(conta)
while True:
    print('\nOPERAÇÕES:')
    print('[1] Depositar')
    print('[2] Sacar')
    print('[3] Saldo')
    print('[4] Sair')
    opcao = int(input('Opção: '))
    if opcao == 1:
        numero = int(input('Número da conta: '))
        for conta in contas:
            if conta.numero == numero:
                valor = float(input('Valor a ser depositado: R$ '))
                conta.depositar(valor)
                print('Depósito realizado com sucesso!')
                break
        else:
            print('Conta não encontrada.')
    if opcao == 2:
        numero = int(input('Número da conta: '))
        for conta in contas:
            if conta.numero == numero:
                valor = float(input('Valor a sacado: R$ '))
                if conta.sacar(valor):
                    print('Saque realizado!')
                else:
                    print('Saldo insuficiente!')
                break
        else:
            print('Conta não encontrada!')
    elif opcao == 3:
        numero = int(input('Número da conta: '))
        for conta in contas:
            if conta.numero == numero:
                print(f'Saldo: R$ {conta.saldo:.2f}')
                break
        else:
            print('Conta não encontrada!')
    elif opcao == 4:
        break
    else:
        print('Opção inválida!')
print('Fim do programa!')