#ATÉ A AULA 13
'''
Faça um programa que moestre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles. explorar bibliotecas
'''
from time import sleep
print('A contagem para os fógos começam em:')
for c in range(10,-1,-1):
    sleep(1)
    print(c)