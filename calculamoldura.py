# gustavoas
# UFCG 2019
# Q19TST

comprimento = float(input())
largura = float(input())

j = (comprimento * 2 / 100) + (largura * 2 / 100)
orcamento = j * 120.0

print('R$ {:.1f}'.format(orcamento))
