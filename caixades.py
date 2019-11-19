peso = 0
comb = 0
alt = 0

while True:
    unis = input().split()
    if int(unis[0]) < 0:
        print('dado inconsistente. peso negativo.')
        break
    else:
        peso += 1
    if int(unis[1]) < 0:
        print('dado inconsistente. combustível negativo.')
        break
    else:
        comb += 1
    if int(unis[2]) < 0:
        print('dado inconsistente. altitude negativa.')
        break
    else:
        alt += 1

print('peso: {}'.format(peso))
print('combustível: {}'.format(comb))
print('altitude: {}'.format(alt))
