def vogais_primeiro(frase):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = ''
    cont = 0
    for e in frase:
        for i in vogais:
            if e == i:
                string += e
                break
    for e in frase:
        for i in vogais:
            if e != i:
                cont += 1
        if cont == 10:
            string += e
        cont = 0
    return string
