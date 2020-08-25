#Até a aula 14
'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrandos os 10 primeiros termos da
progressão usando a estrutura while.
'''
print('Gerador de P.A.')
print('-='*17)
a1 = int(input('Digite o primeiro termo P.A.: '))
r = int(input('Digite a razão da P.A.:'))
termo = a1
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='') #até aqui o programa imprime somente o primeiro termo infinitamente
    print(' -> ' if cont < 10 else ' Fim ', end='')
    termo += r # aqui o programa soma o termo com a razão e imprime infinitamente
    cont +=1 # aqui o programa concretiza o comando while e imprime somente os 10 termos pedido
