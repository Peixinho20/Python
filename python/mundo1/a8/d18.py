'''
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno , cosseno e tangente desse angulo. até
aula 8
'''
import math
x = float(input('Digite o valor do angulo: '))
s = math.sin(math.radians(x))
c = math.cos(math.radians(x))
t = math.tan(math.radians(x))
print('O angulo \033[4;32;41m{}\033[m tem seno igual a \033[7;33;42m{:.2f}\033[m, cosseno igual a {:.2f} e tangente '
      'igual a \033[0;34;43m{:.2f}\033[m.'.format(x,s,c,t))