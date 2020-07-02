'''
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
até a aula 7
'''

n = int(input('Digite um número:'))
a = n*0
b = n*1
c = n*2
d = n*3
e = n*4
f = n*5
g = n*6
h = n*7
i = n*8
j = n*9
k = n*10
print('A tabuada desse número é: \n\033[0;35;44m{}\033[m \n\033[1;36;45m{}\033[m \n\033[4;37;46m{}\033[m '
      '\n\033[7;30;47m{}\033[m \n\033[0;31;40m{}\033[m \n\033[1;32;41m{}\033[m \n\033[4;33;42m{}\033[m '
      '\n\033[7;34;43m{}\033[m \n\033[0;35;44m{}\033[m \n\033[1;36;45m{}\033[m \n\033[4;37;46m{}\033[m '.format(a,b,c,d,e,f,g,h,i,j,k))