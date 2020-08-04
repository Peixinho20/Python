#ATÉ A AULA 12
'''
Faça um programa que leia o ano de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
nome = str(input('Insira seu nome: '))
idade = int(input('Insira sua idade:'))
if idade == 18:
    print('{} é a hora de se alistar!'.format(nome))
elif idade < 18:
    c = (18 - idade)
    print('{} deve se alistar daqui a {} ano(s).'.format(nome,c))
elif idade > 18:
    a = (idade - 18)
    print('{} deveria ter se alistado há {} anos.'.format(nome,a))