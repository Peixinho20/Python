'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
até a aula 7
'''

n = float(input('Digite uma número: '))
c = n/100
mm = n/1000

print('O valor escolhido em centímetros é {:.3f} e em milímetros é {:.3f}.'.format(c,mm))