#ATÉ A AULA 12
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele não
pode exceder 30% do salário ou então o empréstimo será negado.
'''
casa = float(input('Empréstimo bancário \n Qual é o valor da casa? '))
salario = float(input('Quanto é o seu salaŕio? '))
anos = int(input('Em quantos anos você pretende pagar? '))

meses = 12*anos
prestacao = casa/meses
porcentagem = (30/100)*salario

if prestacao > porcentagem:
    print('\033[1:30:41mEmpréstimo negado!\033[m O valor da prestação ultrapaça a porcentagem permitida pelo banco!'
          ' \n Prestação: R$ {:.2f} \n 30% do salário: R$ {}'.format(prestacao,porcentagem))
else:
    print('\033[1:30:42mEmpréstimo aprovado!\033[m \n Prestação: R$ {:.2f} \n 30% do salário: R$ {}'.format(prestacao,porcentagem))
print('Tenha um bom dia!')