test = 0
media = 0
quant = 0

while True:
    value = float(input())
    if value >= media:
        quant += 1
        test += value
        media = test / quant
    else:
        print('Saldo total do FIS: R${:.2f}.'.format(test))
        print('Média das contribuições: R${:.2f}.'.format(test / quant))
        break
