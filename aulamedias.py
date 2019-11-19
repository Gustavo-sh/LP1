soma_conf = 0
quant = 0
lista_num = []
lista_acima = []
lista_abaixo = []

while True:
    num = float(input())
    soma_conf += num
    quant += 1
    lista_num.append(num)
    if soma_conf >= 100:
        break

media = soma_conf / quant

for e in range(len(lista_num)):
    if lista_num[e] > media:
        lista_acima.append(lista_num[e])
        lista_acima.append(e + 1)
    if lista_num[e] < media:
        lista_abaixo.append(lista_num[e])
        lista_abaixo.append(e + 1)

print('Quantidade de números lidos: {}'.format(quant))
print('Soma dos números lidos: {:.2f}'.format(soma_conf))
print('Média = {:.2f}'.format(media))
print('')
print('Abaixo da média')
for e in range(0, len(lista_abaixo), 2):
    print('{:.2f} ({}o)'.format(lista_abaixo[e], lista_abaixo[e + 1]))
print('')
print('Acima da média')
for e in range(0, len(lista_acima), 2):
    print('{:.2f} ({}o)'.format(lista_acima[e], lista_acima[e + 1]))
