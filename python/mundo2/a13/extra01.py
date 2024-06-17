'''
Desafio: 
Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, 
você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

Entrada:
Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta.

Saída:
O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. 
A cada passo, imprima uma mensagem informando a distância percorrida até o momento.
'''

# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
if quantidade_passos > 0 :
  #// Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.
  for i in range(1,quantidade_passos+1):
    if i == 1:
      print(f"Explorador: {i} passo")
    else:
      print(f"Explorador: {i} passos")
#// Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
elif quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")
else:
  print("Coloque um número mair que zero.")
