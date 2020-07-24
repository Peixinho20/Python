'''
Operadores aritméticos
'''

5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2 #divisão inteira
5 % 2 == 1#resto da divisão

'''Ordem de precedencia

1º ()
2º **
3º *,/,//,%
4º +,-
'''
'''
Replicar Informações

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) # escreve o conteúdo da varialvem em 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome)) # alinha o conteúdo a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # alinnha a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # centraliza o conteudo
print('Prazer em te conhecer {:=^20}!'.format(nome)) #centraliza o conteúdo e o restante do espaço é preenchido com ==
'''

'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1*n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {}, a divisão é {:.3f}'.format(s,m,d), end=' ') # :.3f significa que irá mostrar até
# 3 casas decimais; \n significa quebrar a linha; end='' signfica que não haverá quebra de linha entre um print e outro
print('Adivisão inteira é {} e potência é {}'.format(di,e))
'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
di = n1 // n2
d = n1 % n2
print(di,d)