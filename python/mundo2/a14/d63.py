#Até a aula 14
'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros termos de uma
sequencia de Fibonacci.
ex 0,1,1,2,3,5,8
'''
a = 0
b = 1
n = int(input('Digite um número: '))
n = (n-1) + (n-2)
while n > 0:
    print('{} -> {}'.format(a,b))
    print(' -> {}'.format(n))
    n += 1



