vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
lvogais = 0
lconsoantes = 0
palavras = 1

while True:
    palavra = input()
    for e in range(len(palavra)):
        for i in range(len(vogais)):
            if palavra[e] == vogais[i]:
                lvogais += 1
                break
        for i in range(len(consoantes)):
            if palavra[e] == consoantes[i]:
                lconsoantes += 1
                break
    if lconsoantes > lvogais:
        break
    palavras += 1
    lvogais = 0
    lconsoantes = 0

print(palavras)
