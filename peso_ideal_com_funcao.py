def calculaPeso(sexo, altura):
    peso = 0
    if sexo == 'M' or sexo == 'm':
        peso = 72.7 * altura - 58
        print('Homem: peso ideal é {:.1f}'.format(peso))
    if sexo == 'F' or sexo == 'f':
        peso = 62.1 * altura - 44.7
        print('Mulher: peso ideal é {:.1f}'.format(peso))
    return peso

while True:
    des = input()
    if des == '****': break
    dos = des.split()
    calculaPeso(dos[0], float(dos[1]))
