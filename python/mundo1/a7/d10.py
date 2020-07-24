'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar. até a aula 7
'''
n = float(input('Quanto dinheiro vc tem carteira? '))
d = n/5
print('A quantidade em dólares é U$ \033[0;30;47m{}\033[m.'.format(d))