'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um doa dígitos separados
Ex:
Digite um número: 1834
unidades: 4
dezenas: 3
centenas: 8
milhar: 1
#ATÉ A AULA 9
'''
n = str(input('Insira um número entre 0 e 9999: '))
print('A analisando seu número... ')
print('O primeiro algarismo tem {} unidades'.format(n[3]))
print('O segundo algarismo tem {} dezenas'.format(n[2]))
print('O terceiro algarismo tem {} centenas'.format(n[1]))
print('O quarto algarismo tem {} milhar'.format(n[0]))
