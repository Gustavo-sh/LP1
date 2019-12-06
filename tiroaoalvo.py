catetos = 0
hipotenusa = 0
cont = 0
soma = 0

while True:
    tiro = input().split(',')
    catetos = (float(tiro[0]) ** 2) + (float(tiro[1]) ** 2)
    hipotenusa = catetos ** 0.5
    if hipotenusa > 200:
        break
    print('{:.2f}'.format(hipotenusa))
    cont += 1
    soma += hipotenusa

print('--')
print('num disparos: {}'.format(cont))
print('distancia media: {:.2f}'.format(soma / cont))
