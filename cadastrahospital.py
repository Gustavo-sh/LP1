lista_all = [[], [], [], [], []]
lista = []

def cadastra(l, nome, cor):
    if cor == 'vermelho':
        l[0].append(nome)
    elif cor == 'laranja':
        l[1].append(nome)
    elif cor == 'amarelo':
        l[2].append(nome)
    elif cor == 'verde':
        l[3].append(nome)
    else:
        l[4].append(nome)

def resumo(cor, l):
    vermelho = 0
    laranja = 0
    amarelo = 0
    verde = 0
    azul = 0
    for e in range(len(l)):
        ver = l[e].split()
        if ver[1] == 'vermelho':
            vermelho += 1
        elif ver[1] == 'laranja':
            laranja += 1
        elif ver[1] == 'amarelo':
            amarelo += 1
        elif ver[1] == 'verde':
            verde += 1
        else:
            azul += 1
    if cor == 'vermelho':
        return vermelho
    elif cor == 'laranja':
        return laranja
    elif cor == 'amarelo':
        return amarelo
    elif cor == 'verde':
        return verde
    else:
        return azul

while True:
    nome = input()
    if nome == 'fim': break
    lista.append(nome)
    true = nome.split()
    cadastra(lista_all, true[0], true[1])

for e in range(len(lista_all)):
    for i in range(len(lista_all[e])):
        print(lista_all[e][i])

print('---')

print('vermelho: {}'.format(resumo('vermelho', lista)))
print('laranja: {}'.format(resumo('laranja', lista)))
print('amarelo: {}'.format(resumo('amarelo', lista)))
print('verde: {}'.format(resumo('verde', lista)))
print('azul: {}'.format(resumo('azul', lista)))

print('---')
