#ATÉ A AULA 12
'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão preço normal sem juros
- 3x ou mais no cartão: 20% de juros
'''
print('Vendas!')
produto = float(input('Digite o valor do produto: R$'))
print('As opções de pagamento são:\n'
      '[1] à vista no dinheiro ou cheque com 10% de desconto\n'
      '[2] cartão de débito com 5% de desconto\n'
      '[3] cartão de crédito em até 2x sem juros\n'
      '[4] 3x ou mais no crédito com 20% de juros ')
escolha = int(input('Digite sua escolha: '))
if escolha == 1:
      vista = produto - (10 / 100) * produto
      print('O produto  que custava R${} vai custar R${:.2f}!'.format(produto,vista))
elif escolha == 2:
      debito = produto - (5 / 100) * produto
      print('O produto que custava R${} vai custar R${:.2f}!'.format(produto,debito))
elif escolha == 3:
      duas = produto / 2
      print('O produto que custava R${} vai custar R${:.2f}!'.format(produto,duas))
elif escolha == 4:
      n = int(input('Quantas vezes? '))
      x = (produto + (20 / 100) * produto)
      y = x/n
      print('O produto que custava R${} vai custar R${:.2f} e a sua mensalidade será R${:.2f}!'.format(produto,x,y))
else:
      print('Obrigado e volte sempre!')




