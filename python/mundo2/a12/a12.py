# Condições Aninhadas

'''
if condicao1():
    bloco1
elif condicao2():
    bloco2
elif condicao3():
    bloco3
else:
    bloco4

#Estrurura condicional simples
nome = str(input('Qual é o seu nome? '))
if nome == 'Camila':
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(nome))

#Estrurura condicional composta
nome = str(input('Qual a seu nome? '))
if nome == 'Camila':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}.'.format(nome))
'''
#Estrutura condicional aninhada
nome = str(input('Qual o seu nome? '))
if nome == 'Camila':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}.'.format(nome))