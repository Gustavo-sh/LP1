import string

vezes = input()
sequencia = input().split()
lista = []
cont = 0
for e in range(len(sequencia)):
    if sequencia[e] == vezes:
        lista.append(str(e))
        cont += 1

if cont == 0:
    print('-1')
else:
    print(' '.join(lista))

# Gustavoas 119210741
# UFCG 2019.2
