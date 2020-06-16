'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira. Até a aula 8
'''
from math import trunc
n = float(input('Digite um número real qualquer: '))
print('Aparte inteira do número digitado é {}'.format(trunc(n)))
