'''
Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
delas e escrevendo o nome escolhido.
'''
import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input(('Digite o nome do quarto aluno: ')))
nomes =[n1,n2,n3,n4]
n = random.choice(nomes)
print('O aluno escolhido foi {}.'.format(n))
