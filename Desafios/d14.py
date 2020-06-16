'''
Crie um programa que converta uma temperatura digitada em °C e converta para °F.
'''

c = float(input('Informe a temperatura em °C: '))
f = (9/5)*c + 32
print('A temperatura {:.1f}°C corresponde a {:.1f}°F.'.format(c,f))

