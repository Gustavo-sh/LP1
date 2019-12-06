num = int(input())
quant = 0

if num != 0:
    while num > 0:
        num = num // 10
        quant += 1
    print(quant)
else:
    print('1')
