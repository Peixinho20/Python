#ATÉ A AULA 13
'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
Ex: apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''
frase = str(input('Digite uam frase: ')).strip().upper() # pede uma frase
palavras = frase.split() # separa a frase numa lista de palavras
junto =''.join(palavras) # juntas as letras da frase novamente
inverso = '' # começa do início e vai até o fim de tràs pra frente
for letra in range(len(junto)-1,-1,-1):# vai começar na penúltima letra da frase, vai até a posição -1 que é antes
# primeira nesse caso posição zero, de trás pra frente
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')

#outra forma de fazer
'''
frase = str(input('Digite uam frase: ')).strip().upper() # pede uma frase
palavras = frase.split() # separa a frase numa lista de palavras
junto =''.join(palavras) # juntas as letras da frase novamente
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
'''