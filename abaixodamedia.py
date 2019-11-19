lista = []
indice = 1
soma = 0
quant = 0

while True:
    num = input()
    if num == 'fim':
        break
    soma += int(num)
    quant += 1
    lista.append(int(num))
    lista.append(indice)
    indice += 1

media = soma / quant
print('{:.2f}'.format(media))

for e in range(0, len(lista), 2):
    if lista[e] < media:
        print('{} {}'.format(lista[e + 1], lista[e]))
