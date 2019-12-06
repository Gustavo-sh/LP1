linhas = int(input())
num = int(input())
maior = num
menor = num
abaixo = 0
acima = 0
lista = []
lista.append(num)

for i in range(linhas - 1):
    numeros = int(input())
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
    lista.append(numeros)

media = (maior + menor) / 2

for e in lista:
    if e < media:
        abaixo += 1
    elif e > media:
        acima += 1

print('Menor número: {}'.format(menor))
print('Maior número: {}'.format(maior))
print('Média dos extremos: {:.2f}'.format(media))
print('{} número(s) abaixo da média'.format(abaixo))
print('{} número(s) acima da média'.format(acima))

# Gustavoas 119210741
# UFCG 2019.2
