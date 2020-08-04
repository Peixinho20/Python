#ATÉ A AULA 12
'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''
print('Cálculo do IMC:')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (peso)/(altura**2)
if imc < 18.5:
    print('Você está abaixo do peso! Seu IMC é {:.2f} kg/m².'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está no peso ideal! Seu IMC é {:.2f} kg/m².'.format(imc))
elif 25 <= imc < 30:
    print('Você está no sobrepeso! Seu IMC é {:.2f} kg/m².'.format(imc))
elif 30 <= imc < 40:
    print(' Você está na obesidade!Seu IMC é {:.2f} kg/m².'.format(imc))
else:
    print('Você está na Obesidade mórbida. Seu IMC é {:.2f} kg/m².'.format(imc))