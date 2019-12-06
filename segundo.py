def bublle_maior(lista):
    controle = False
    troca = False
    while not controle:
        for e in range(len(lista) - 1):
            if lista[e] > lista[e + 1]:
                lista[e], lista[e + 1] = lista[e + 1], lista[e]
                troca = True
        if troca == False:
            controle = True
        troca = False
    return lista

def bublle_menor(lista):
    controle = False
    troca = False
    while not controle:
        for e in range(len(lista) - 1):
            if lista[e] < lista[e + 1]:
                lista[e], lista[e + 1] = lista[e + 1], lista[e]
                troca = True
        if troca == False:
            controle = True
        troca = False
    return lista

lista = []
for e in range(4):
    num = int(input())
    lista.append(num)
print('Considerando os números {}, {}, {} e {}'.format(lista[0], lista[1], lista[2], lista[3]))

def segs(lista):
    bublle_maior(lista)
    lista.pop()
    bublle_menor(lista)
    lista.pop()
    if lista[0] > lista[1]:
        print('O segundo menor número é {}'.format(lista[1]))
        print('O segundo maior número é {}'.format(lista[0]))
    else:
        print('O segundo menor número é {}'.format(lista[0]))
        print('O segundo maior número é {}'.format(lista[1]))

segs(lista)
