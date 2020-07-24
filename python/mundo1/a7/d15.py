'''
Escreva um programa que pergunte a quantidade de km percorridos por uma carro alugado e quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''

x = float(input('Digite a quantidade de km percorridos pelo carro: '))
y = float(input('Digite a quantidade de dias que o carro ficou alugado: '))
t = (x*0.15)+(y*60)
print('O total a ser pago é R$\033[7;37;46m{:.2f}\033[m.'.format(t))