'''
ATÉ A AULA 10
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$ 7.00 por cada km acima do limite.
'''

v = float(input('Digite a sua velocidade do carro em km/h: '))
if v > 80:
    d = (v - 80)*7
    print('Limite de velocidade ultrapaçado! Você será multado em R${}'.format(d))
else:
    print('Você está dentro do limite!')
print('Tenha um bom dia!')