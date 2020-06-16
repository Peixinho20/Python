'''
ATÉ A AULA 10
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
a R$ 1,250.00 calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.
'''
s = int(input('Digite seu salário: '))
if s <= 1250:
    a = (1250 + (15*1250)/100)
    print('O seu aumento será de 15%, logo seu novo salário será de R$ {:.2f}'.format(a))
else:
    b = (1250 + (10*1250)/100)
    print('O seu aumento será de 10%, logo seu novo salário será de R$ {:.2f}'.format(b))