#ATÉ A AULA 16
'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os últimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense.
'''

g20 = ('Atletico-MG','Internacional','São Paulo','Flamengo','Palmeiras','Santos','Gremio',
       'Fluminense','Bahia','Bragantino','Athletico-PR','Sport Recife', 'Fortaleza',
       'Corinthias','Ceará-SC','Atlético-GO','Vasco da Gama','Coritiba','Botafogo','Goiás')
print('-='*20)
print(f'Os cincos primeiros colocados {g20[:5]}')
print('-='*20)
print(f'Os últimos quatro colocados na lista da série A são {g20[-4:]}')
print('-='*20)
print(f'Os times em ordem alfabética {sorted(g20)}')
print('-='*20)
print('O Chapecoense não está na lista do Brasileirão de 2020.')
#print(f'O chapecoense está na {g20.index("Chapecoense")+1} posição.')# .index('arg') serve para cahar algo na lista
# e o +1 é por conta posição
print('-='*20)