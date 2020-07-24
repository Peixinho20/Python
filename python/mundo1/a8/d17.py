'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule  e
mostre o comprimento da hipotenusa.
'''
from math import hypot
x = float(input('Digite o comprimento do cateto oposto: '))
y = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é \033[1;31;40m{:.2f}\033[m'.format(hypot(x,y)))
