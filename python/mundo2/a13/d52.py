#ATÉ A AULA 13
'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um número: '))
print('Verificando o número {}...'.format(num))
tot = 0
for c in range(1,num+1):
    if num%c==0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes!'.format(num,tot))
if tot == 2:
    print('Por isso o número {} é primo!'.format(num))
else:
    print('Por isso o número {} não é primo!'.format(num))

