Crie um programa que permita cadastrar uma lista de itens que o personagem possui. A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

Entrada
O programa deve solicitar ao usuário o nome dos 3 itens que o personagem possui. Cada item deve ser cadastrado separadamente.

Saída
Após receber os itens cadastrados pelo usuário, o programa deve exibir na tela a lista de itens que o personagem possui. A saída deve ter o seguinte formato:

Lista de itens:
- [item1]
- [item2]
- [item3]

# Lista para armazenar os itens
itens = []

#TODO: Solicite os itens ao usuário
for elemento in range (0,3):
    itens.append(str(input(" ")))
    
print("Lista de itens:")    
for elemento in itens:
    print(f"- {elemento}")
