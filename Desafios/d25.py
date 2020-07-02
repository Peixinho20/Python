'''
Crie um programa que leia o nome da uma pessoa e diga se ela tem 'Silva' no nome.
'''
nome = str(input('\033[4;32;41mDigite seu nome completo: \033[m')).lower().strip()
print('Você tem Silva no nome? \033[7;33;42m{}\033[m '.format('silva' in nome))