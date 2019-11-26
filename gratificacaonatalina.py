num = int(input())

if num == 1:
    print('Deverá receber em dezembro R$ 25000.00.')
elif num == 2:
    print('Deverá receber em dezembro R$ 15000.00.')
elif num == 3:
    faltas = int(input())
    tal = (235 - faltas) * 2
    if faltas == 0:
        print('Valor da gratificação R$ 500.00.')
        print('Deverá receber em dezembro R$ 8500.00.')
    else:
        print('Valor da gratificação R$ {:.2f}.'.format(tal))
        print('Deverá receber em dezembro R$ {:.2f}.'.format(8000 + tal))
elif num == 4:
    faltas = int(input())
    tal = (235 - faltas) * 1
    if faltas == 0:
        print('Valor da gratificação R$ 300.00.')
        print('Deverá receber em dezembro R$ 5300.00.')
    else:
        print('Valor da gratificação R$ {:.2f}.'.format(tal))
        print('Deverá receber em dezembro R$ {:.2f}.'.format(5000 + tal))
elif num == 5:
    faltas = int(input())
    tal = (235 - faltas) * 0.7
    if faltas == 0:
        print('Valor da gratificação R$ 200.00.')
        print('Deverá receber em dezembro R$ 3000.00.')
    else:
        print('Valor da gratificação R$ {:.2f}.'.format(tal))
        print('Deverá receber em dezembro R$ {:.2f}.'.format(2800 + tal))
