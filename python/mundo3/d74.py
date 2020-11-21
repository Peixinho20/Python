#ATÉ A AULA 16
''''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla
'''
from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))# sorteia cinco numeros em forma de tupla
print('Os valores sorteados foram: ', end='') # o end='' aqui faz o outro print ficar na mesma linha desse print
for n in numeros: # mostra todos os numeros n printados no sorteio
    print(f'{n} ', end='')# o espaço depois do {n} separa os numeros no print
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

