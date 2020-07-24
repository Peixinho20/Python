'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
até a aula 7
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A média é \033[1;32;41m{:.2f}\033[m!'.format(m))