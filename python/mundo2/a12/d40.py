#ATÉ A AULA 12
'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
'''

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2)/2
if m < 5:
    print('A média do alun@ é {:.1f}. Significa Reprovação.'.format(m))
elif 5 <= m <= 6.9:
    print('A média do alun@ é {:.1f}. Significa recuperação.'.format(m))
else:
    print('A média do alun@ é {:.1f}. Significa aprovação.'.format(m))