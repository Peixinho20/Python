'''
Faça um programa que leia o nome completo de um pessoas, mostrando em seguida o primeiro e o último nome separadamente
Ex: Ana Maria de Souza
primeiro: Ana
último: Souza
#ATÉ A AULA 9
'''
nome = str(input('Digite seu nome completo: ')).split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[-1]))
