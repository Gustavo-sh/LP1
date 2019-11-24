numero = int(input())

if numero != 0:
    while numero > 0:
        print(numero % 10)
        numero = numero // 10
else:
    print('0')
