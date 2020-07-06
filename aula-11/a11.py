'''
\033[m  estrurura de um código para cores no terminal
quando ela está no início e fim do código significa que as cores ficarão limitadas ao tamanho do print
\033[style;text;back;m
\033[0;33;44m  esses valores são códigos para a linha de cima

style do texto
0 (sem estilo)
1 (bold ou negrito)
4 (underline)
7 (negativo, inverte as cores)

text                        background
30 branco                   40 branco
31 vermelho                 41 vermelho
32 verde                    42 verde
33 amarelo                  43 amarelo
34 azul                     44 azul
35 roxo                     45 roxo
36 azul claro               46 azul claro
37 cinza                    47 cinza
'''

#print('\033[31m Olá, Mundo!')
#print('\033[1:31:43m Olá, mundo!\033[m')
#print('\033[4;30;45m Olá, mundo!\033[m')
#print('\033[30m Olá, mundo!\033[m')
#print('\033[7;30m Olá, mundo!\033[m')
#print('\033[33;44m Olá, mundo!\033[m')
#print('\033[7;33;44m Olá, mundo!\033[m')
#módulo colorize
'''
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}'.format(a,b))
'''
'''
nome = 'Camila'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))
#cada item entre as vórgulas estão associadas a um colchete no exemplo acima
'''
'''
#Dicionário (vai explicar melhor depois)
nome = 'Camila'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
'''


#Desafio: Refazer todos os exercícios colocando cores
