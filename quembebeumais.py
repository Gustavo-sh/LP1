def quem_bebeu_mais_menos(m1, m2):
    soma = 0
    maior = 0
    soma2 = 0
    menor = 0
    look1 = 0
    look2 = 0
    for e in range(len(m1)):
        for i in range(len(m1[e])):
            soma += m1[i][e]
        if look1 == 0:
            look1 = soma
            maior = e + 1
        if soma > look1:
            look1 = soma
            maior = e + 1
        soma = 0
    for e in range(len(m2)):
        for i in range(len(m2[e])):
            soma2 += m2[i][e]
        if look2 == 0:
            look2 = soma2
            menor = e + 1
        if soma2 < look2:
            look2 = soma2
            menor = e + 1
        soma2 = 0
    return (maior, menor)
