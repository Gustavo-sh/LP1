vezes = int(input())
lista = []
soma = 0

for e in range(vezes):
    geral = input().split(',')
    lista.append(geral[0])
    lista.append(geral[1])

chave = input()

for e in range(len(lista)):
    if lista[e] == chave:
        soma += int(lista[e + 1])

print('R$ {}'.format(soma))
