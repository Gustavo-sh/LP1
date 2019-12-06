lista = []

for e in range(12):
    spl = input().split()
    fnl = float(spl[0]) - float(spl[1])
    fnl1 = str(fnl)
    lista.append(fnl1)

if lista[0][0] != '-':
    print('jan  {:.1f}'.format(float(lista[0])))
else:
    print('jan {:.1f}'.format(float(lista[0])))

if lista[1][0] != '-':
    print('fev  {:.1f}'.format(float(lista[1])))
else:
    print('fev {:.1f}'.format(float(lista[1])))

if lista[2][0] != '-':
    print('mar  {:.1f}'.format(float(lista[2])))
else:
    print('mar {:.1f}'.format(float(lista[2])))

if lista[3][0] != '-':
    print('abr  {:.1f}'.format(float(lista[3])))
else:
    print('abr {:.1f}'.format(float(lista[3])))

if lista[4][0] != '-':
    print('mai  {:.1f}'.format(float(lista[4])))
else:
    print('mai {:.1f}'.format(float(lista[4])))

if lista[5][0] != '-':
    print('jun  {:.1f}'.format(float(lista[5])))
else:
    print('jun {:.1f}'.format(float(lista[5])))

if lista[6][0] != '-':
    print('jul  {:.1f}'.format(float(lista[6])))
else:
    print('jul {:.1f}'.format(float(lista[6])))

if lista[7][0] != '-':
    print('ago  {:.1f}'.format(float(lista[7])))
else:
    print('ago {:.1f}'.format(float(lista[7])))

if lista[8][0] != '-':
    print('set  {:.1f}'.format(float(lista[8])))
else:
    print('set {:.1f}'.format(float(lista[8])))

if lista[9][0] != '-':
    print('out  {:.1f}'.format(float(lista[9])))
else:
    print('out {:.1f}'.format(float(lista[9])))

if lista[10][0] != '-':
    print('nov  {:.1f}'.format(float(lista[10])))
else:
    print('nov {:.1f}'.format(float(lista[10])))

if lista[11][0] != '-':
    print('dez  {:.1f}'.format(float(lista[11])))
else:
    print('dez {:.1f}'.format(float(lista[11])))

# Gustavoas 119210741
# UFCG 2019.2
