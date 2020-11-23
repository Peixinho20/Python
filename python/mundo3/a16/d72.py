#ATÉ A AULA 16
'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte. Seu
programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
lista = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número: '))
    if 0 <= numero <= 20:
        break
    print('Esse número não pertence a essa sequencia!', end='')
print(f'Você digitou o número {lista[numero]}') # o valor do input vai ser associado com a sua posição e printado