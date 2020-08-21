#Até a aula 14
'''
Melhore o jogo do Desafio 28 onde o computador vai pensar em núemro entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
computador = randint(0,5)
palpites = 0
acertou = False
print('Vamos brincar de advinhação! Pensei num número de 0 a 5, tente adivinhar!')
while not acertou:
    jogador = int(input('Digite um número de 0 a 5: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente mais uma vez')
        elif jogador < computador:
            print('Mais... Tente mais uma vez')
print('Você acertou depois de {} tentativas! Parabéns!'.format(palpites))