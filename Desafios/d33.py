'''
ATÉ A AULA 10
Faça um prgrama que leia três números e mostre qual é o maior e qual é o menor.
'''
a = int(input('Digite um número:'))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
if a > b > c:
    print('O valor \033[0;34;43m{}\033[m é o maior e o \033[1;35;44m{}\033[m é o menor!'.format(a,c))
elif a > c > b:
    print('O valor \033[4;36;45m{}\033[m é o maior e o \033[7;37;46m{}\033[m é o menor!'.format(a,b))
elif b > a > c:
    print('O valor \033[0;30;47m{}\033[m é o maior e o \033[1;31;40m{}\033[m é o menor!'.format(b,c))
elif b > c > a:
    print('O valor \033[4;32;41m{}\033[m é o maior e o \033[7;33;42m{}\033[m é o menor!'.format(b,a))
elif c > a > b:
    print('O valor \033[0;34;43m{}\033[m é o maior e o \033[1;35;44m{}\033[m é o menor!'.format(c,b))
elif c > b > a:
    print('O valor \033[4;36;45m{}\033[m é o maior e o \033[7;37;46m{}\033[m é o menor!'.format(c,a))