'''
Faça um programa que leia o nome completo de um pessoas, mostrando em seguida o primeiro e o último nome separadamente
Ex: Ana Maria de Souza
primeiro: Ana
último: Souza
'''
nome = str(input('Digite seu nome completo: ')).split()
print('Primeiro nome: \033[7;37;46m{}\033[m'.format(nome[0]))
print('Último nome: \033[0;30;47m{}\033[m'.format(nome[-1]))
