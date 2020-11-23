#TUPLAS
'''
#TUPLAS SÃO IMUTÁVEIS FORA DA SUA DECLARAÇÃO
lanche = ('Hanbuguer','Suco','Pizza','Pudim') #tupla são entre () lista são [] e dicionario são {}
print(lanche)
print(lanche[-1])
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[-2]) # mostra o pudim
print(lanche[-3]) # mostra a pizza
print(lanche[0:3]) # vai do elemento 1 ao elemento 2 sem considerar o elementoo 3
print(lanche[1:]) # vai mostrar do elemento 2 até o final
print(lanche[:1]) # vai mostrar do 0 ao 1
print(lanche[-3:]) # vai começar na pizza e vai até o final, no pudim
print(lanche[-4:]) # começar no suco e vai até o final, no pudim
lanche = ('Hanbuguer','Suco','Pizza','Pudim') #tupla são entre () lista são [] e dicionario são {}
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(len(lanche))
'''

'''
lanche = ('Hanbuguer','Suco','Pizza','Pudim') #tupla são entre () lista são [] e dicionario são {}
for cont in range(0,len(lanche)):
    print(lanche[cont]) # sem a palavra lanche nessa linha, o programa mostraria o número das posições
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}') outra forma de mostrar
print('Comi pra caramba!')
# os dois for acima são iguais
#outro metodo
for posicao, comida in enumerate(lanche): # mostra tanto o dado quanto a posição
    print(f'Eu vou comer {comida} na posição {posicao}')
lanche = ('Hanbuguer','Suco','Pizza','Pudim') #tupla são entre () lista são [] e dicionario são {}
print(sorted(lanche)) #printa em ordem alfabética e em forma de lista
'''
'''
a = (2,5,4)
b = (5,8,1,2)
print(a)
print(b)
c = b + a
print(c)
print(len(c))
print(c.count(5))# quantas vezes aparece o 5
print(c.index(8))# em que posição está o número 8
print(c.index(5,1))# mostrar a posiçao do 5 apartir da posiçao 1
'''

pessoa = ('Gustavo', 39,'M',99.88) # pode misturar dados de naturezas diferentes
#del(pessoa) # apaga a tupla inteira
print(pessoa)
