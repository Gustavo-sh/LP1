def separa(string):
    stringg = ''
    lista = []
    for e in range(len(string)):
        if e == len(string) - 1:
            stringg += string[e]
            lista.append(stringg)
        elif string[e]!= ' ':
            stringg += string[e]
        else:
            lista.append(stringg)
            stringg = ''
    return lista
def meu_in(string):
    for e in range(len(string)):
        if string[e] == ' ':
            return True
    return False
def maior_palavra(string):
    separado = separa(string)
    maior = ''
    if not meu_in(string):
        return string
    for e in range(len(separado) - 1, -1, - 1):
        if len(separado[e]) > len(maior):
            maior = separado[e]
    return maior
