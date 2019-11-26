lista = []
beggin = 15.2
lista.append(beggin)

for e in range(14):
    continuedade = beggin - 1.5
    beggin = continuedade
    lista.append(continuedade)

for e in lista:
    print('{:.1f}'.format(e))

# Gustavoas 119210741
# UFCG 2019.2
