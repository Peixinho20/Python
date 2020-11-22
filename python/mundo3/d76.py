#ATÉ A AULA 16
'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.
'''
listagem = ('Lápis', 1.20,
            'Caneta',1.50,
            'Borracha',2.0,
            'Papel Almaço',0.40,
            'Lapiseira',2.50)
print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos%2 == 0:
        print(f'{listagem[pos]:.<30}',end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)