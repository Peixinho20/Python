#Até a aula 14
'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Digite seu sexo com M ou F: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Voce digitou errado! Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))