'''
ATÉ AULA 10
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
ano = int(input('Digite o ano desejado: '))
if ano%4 == 0:
    print('O ano \033[4;32;41m{}\033[m é bissexto.'.format(ano))
else:
    print('O ano \033[7;33;42m{}\033[m não é bissexto.'.format(ano))