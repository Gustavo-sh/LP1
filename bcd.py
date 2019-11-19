while True:
    sep1 = ''
    sep2 = ''
    binario = input()
    if binario == 'fim': break
    if len(binario) < 8:
        print('Tente novamente.')
        continue
    for e in range(0, 4):
        sep1 += binario[e]
    for e in range(4, 8):
        sep2 += binario[e]
    if int(sep1, 2) > 9 or int(sep2, 2) > 9:
        print('BCD inválido.')
    else:
        print(str(int(sep1, 2)) + str(int(sep2, 2)))
