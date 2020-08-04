#ATÉ A AULA 12
'''
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
print('Retas e Triâgulo!')
a = float(input('Digite o comprimento de uma reta: '))
b = float(input('Digite outro comprimento de reta: '))
c = float(input('Digite mais um comprimento de reta: '))
if a<b+c and b<a+c and c<a+b:
    if a==b and a==c and b==c:
        print('Elas podem formar um triâgulo equilátero!')
    elif a==b or b==c or a==c:
        print('Elas podem formar um triângulo isósceles!')
    elif a!=b and a!=c and b!=c:
        print('Elas podem formar um triângulo escaleno!')
else:
    print('Elas não podem formar um triângulo!')
