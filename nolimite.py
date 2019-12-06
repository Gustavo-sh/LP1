lista = []
soma = 0
cont = 0

while True:
    num = input()
    if num != '-':
        lista.append(num)
    else:
        break

limite = float(input())
media = 0
cont2 = 0

for e in range(len(lista)):
    soma += float(lista[e])
    cont += 1
    media = soma / cont
    if media > limite:
        print('media = {:.1f}'.format(media))
        print('num = {}'.format(e + 1))
        cont2 += 1
        break

if cont2 == 0:
    print('limite não alcançado')
