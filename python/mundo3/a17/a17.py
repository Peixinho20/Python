# Aula de Listas = []
'''
lanche = ['hamburguer','suco','pizza','pudim']
lanche[3] = 'picolé' # a posição 3 original será eliminado e substituído por picolé
# Adicionar elementos no final
lanche.append('biscoito')
# Adicionar elementos em qualquer posição
lanche.insert(0,'cachorro-quente') # adiciona cachorro quente na posição 0
'''
'''
# Apagar elementos # elimina o valor e reposiciona as contagem dos indices
del lanche[3]
lanche.pop(3) # se quiser remover no final da lista ésó deixar o argumento vazio
lanche.remove('pizza')
# Para remorver o elemento que não existe utilize o if
if 'pizza' in lanche:
    lanche.remove('pizza')
'''
'''
# Criar lista apartir de range
valores = list(range(4,11))
valores = [8,2,5,4,9,3,0]
valores.sort() # ordena os valores dentro de valores
valores.sort(reverse=True) # reordena na ordem inversa
len(valores) # retorna o tamanho da lista valores
'''
'''
num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
#num.insert(2,0) # adiciona 0 na posição 2
# num.pop() # elimina o ultimo elemento
# num.pop(2) # elimina o elemento na posição 2
num.insert(2,2)
num.remove(2) # elimina a primeira ocorrencia do elemento 2
print(num)
print(f'Essa lista tem {len(num)} elementos')
'''
'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # essa função acha a posição c e o seu valor v
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''
'''
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores): # essa função acha a posição c e o seu valor v
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''
a = [2,3,4,7]
b = a # cria uma ligação entre as duas, então se houver mudanças em uma haverá na outra
#b[2] = 8 #ligação entre as duas listas sem o comando abaixo
b = a[:] # cria uma cópia dos valores de a em b
b[2] = 8 # com o comando acima não cria ligação entre as listas, só uma cópia
print(f'Lista A: {a}')
print(f'Lista B: {b}')
