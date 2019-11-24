def divisor(num, lista):
    for e in range(len(lista)):
        div = str(lista[e] / num)
        if div[len(div) - 1] == '0':
            return e
    return -1
