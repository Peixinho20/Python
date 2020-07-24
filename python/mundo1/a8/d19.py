'''
Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome escolhido. Até a aula 8.
'''
import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
n5 = str(input('Digite o quinto nome: '))
nomes =[n1,n2,n3,n4,n5]
n = random.choice(nomes)
print('O aluno escolhido foi \033[1;35;42m{}\033[m.'.format(n))
