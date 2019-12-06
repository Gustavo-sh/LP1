def radar_transito(limite, tempo):
    velo = (2 / tempo) * 3.6
    multa = 0
    estado = ''
    lista = []
    if velo > 80 and velo <= 88:
        multa = 87.5
        estado = 'Leve'
    elif velo > 88 and velo <= 120:
        multa = 127.5
        estado = 'Média'
    elif velo > 120:
        multa = 577.5
        estado = 'Grave'
    else:
        multa = 0.0
        estado = 'Ok'
    lista.append(estado)
    lista.append(multa)
    return lista
