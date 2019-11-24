seq = input()
seq2 = seq.split()
teste = 0
teste2 = 0

if int(seq2[0]) % 2 == 1:
    for e in range(1, len(seq2)):
        if int(seq2[e]) % 2 == 0:
            for i in range(e, len(seq2)):
                if int(seq2[i]) % 2 == 1:
                    print('erro')
                    teste += 1
                    break
    if teste == 0:
        print('ok')

elif int(seq2[0]) % 2 == 0:
    for e in range(1, len(seq2)):
        if int(seq2[e]) % 2 == 1:
            print('erro')
            teste2 += 1
            break
    if teste2 == 0:
        print('ok')

