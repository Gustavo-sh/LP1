def calcula_digitos_verificacao(string):
    my = string
    indice = 2
    digito = 0
    verifica = ''
    for e in range(len(string) - 1, -1, -1):
        digito += int(string[e]) * indice
        indice += 1
    digito *= 10
    digito = digito % 11
    if digito == 10:
        my += '0'
        verifica += '0'
    else:
        my += str(digito)
        verifica += str(digito)
    digito = 0
    indice = 2
    for e in range(len(my) - 1, -1, -1):
        digito += int(my[e]) * indice
        indice += 1
    digito *= 10
    digito = digito % 11
    if digito == 10:
        verifica += '0'
    else:
        verifica += str(digito)
    return verifica
