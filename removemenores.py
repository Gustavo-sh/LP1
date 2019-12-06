def remove_menores(num, l):
    quant = 0
    for e in range(len(l) - 1, -1, -1):
        if l[e] < num:
            quant += 1
            l.pop(e)
    return quant
