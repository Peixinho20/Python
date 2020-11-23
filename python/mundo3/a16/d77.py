'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar
para cada palavra quais são as suas vogais.
'''

frase = ('Preciso', 'passar', 'em', 'algebra', 'fundamentos', 'e', 'fisica')
# o primeiro for analisa as palavras da frase
for palavra in frase: #printar palavra me da as posições e printar frase me dá a frase para cada posição
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    # esse for analisa as letras em  cada palavra
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')