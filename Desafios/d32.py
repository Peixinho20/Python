'''
ATÉ AULA 10
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
ano = int(input('Digite o ano desejado: '))
if ano%4 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))