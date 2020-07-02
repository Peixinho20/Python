'''
ATÉ A AULA 10
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
'''
n = int(input('Digite um número inteiro: '))
if n%2 == 0:
    print('O número \033[4;36;45m{}\033[m é par'.format(n))
else:
    print('O número \033[7;37;46m{}\033[m é ímpar!'.format(n))