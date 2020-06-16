'''
ATÉ A AULA 10
Faça um prgrama que leia três números e mostre qual é o maior e qual é o menor.
'''
a = int(input('Digite um número:'))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
if a > b > c:
    print('O valor {} é o maior e o {} é o menor!'.format(a,c))
elif a > c > b:
    print('O valor {} é o maior e o {} é o menor!'.format(a,b))
elif b > a > c:
    print('O valor {} é o maior e o {} é o menor!'.format(b,c))
elif b > c > a:
    print('O valor {} é o maior e o {} é o menor!'.format(b,a))
elif c > a > b:
    print('O valor {} é o maior e o {} é o menor!'.format(c,b))
elif c > b > a:
    print('O valor {} é o maior e o {} é o menor!'.format(c,a))