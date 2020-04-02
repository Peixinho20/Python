'''
Crie um programa que leia o nome da uma pessoa e diga se ela tem 'Silva' no nome. #ATÉ A AULA 9
'''
nome = str(input('Digite seu nome completo: ')).lower().strip()
print('Você tem Silva no nome? {} '.format('silva' in nome))
