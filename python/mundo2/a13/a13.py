#Estrutura de Repetição
'''
for c in range(1,6):
    print('Oi') #printa oi 5 vezes
print('Fim')


for c in range(0,6):
    print('Oi') #printa oi seis vezes
    print('FIM')


for c in range(0,6):
    print(c) #printa de 0 a 5
print('FIM')
'''

for c in range(6,0,-1):
    print(c) # printa de 6 a 0
print('FIM')


for c in range(0,7,2):
    print(c)#printa de 0 a 7 de dois em dois
print('FIM')


n = int(input('Digite uum número: '))
for c in range(0,n):
    print(c) # printa c até n que usuário definiu
print('FIM')


n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print('FIM')


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p):
    print(c) #printa c do com os dados (início, fim e passo) que o usuário definiu
print('FIM')


for c in range(0,3):
    n = int(input('Digite um valor: '))#Faz essa pergunta 3 vezes e armazena todas as respostas
print('FIM')


s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))#faz quatro perguntas e armazena todas as respostas
    s += n #é igual a s = s+n
print('0 somatório de todos os valores foi {}.'.format(s))