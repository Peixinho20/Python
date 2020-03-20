'''
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno , cosseno e tangente desse angulo. até
aula 8
'''
import math
x = float(input('Digite o valor do angulo: '))
s = math.sin(math.radians(x))
c = math.cos(math.radians(x))
t = math.tan(math.radians(x))
print('O angulo {} tem seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}.'.format(x,s,c,t))