#Até a aula 14
'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] - somar
[2] - multiplicar
[3] - maior
[4] - novos números
[5] - sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep
n = float(input('Digite um valor: '))
p = float(input('Digite outro valor: '))
print('O que você quer fazer com eles?\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos Números'
      '\n[5] - Sair do programa ')
escolha = int(input('Digite sua escolha: '))
while escolha != 5:
    if escolha == 1:
          r = n + p
          print(r)
    elif escolha == 2:
          r = n * p
          print(r)
    elif escolha == 3:
        if n > p:
            print(n)
        elif p > n:
            print(p)
        elif p == n:
            print('Ele são iguais')
    elif escolha == 4:
        print('Informe os números novamente!')
        n = int(input('Primeiro Valor: '))
        p = int(input('Segundo Valor: '))
    elif escolha == 5:
          print('Saindo do programa...')
          sleep(2)
          print('Obrigado!')
print('Fim')

'''
OUTRO MODO

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
escolha = 0
while escolha != 5:
    print('\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos Números'
       '\n[5] - Sair do programa ')
    escolha = int(input('Qual é a sua escolha? '))
    if escolha == 1:
        r = n1 + n2
        print('O resultado de {} + {} é {}'.format(n1,n2,r))
    elif escolha == 2:
        r = n1*n2
        print('O resultado de {} x {} é {}'.format(n1,n2,r))
    elif escolha == 3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    elif escolha == 4:
        print('Informe os números novamente!')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif escolha == 5:
        from time import sleep
        print('Finalizando programa')
        sleep(2)
    else:
        print('Opção inválida! Tente novamente!')
    print('=-=' * 10)
print('Fim do programa')
'''