def conta_alertas_acude(m):
    quant = 0
    for e in range(1, len(m)):
        if abs(m[e] - m[e - 1]) < 10:
            if m[e] < 17:
                quant += 1
            if e == 1:
                if m[e - 1] < 17:
                    quant += 1
    return quant
