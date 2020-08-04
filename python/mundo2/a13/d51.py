#ATÉ A AULA 13
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.
'''
#an = a1 + (n - 1)r
a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
a10 = a1 +(10 - 1)*r
for c in range(a1,a10 + r,r):
    print(c)