#Até a aula 14
'''
Crie um programa que leia varios numeros inteiros pelo teclado. No final da execuçao, mostre a media entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer
ou nao continuar a digitar valores.
'''
resp = 'S'
soma = total = media = 0
while resp in 'Ss':
    n = int(input('Digite um valor inteiro: ')) # nessa ordem: 1ª definição da variável n e depois vem suas aplicações
    soma += n
    total += 1
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
media = soma/total # a media dentro do while o programa faria a media individual de cada valor
print('Foram digitados {} números e a soma entre eles é {}.'.format(total, soma))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior,menor))
