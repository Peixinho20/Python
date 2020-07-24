'''
Crie uma algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
até a aula 7
'''

n = float(input('Digite um número: '))
a = n*2
b = n*3
c = n**(1/2)
print('O seu dobro é \033[4;37;46m{}\033[m, o seu triplo é \033[7;30;46m{}\033[m e a sua raiz quadrada é \033[0;31;40m{:.3f}\033[m'. format(a,b,c))