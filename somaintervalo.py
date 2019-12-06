def soma_intervalo(a,b):
    soma = 0
    if a != b:
        for e in range(abs(a - b) + 1):
            soma += a
            a += 1
    else:
        return a
    return soma
