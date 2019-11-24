n = int(input())
palavra = input().split()
cont = 0

for e in range(len(palavra)):
    if int(palavra[e]) == n:
        print('sim')
        break
    elif palavra[e] != n:
        cont += 1
    if cont == len(palavra):
        print('não')
