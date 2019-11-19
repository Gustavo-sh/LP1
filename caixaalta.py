def minuscula(l):
    minusc = chr(ord('a') + ord(l) - ord('A'))
    return minusc
def maiuscula(l):
    maiusc = chr(ord('A') + ord(l) - ord('a'))
    return maiusc
def caixa_alta(frase):
    string = ''
    if len(frase) == 1:
        if frase >= 'A' and frase <= 'Z':
            string += minuscula(frase)
            return string
        else:
            string += frase
            return string
    if frase[1] == ' ':
        if frase[0] >= 'A' and frase[0] <= 'Z':
            string += minuscula(frase[0])
        else:
            string += frase[0]
    if frase[1] != ' ':
        if frase[0] >= 'a' and frase[0] <= 'z':
            string += maiuscula(frase[0])
        else:
            string += frase[0]
    for e in range(1, len(frase) - 1):
        if frase[e] == ' ':
            string += ' '
        elif frase[e - 1] == ' ' and frase[e + 1] == ' ':
            if frase[e] >= 'A' and  frase[e] <= 'Z':
                string += minuscula(frase[e])
            else:
                string += frase[e]
        elif frase[e - 1] == ' ':
            if frase[e] >= 'a' and frase[e] <= 'z':
                string += maiuscula(frase[e])
            else:
                string += frase[e]
        else:
            string += frase[e]
    if frase[-2] == ' ':
        if frase[-1] >= 'A' and frase[-1] <= 'Z':
            string += minuscula(frase[-1])
        else:
            string += frase[-1]
    else:
        string += frase[-1]
    print(string)
    return string
