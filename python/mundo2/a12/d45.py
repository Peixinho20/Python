#ATÉ A AULA 12
'''
Crie um programa que faça o computador jogar Jokepô (pedra, papel e tesoura) com vc.
'''
import random
print('Vamos brincar de Jokepô (pedra, papel e tesoura)!')
print('Digite:'
      '\n[1] para papel'
      '\n[2] para tesoura'
      '\n[3] para pedra')
escolha = int(input('Digite sua escolha: '))
x = random.randint(1,3)
if escolha == x == 1:
      print('Empate! Você e o computador pensaram em papel.')
elif escolha == x == 2:
      print('Empate! Você e o computador pensaram em tesoura')
elif escolha == x == 3:
      print('Empate! Você e o computador pensaram em pedra')
elif escolha == 1 and x == 2:
      print('Você perdeu! O computador pensou em tesoura e você pensou em papel!')
elif escolha == 1 and x == 3:
      print('Você ganhou! Parabéns!')
elif escolha == 2 and x == 1:
      print('Você ganhou! Parbéns!')
elif escolha == 2 and x == 3:
      print('Você perdeu! Você pensou em tesoura e o computador em pedra!')
elif escolha == 3 and x == 2:
      print('Você ganhou! Parabéns!')
elif escolha == 3 and x == 1:
      print('Você perdeu! Você pensou em pedra e o computador em papel!')
else:
      print('Obrigado por jogar!')