import string

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_palavras = []
palavras = []
lista = []

for e in range(3):
    palavra = input()
    palavras.append(palavra)
    for e in range(len(palavra)):
        for i in range(len(letras) - 1):
            if palavra[e] == letras[i]:
                    num_palavras.append(i)

maior = 0

for e in range(len(palavras[0])):
    maior = num_palavras[e]
    if num_palavras[e + len(palavras[0])] > maior:
        maior = num_palavras[e + (len(palavras[0]))]
    if num_palavras[e + (len(palavras[0])) * 2] > maior:
        maior = num_palavras[e + (len(palavras[0]) * 2)]
    lista.append(letras[maior])

print(''.join(lista))
