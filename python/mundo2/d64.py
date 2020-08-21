#ATÉ AULA 14
'''
Crie uma programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números fora digitados e qual foi a soma entre
eles (desconsiderando flag)
'''
soma = total = n = 0
n = int(input('Digite um inteiro de 0 a 999 [Digite 999 para sair do programa]: '))
while n != 999:
    total += 1
    soma += n
    n = int(input('Digite um inteiro de 0 a 999: '))
print('Foram digitados {} números e a soma deles é {}.'.format(total, soma))
# colocando o input dentro e fora do while a fariável soma não soma o 999, então o 999 só servirá para sair do programa