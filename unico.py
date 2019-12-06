def unico(string):
    if string == '':
        return string
    stringg = ''
    for e in range(len(string) - 1):
        if e == len(string) - 2:
            if string[e + 1] == string[e]:
                stringg += string[e]
            else:
                stringg += string[e]
                stringg += string[e + 1]
        elif string[e + 1] != string[e]:
            stringg += string[e]
    return stringg
