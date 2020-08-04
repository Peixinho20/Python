#ATÉ A AULA 13
'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
'''
s = 0
print('Será pedido seis valores inteiros!')
for c in range(0,6):
    n = int(input('Digite um valor: '))
    if n%2==0:
        s += n
print('A soma dos números pares é {}.'.format(s))