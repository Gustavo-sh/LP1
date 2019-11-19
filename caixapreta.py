quant = int(input())
vezes = quant - 1
validos = 0

for e in range(quant):
    valores = input().split()
    for v in range(1):

        if valores[0][0] == '-':
            print('dado inconsistente. peso negativo.')
            break
        elif valores[1][0] == '-':
            print('dado inconsistente. combustível negativo.')
            break
        elif valores[2][0] == '-':
            print('dado inconsistente. altitude negativa.')
            break

    if valores[0][0] != '-':
        validos += 1
    else:
        break

    if valores[1][0] != '-':
        validos += 1
    else:
        break
    if valores[2][0] != '-':
        validos += 1
    else:
        break
    vezes -= 1

for e in range(vezes):
    new = input()

print('{} dados válidos.'.format(validos))

# Gustavoas 119210741
# UFCG 2019.2
