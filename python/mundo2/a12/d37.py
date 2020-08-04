#ATÉ A AULA 12
'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
pesquisar bases numéricas
'''

num = int(input('Digite um número: '))
print('Digite um número para conversão:\n 1 para binário\n 2 para octal\n 3 para hexadecimal ')
escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    print('{} convertido para binário é {}.'.format(num,bin(num)[2:]))
    # fatiamento do número: imprime o número da posição 2 em diante
elif escolha == 2:
    print('{} conertido para octal é {}.'.format(num,oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é {}.'.format(num,hex(num)[2:]))
else:
    print('Escolha inválida. Tente novamente.')
