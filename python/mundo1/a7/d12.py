'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. até a aula 7
'''
n = float(input('Digite o valor do produto: '))
N = n - (n*5)/100
print('O novo preço do produto é R$ \033[7;33;42m{:.2f}\033[m'.format(N))