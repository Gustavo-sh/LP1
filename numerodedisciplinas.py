def in_es(lista, pdic):
    cont = 0
    for e in range(len(lista)):
        if lista[e] == pdic[e]:
            cont += 1
    if cont == len(lista):
        return True
    return False


def pode(dic, lista):
    pode = []
    for e in dic:
        if dic[e] == []:
            pode.append(e)
        else:
            if len(lista) <= len(dic[e]):
                if in_es(lista, dic[e]):
                    pode.append(e)
    return pode

def meu_in(horarios, ref):
    lista = []
    for e in horarios.items():
        if e != ref:
            if e[1] == ref[1]:
                lista.append(e[0])
                lista.append(ref[0])


def naopode(horarios, lista):
    aux = []
    for e in horarios.items():
        aux.append(meu_in(horarios, e))
    return aux
def my_in(listinha, lista):
    for e in range(len(listinha)):
        if listinha[e] in
def numero_disciplinas(grade, horarios, lista):
    pode = pode(grade, lista)
    naopode = naopode(horarios, lista)
    for e in range(len(naopode)):
        for i in range(len(naopode[e])):
            if naopode[e][i] in pode:
