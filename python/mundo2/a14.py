#Comando while no python

'''1a)
for c in rage (1,10):
    print(c)
print('Fim')

1b)
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

1a e 1b são iguais na execução

1c)
for c in range(1,5):
    n = int(input('Digite um valor: '))
print('Fim')

1d)
n=1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

1c e 1d são diferentes

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
'''
n=1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # se n for diferente de zero ele não será contabilizado na resposta só pra encerrar o programa
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par,impar))