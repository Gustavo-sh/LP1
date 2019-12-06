quant = int(input()) + 1
saldo = float(input())
um = 'depósito'
dois = 'saque'

while True:
    operacao = input()
    op = operacao.split()
    if op[0] == um:
        if float(op[1]) > 1000.00:
            print('Operação inválida: {}.'.format(operacao))
            break
        else:
            saldo += float(op[1])
    if op[0] == dois:
        saldo -= float(op[1])
        quant = quant - 1
    if str(saldo)[0] == '-':
        print('Operação inválida: {}.'.format(operacao))
        break
    if quant == 0:
        print('Operação inválida: {}.'.format(operacao))
        saldo += float(op[1])
        break

print('Seu saldo é R$ {:.2f}.'.format(saldo))
