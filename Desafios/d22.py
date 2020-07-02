'''
Até a aula 9
Crie um programa que leia o nome completo de uma pessoas e mostre:

O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome
Até a aula 9
'''
nome = str(input('Digite seu nome completo: ')).strip() #retira espaços inuteis antes e depois da frase
print('\033[1;31;40mAnalisando seu nome...\033[m ')
print('Seu nome em maiúscula é \033[4;36;45m{}\033[m.'.format(nome.upper()))
print('Seu nome em minúscula é \033[7;37;46m{}\033[m.'.format(nome.lower()))
print('Seu nome ao todo tem \033[0;30;47m{}\033[m letras.'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome tem \033[4;32;41m{}\033[m letras'.format(len(dividido[0])))
# o argumento do divido é a
'''
para a última pergunta: 
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
'''
