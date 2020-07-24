'''
Faça um programa que leia um número e mostre na tela o seu sucessor se antecessor.
até a aula 7
'''

n = float(input('Digite um número: '))
a = n+1
b = n-1
print('O sucessor dele é \033[7;36;45m{}\033[m e o antecessor dele é \033[1;37;46m{}\033[m.'.format(a,b))