'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira. Até a aula 8
'''
from math import trunc  # essa função mostra só a parte inetira de um número decimal
n = float(input('Digite um número real qualquer: '))
print('Aparte inteira do número digitado é \033[0;30;47m{}\033[m'.format(trunc(n)))