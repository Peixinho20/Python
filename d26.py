'''
Crie um programa que leia uma frase pelo teclado e mostre:

quantas vezes aparece a letra 'A'
em que posição ela aparece a primeira vez.
em que posição ela aparece pela ultima vez.
'''
nome = str(input('Digite seu nome: ')).strip()
print('A letra a aparece {} vezes'.format(nome.count('a')))
print('A letra a aparece pela primeira vez na posição {}'.format(nome.find('a')))
print('A letra a aparece pela última vez na posição {}'.format(nome.rfind('a')))
