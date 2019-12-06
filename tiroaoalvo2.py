lista = []
num = 0
melhor =  0
media = 0

while True:
    num1 = float(input())
    num2 = float(input())
    catetos = num1 ** 2 + num2 ** 2
    hipotenusa = catetos ** 0.5
    if hipotenusa > 200: break
    lista.append(hipotenusa)
    menor = lista[0]
    num += 1
    media += hipotenusa
    for e in range(len(lista)):
        if lista[e] < menor:
            menor = lista[e]
    if hipotenusa <= menor:
        print('{:.2f} cm (melhor tiro)'.format(hipotenusa))
        melhor = hipotenusa
    else:
        print('{:.2f} cm'.format(hipotenusa))

print('--')
print('num tiros: {}'.format(num))
print('melhor tiro: {:.2f} cm'.format(melhor))
print('distancia media: {:.2f} cm'.format(media / num))
