def soma(l, num):
    soma = 0
    for e in range(num, len(l) - num):
        soma += l[e]
    return soma

def soma_moldura(m, num):
    somar = 0
    for e in range(num, len(m) - num):
        if e == num:
            somar += soma(m[e], num)
        elif e == len(m) - (num + 1):
            somar += soma(m[e], num)
        else:
            if num < (len(m) // 2):
                somar += m[e][num]
                somar += m[e][num + (num + 1)]
            else:
                somar += m[e][e]
    return somar

M = [[1,  2,  3,  4 ], [5,  6,  7,  8 ], [9,  10, 11, 12], [14, 15, 16, 17]]
print(soma_moldura(M, 0))
print(soma_moldura(M, 1))
