area = float(input())
preco = float(input())
forma = input()

valor = area * preco

if forma == 'vista':
    percent = valor * 0.2
    total = valor - percent
    print('Total: R$ {:.2f}'.format(total))
elif forma == '2x':
    percent = valor * 0.1
    total = valor - percent
    parcelas = total / 2
    print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(total, parcelas))
elif forma == '3x':
    percent = valor * 0.05
    total = valor - percent
    parcelas = total / 3
    print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(total, parcelas))

# Gustavoas 119210741
# UFCG 2019.2
# Questão iptu do tst
