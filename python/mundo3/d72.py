#ATÉ A AULA 16
'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte. Seu
programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
lista = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número: '))
for i in lista:
    if numero == 0:
        print(lista[0])
    elif numero == 1:
        print(lista[1])
    elif numero == 2:
        print(lista[2])
    elif numero == 3:
        print(lista[3])
    elif numero == 4:
        print(lista[4])
    elif numero == 5:
        print(lista[5])
    elif numero == 6:
        print(lista[6])
    elif numero == 7:
        print(lista[7])
    elif numero == 8:
        print(lista[8])
    elif numero == 9:
        print(lista[9])
    elif numero == 10:
        print(lista[10])
    elif numero == 11:
        print(lista[11])
    elif numero == 12:
        print(lista[12])
    elif numero == 13:
        print(lista[13])
    elif numero == 14:
        print(lista[14])
    elif numero == 15:
        print(lista[15])
    elif numero == 16:
        print(lista[16])
    elif numero == 17:
        print(lista[17])
    elif numero == 18:
        print(lista[18])
    elif numero == 19:
        print(lista[19])
    elif numero == 20:
        print(lista[20])
    else:
        print('Esse número não pertence a essa sequencia!')
    numero = int(input('Digite um número: '))