'''
Cire um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
Até a aula 9
'''
cidade = str(input('\033[1;31;40mDigite a cidade em que você nasceu: \033[m')).capitalize().split()
print(cidade[0].endswith('Santo')) #diz se tem ou não o item procurado no item 0
