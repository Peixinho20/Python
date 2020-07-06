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

n = str(input('\033[7;33;42mInsira um número entre 0 e 9999:\033[m '))
print('\033[0;34;43mA analisando seu número... \033[m')
print('\033[1;35;44mO primeiro algarismo tem {} unidades\033[m'.format(n[3]))
print('\033[4;36;45mO segundo algarismo tem {} dezenas\033[m'.format(n[2]))
print('\033[7;37;46mO terceiro algarismo tem {} centenas\033[m'.format(n[1]))
print('\033[0;30;47mO quarto algarismo tem {} milhar\033[m'.format(n[0]))
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
