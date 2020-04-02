'''
Cire um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
'''
cidade = str(input('Digite a cidade em que você nasceu: ')).capitalize().split()
print(cidade[0].endswith('Santo')) #diz se tem ou não o item procurado no item 0
