#ATÉ A AULA 13
'''
Faça um programa que calcule a soma entre todos o números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

s = 0
cont = 0
print('\nA soma de todos os números ímpares entre 1 e 500 múltiplos de três é:')
for c in range (1,501,2):
    if c%3==0:
        cont = cont + 1
        s += c
print('A soma dos {} valores solicitados é {}'.format(cont,s))