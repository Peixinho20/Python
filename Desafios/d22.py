'''
Crie um programa que leia o nome completo de uma pessoas e mostre:

O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome
Até a aula 9
'''
nome = str(input('Digite seu nome completo: ')).strip() #retira espaços inuteis antes e depois da frase
print('Analisando seu nome... ')
print('Seu nome em maiúscula é {}.'.format(nome.upper()))
print('Seu nome em minúscula é {}.'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))
'''
para a última pergunta: 
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
'''
