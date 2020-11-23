
#ATÉ A AULA 16
'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os numa tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.
'''

valores = (int(input('Digite um inteiro: ')),int(input('Digite outro inteiro: ')),
           int(input('Digite mais um inteiro: ')),int(input('Digite o último inteiro: ')))
print('-='*20)
print(f'Você digitou os valores {valores}')
print('-='*20)
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
print('-='*20)
if 3 in valores:
    print(f'O valor 3 apareceu na posição {valores.index(3)+1}')
else:
    print('O valor 3 não foi digitado!')
print('-='*20)
print('O valores pares digitados foram: ', end='')
for n in valores:
    if n%2 == 0:
        print(n, end=' ')

