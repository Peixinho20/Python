#ATÉ A AULA 13
'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade (21 anos) e quantas já são maiores.
'''
from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range (1,8):
    nasc = int(input('Quando nasceu a {}ª pessoas: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('{} são maiores de 21 anos!'.format(tmaior))
print('{} são menores de 21 anos!'.format(tmenor))