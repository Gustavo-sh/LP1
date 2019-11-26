alvo = int(input())
maior = 0
lista = []
indice = 1

while True:
    seq = input()
    seq2 = seq.split()
    if seq == 'fim':
        break
    for e in seq2:
        if float(e) > alvo:
            maior += 1
    if maior > (len(seq2) / 2):
        lista.append(indice)
        lista.append(seq)
    indice += 1
    maior = 0

for e in range(0, len(lista) - 1, 2):
    print('sequencia {}: {}'.format(lista[e], lista[e + 1]))
