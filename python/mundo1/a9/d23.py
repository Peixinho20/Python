'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
Até a aula 9
Ex:
Digite um número: 1834
unidades: 4
dezenas: 3
centenas: 8
milhar: 1
Atenção: Esse exercício só será bem executado ser for digitado os 4 algarismos, mesmo que sejam zeros
'''
n = int(input('Insira um número entre 0 e 9999:'))
u = n // 1 % 10  # faz a divisão inteira por 1, ou seja n, e usa o resto da divisão de n por 10 como resposta
d = n // 10 % 10  # divisão inteira por 10, e usa a parte inteira do resto da divisão por dez de novo como resposta
c = n // 100 % 10  # divisão inteira por 100, e usa a parte inteira do resto da divisão por dez como resposta
m = n // 1000 % 10  # divisão inteira por 1000, e usa a parte inteira do resto da divisão por 10 como resposta
print('Analisando o número {}'.format(n))
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u,d,c,m))


#ou
'''
x = input('Digite um número entre 0 e 9999:')
if len(x) == 1:
    x = (x._add_('000'))
    print('Unidade:{}, Dezena:{}, Centena:{}, Milhar:{}'.format(x[0], x[1], x[2], x[3]))
elif len(x) == 2:
    x = (x._add_('00'))
    print('Unidade:{}, Dezena:{}, Centena:{}, Milhar:{}'.format(x[1], x[0], x[2], x[3]))
elif len(x) == 3:
    x = (x._add_('0'))
    print('Unidade:{}, Dezena:{}, Centena:{}, Milhar:{}'.format(x[2], x[1], x[0], x[3]))
elif len(x) >= 5:
    print('Você digitou um número muito grande!!!! Ele é maior que 9999!!')
else:
    print('Unidade:{}, Dezena:{}, Centena:{}, Milhar:{}'.format(x[3], x[2], x[1], x[0]))
'''