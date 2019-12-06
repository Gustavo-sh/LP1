conta = input().split()
valor = float(conta[1])

while True:
    num = input().split()
    if num[0] == '3':
        break
    elif num[0] == '1':
        valor -= float(num[1])
    elif num[0] == '2':
        valor += float(num[1])

print('Saldo de R$ {:.2f} na conta de {}'.format(valor, conta[0]))
