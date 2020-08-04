#ATÉ A AULA 13
'''
Desenvolva um programa que leia o nome, idade, e sexo de quatro pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
'''
i = 0
cont = 0
hvelho = 0
hnome = 0
for d in range(1,5):
    print('--------- {}ª Pessoa ---------'.format(d))
    idade = int(input('Digite sua idade: '))
    i += idade
    sexo = str(input('Digite seu sexo como M ou F:')).upper().strip()
    if sexo == 'F':
        if idade < 20:
            cont = cont + 1
    nome = str(input('Digite seu nome: '))
    if (d==1) and (sexo in 'M'):
        hvelho = idade
        hnome = nome
    if sexo in 'M' and idade > hvelho:
        hvelho = idade
        hnome = nome
print('\nA média da idade do grupo foi de {:.0f} anos.'.format(i / 4))
print('Temos {} mulheres com menos de 20 anos!'.format(cont))
print('O homem mais velho é {} com {} anos.'.format(hnome,hvelho))