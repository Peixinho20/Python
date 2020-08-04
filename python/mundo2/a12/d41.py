#ATÉ A AULA 12
'''
A Confederção Nacional de Natação precisa de uma programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''
nome = str(input('Digite seu nome: '))
idade = int(input('Agora informe sua idade: '))
if idade < 9:
    print('{} está na categoria mirim!'.format(nome))
elif 9 <= idade < 14:
    print('{} está na categoria infantil.'.format(nome))
elif 14 <= idade < 19:
    print('{} está na categoria junior.'.format(nome))
elif 19 <= idade < 22:
    print('{} está na categoria sênior.'.format(nome))
else:
    print('{} está na categoria master.'.format(nome))