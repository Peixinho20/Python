#Condições (Parte 1)
'''
if condiçaõ():
    bloco True
else:
    bloco False
'''

#Exemplos:
'''1
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('Fim')
'''

'''2.Versão Simplificada
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo<=3 else'carro velho')
print('Fim')
'''
'''3
nome = str(input('Qual é o seu nome? '))
if nome == 'Camila':
    print('Que lindo nome você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))    
'''
'''4
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')
'''
