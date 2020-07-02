'''
ATÉ A AULA 10
Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0.50 por
km para viagens de até 200km e R$0.45 para viagens mais longas.
'''
dist = float(input('Digite a distancia a ser percorrida em km: '))
if dist < 200:
    print('O preço da passagem será \033[0;30;47mR$ {:.2f}\033[m'.format(dist*0.5))
else:
    print('O valor da passagem será R$ \033[1;31;40m{:.2f}\033[m'.format(dist*0.45))