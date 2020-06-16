'''
ATÉ A AULA 10
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.
'''
a = float(input('Digite o comprimento de uma reta: '))
b = float(input('Digite outro comprimento de reta: '))
c = float(input('Digite mais um comprimento de reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Elas podem formar um triângulo!')
else:
    print('Elas não podem formar uma reta!')