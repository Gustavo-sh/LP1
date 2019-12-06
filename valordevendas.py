quant = int(input()) + 1
saldo = float(input())

while True:
    operacao = input()
    op = operacao.split()
    if op[0] == 'depósito':
        if float(op[1]) > 1000.00:
            print('Operação inválida: {} {:.2f}.'.format(op[0], float(op[1])))
            break
        else:
            saldo += float(op[1])
    if op[0] == 'saque':
        saldo -= float(op[1])
        quant -= 1
    if str(saldo)[0] == '-':
        print('Operação inválida: {} {:.2f}.'.format(op[0], float(op[1])))
        saldo += float(op[1])
        break
    if quant == 0:
        print('Operação inválida: {} {:.2f}.'.format(op[0], float(op[1])))
        saldo += float(op[1])
        break

print('Seu saldo é R$ {:.2f}.'.format(saldo))
