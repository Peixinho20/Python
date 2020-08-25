#Até a aula 14
'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
       = (5-0)x(5-1)
Tentar fazer com for e com while


from math import factorial
n = int(input('Digite um número: '))
print(factorial(n))
'''

#Outro modo

'''
n = int(input('Digite um número: '))
cont = n #vai contando até que cont seja igual a n
f = 1 # f começa com 1 pq 1 é o elemento neutro da multiplicação
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='') # faz aparecer a igualdade quando a contagem chegar no 1
    f *= cont
    cont -=1 # faz a contagem de trás pra frente
print('{}'.format(f))
'''