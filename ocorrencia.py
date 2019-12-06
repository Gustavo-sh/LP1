def my_in_especial(ref, l):
    for elemento in range(0, len(l), 2):
        if l[elemento] == ref:
            return True
        elif chr(ord('a') + ord(l[elemento]) - ord('A')) == ref:
            return True
        elif chr(ord('A') + ord(l[elemento]) - ord('a')) == ref:
            return True
    return False

palavra = input()
lista = []

def minu(le):
    minu = chr(ord('a') + ord(le) - ord('A'))
    return minu


def maiu(le):
    maiu = chr(ord('A') + ord(le) - ord('a'))
    return maiu

for e in range(len(palavra)):
    if not my_in_especial(palavra[e], lista):
        lista.append(palavra[e])
        lista.append(1)
    else:
        for i in range(0, len(lista), 2):
            if palavra[e] == lista[i]:
                lista[i + 1] += 1
            elif minu(palavra[e]) == lista[i]:
                lista[i + 1] += 1
            elif maiu(palavra[e]) == lista[i]:
                lista[i + 1] += 1

maior = 0
letra = ''

for e in range(1, len(lista), 2):
    if lista[e] > maior:
        maior = lista[e]
        letra = lista[e - 1]

if letra < 'a':
    print(minu(letra), maior)
else:
    print(letra, maior)
