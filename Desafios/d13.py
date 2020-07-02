'''
Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com 15% de aumento. até a aula 7
'''
n = float(input('Digite o salário do funcionário: '))
N = n + (n*15)/100
print('O novo salário do funcionário é R$ \033[0;34;43m{:.2f}\033[m'.format(N))