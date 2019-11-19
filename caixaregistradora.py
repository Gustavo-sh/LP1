def calcula_comissao(lista):
    comissao = 0
    for e in lista:
        if e < 1000.0:
            comissao += e * 0.05
        elif 1000.0 <= e < 5000.0:
            comissao += e * 0.1
        else:
            comissao += e * 0.15
    return comissao

def somar(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma

def caixa_registradora(lista, meta):
    soma = somar(lista)
    comissao = calcula_comissao(lista)
    estado = ''
    listaf = []
    if (soma - comissao) >= meta:
        estado = 'Lucro'
    else:
        estado = 'Prejuizo'
    listaf.append(float(soma))
    listaf.append(float(comissao))
    listaf.append(estado)
    return listaf
