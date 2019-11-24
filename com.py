def ver(l):
    num = 0
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for e in range(len(l)):
        for i in range(len(vogais)):
            if l[e] == vogais[i]:
                num += 1
    return num


def remove_palavras_com_mais_vogais(l):
    law = []
    if l == []:
        return None
    for e in range(len(l)):
        law.append(ver(l[e]))
    maior = law[0]
    for e in range(len(law)):
        if law[e] > maior:
            maior = law[e]
    for e in range(len(l) - 1, -1, -1):
        if ver(l[e]) == maior:
            l.pop(e)
