#ATÉ A AULA 13
'''
Refaça o desafio 09, mostrando  tabuada de um número que o usuário escolhaer, só que agora utilizando um laço for.
'''
from time import sleep
n = int(input('Digite um número inteiro: '))
print('A tabuada do número {} é:'.format(n))
sleep(1)
for c in range(0,11):
    x = n*c
    print('{} * {} = {}'.format(n,c,x))