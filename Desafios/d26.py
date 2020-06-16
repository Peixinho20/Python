'''
Crie um programa que leia uma frase pelo teclado e mostre:

quantas vezes aparece a letra 'a'
em que posição ela aparece a primeira vez.
em que posição ela aparece pela ultima vez.
'''
nome = str(input('Digite seu nome: ')).strip()
print('A letra a aparece {} vezes'.format(nome.count('a')))
print('A letra a aparece pela primeira vez na posição {}'.format(nome.find('a')))
print('A letra a aparece pela última vez na posição {}'.format(nome.rfind('a')))
#print('A letra a aparece pela última vez na posição {}'.format(nome.casefold())) #substitui a palavra do input na {}
#print('A letra a aparece pela última vez na posição {}'.format(nome.endswith('a'))) #diz se tem ou não o item procurado
#print('A letra a aparece pela última vez na posição {}'.format(nome.expandtabs('a'))) #requer um número inteiro
#print('A letra a aparece pela última vez na posição {}'.format(nome.format_map('a'))) #substitui a palavra do input na {}
#print('A letra a aparece pela última vez na posição {}'.format(nome.index('a')))#mostra a primeira vez que o argumento aparece
#print('A letra a aparece pela última vez na posição {}'.format(nome.zfill('a')))# pede como argumento um inteiro
#print('A letra a aparece pela última vez na posição {}'.format(nome.isidentifier()))#não precisa de argumento, só lê string

