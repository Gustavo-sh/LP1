def calcula_seguro(valor, lista):
    pontos = 0
    risco = ''
    listap = []
    taxa = 0

    if lista[0] <= 21 or lista[0] > 60:
        pontos += 20
    elif lista[0] >= 22 and lista[0] <= 30:
        pontos += 15
    elif lista[0] >= 31 and lista[0] <= 40:
        pontos += 12
    elif lista[0] >= 41 and lista[0] <= 60:
        pontos += 10
    if lista[1] == True:
        pontos += 10
    else:
        pontos += 20
    if lista[2] == True:
        pontos += 20
    else:
        pontos += 10
    if lista[3] == True:
        pontos += 20
    else:
        pontos += 10
    if lista[4] == True:
        pontos += 20
    else:
        pontos += 10
    if lista[5] == True:
        pontos += 10
    else:
        pontos += 20
    if lista[6] == 'Lazer':
        pontos += 20
    elif lista[6] == 'Misto':
        pontos += 20
    else:
        pontos += 10
    listap.append(pontos)
    if pontos <= 80:
        risco = 'Risco Baixo'
        listap.append(risco)
        taxa = 0.1
    elif pontos > 80 and pontos <= 100:
        risco = 'Risco Medio'
        listap.append(risco)
        taxa = 0.2
    else:
        risco = 'Risco Alto'
        listap.append(risco)
        taxa = 0.3
    valorf = '{:.1f}'.format(valor * taxa)
    listap.append(float(valorf))
    return listap
