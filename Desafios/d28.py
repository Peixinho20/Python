'''
ATÉ A AULA 10
Escreva um programa que faça o computador pensar em um número entre 0 e 5 e peça para o usário tentar descobrir qual
foi o número escolhido pelo computador. O programa deverá escrever na tela se o usário venceu ou não.
'''
import random
n = int(input('Digite um número inteiro de 0 a 5: '))
x = random.randint(0,5)
if x == n:
    print('Parabeńs, você e o computador pensaram no mesmo número!')
else:
    print('Sinto muito, o número do computador é {}!'.format(x))