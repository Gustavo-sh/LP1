def meu_split(palavra, simbolo):
    aux = ''
    for c in palavra:
        if c == simbolo:
            aux += ' '
        else:
            aux += c
    return aux.split()

def is_substring_expr(str1, str2):
    a = meu_split(str2, '*')
    auxiliar = ''
    if len(str1) > 0:
        for c in range(len(a[0])):
            auxiliar += str1[c]
        diferenca = 0
        cont = 0
        aux2 = ''
        if auxiliar == a[0]:
            cont += 1
            diferenca = len(str1) - len(a[1])
            for i in range(diferenca, len(str1)):
                aux2 += str1[i]
            if aux2 == a[1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
