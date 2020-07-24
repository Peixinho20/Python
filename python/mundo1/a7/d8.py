'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
até a aula 7
'''

n = float(input('Digite uma número: '))
c = n/100
mm = n/1000

print('O valor escolhido em centímetros é \033[4;33;42m{:.3f}\033[m e em milímetros é \033[7;34;43m{:.3f}\033[m.'.format(c,mm))