# Utilizando Módulos

#import (comando para importar um módulo)
#import bebida (importa todas as bebidas)
#from bebbida import pudim (importa apenas a funcionalidade escolhida)
'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # arredonda pra cima
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) # arredonda para baixo
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#from math import sqrt, floor (pode substituir o import math   l7)
#o print seria: print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
'''
import random # biblioteca que gera números aleatórios
num = random.random() # gera um número entre 0 e 1
x = random.randint(1,10) # gera um número dentro desse intervalo
print(num, x)