#Manipulando Cadeia de Texto

#Fatiamento
'''
frase = 'Curso em Vídeo'
frase[9] #pega a letra na nona posição apartir do zero
frase[9:13] #pega do 9 até o 12, o treze não está incluído
frase[9:21] #pega do 9 até o 20
frase[9:21:2] #pega do 9 até o 20 pulando de 2 em 2
frase[:5] #começa do zero até o 5, sem incluí-lo
frase[15:] #começa do 15 até o final da frase
frase[9::3] #começa no 9 vai até o final pulando de 3 em 3

#Análise

len(frase) #comprimento da frase, nesse caso 21 caractere
frase.count('o') #contar quantas vezes aparece o 'o' minúsculo
frase.count('o',0,13) #contagem com fatiamento, do zero até o treze sem incluí-lo contanto os 'o'
frase.find('deo') #mostra em que momento começou 'deo' e quantas vezes ele achou essas sequencia
frase.find('Android') #como não tem essa palavra em frase, ele dará a posição como -1
'Curso'in frase #existe curso em frase? True

#Transformação

frase.replace('Python','Android') # substitiu a primeira palavra pela segunda se a primeira existir na sentença
frase.upper() # letras em maiúsculo
frase.lower() #letras em minúsculo
frase.capitalize()# joga todos os caracteres em minúsculo e só a primeira letra em maiúsculo
frase.title() # analisa quantas palavras tem e faz o capitalize de palavra por palavra
frase.strip() #Remove espaços inúteis em uma string, espaços vazios antes da frase por exemplo
frase.rstrip() #remove espaços da direita
frase.lstrip()#remove espaços da esquerda

#Divisão

frase.split() # gera listas independentes com cada uma das palavras em uma strind, ou seja, divide os espaços

#Junção

'-'.join(frase) # juntas as listas independentes em uma string só
'''

frase = 'Curso em Vídeo Python'
#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[1:15])
#print(frase[1:15:2])
#print(frase[1::2])
#print(frase[::2])
#print('''blá blá blá blá blá blá blá blá blá blá
 #blá blá blá blá blá blá blá blá
 #blá blá blá blá blá blá blá blá blá blá
 #blá blá blá blá blá blá blá blá blá''')
#print(frase.count('o'))
#print(frase.count('O'))
#print(frase.count('oi'))
#print(frase.upper().count('O')) #conta quantas vezes tem 'O' na frase em letra maiúscula
#print(len(frase.strip()))
#print(frase.replace('Python','Android'))
'''
frase = frase.replace('Python','Android') # salva as mudanças do replace
print(frase)
'''
#print('Curso'in frase)
#print(frase.find('Curso')) #mostra a posição
#print(frase.lower().find('vídeo')) #achar 'vídeo' em frase em minúsculo
#print(frase.split()) # cria uma lista com o split, q é um separador de espaços
'''
dividido = frase.split()
print(dividido)
ou
print(dividido[0]) #mostra o item na posição 0 da lista
ou
print(dividido[0][3])# o primeiro mostra a posição (Curso) e o segundo mostra a terceira posição da letra (s)
'''
