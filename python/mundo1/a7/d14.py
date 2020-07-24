'''
Crie um programa que converta uma temperatura digitada em °C e converta para °F.
'''

c = float(input('Informe a temperatura em °C: '))
f = (9/5)*c + 32
print('A temperatura \033[1;35;44m{:.1f}°C\033[m corresponde a \033[4;36;45m{:.1f}°F\033[m.'.format(c,f))

