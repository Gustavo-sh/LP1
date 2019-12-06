idade = int(input('Idade? '))

if idade < 12:
    print('criança (meia entrada)')

elif idade >= 65:
    print('idoso (meia entrada)')

elif 12 <= idade <= 65:
    estudante = input('Estudante? ')
    if estudante == 's':
        publica = input('Rede Pública? ')
        if publica == 's':
            print('estudante da rede pública (isento)')
        elif publica == 'n':
            print('estudante (meia entrada)')
    elif estudante == 'n':
        print('adulto (inteira)')

# Gustavoas 119210741

