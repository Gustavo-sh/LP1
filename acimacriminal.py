import string

chave = float(input())
lista = []
div = chave / 2
media = 0

while True:

    valores = input().split()
    teste = ' '.join(valores)

    if teste != 'fim':
        soma = 0
        for e in valores:
            soma += float(e)

        media = soma / len(valores)

        if media > chave:
            lista.append(' '.join(valores))

    if media < div or teste == 'fim':
        break

if lista != []:
    for e in lista:
        print(e)

