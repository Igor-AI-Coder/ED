from Carro import Carro
from Dimensao import Dimensao
from Motor import Motor

dimensao = Dimensao(1.67,1.81,4.37)
motor = Motor('1.6','gasolina')
carro = Carro('azul', 'ABC1D23', dimensao, motor)
print(carro)
print(f'\nMOTOR ATUAL: {carro.motor.motorizacao}')
carro.motor.motorizacao = '2.0'
print(f'\nNOVO MOTOR: {carro.motor.motorizacao}')