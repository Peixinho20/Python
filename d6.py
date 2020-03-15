'''
Crie uma algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
até a aula 7
'''

n = float(input('Digite um número: '))
a = n*2
b = n*3
c = n**(1/2)
print('O seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {:.3f}'. format(a,b,c))