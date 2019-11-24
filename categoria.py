nome = input()
idade = int(input())

if idade >= 5 and idade <=7:
    categoria = 'Infantil A'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))

elif idade >= 8 and idade <= 10:
    categoria = 'Infantil B'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))

elif idade >= 11 and idade <= 13:
    categoria = 'Juvenil A'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))

elif idade >= 14 and idade <= 17:
    categoria = 'Juvenil B'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))

elif idade > 17:
    categoria = 'Senior'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))

else:
    categoria = 'Não pode competir'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))

# Gustavoas 119210741
# UFCG 2019.2
# Questão categoria do tst
