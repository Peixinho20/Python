#Até a aula 14
'''
Melhore o desafio 61 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disse que quer mostrar 0 termos.
'''
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais # sem essa linha o programa não mostra a PA
    while cont <= total:
        print('{}'.format(termo), end='')
        print(' -> ' if cont < 10 else '  ', end='')
        termo += r
        cont += 1
    print('\nPausa...')
    mais = int(input('\nQuantos termos quer mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))