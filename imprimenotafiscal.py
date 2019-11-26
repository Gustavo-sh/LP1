# gustavoas
# UFCG 2019
# Q22TST

valor_total = float(input())
data = input()
quantidade_de_produtos = float(input())

media = valor_total / quantidade_de_produtos
print('Data: {}'.format(data))
print('O valor total da compra foi de R$ {:.2f}. A média do preço dos produtos é de {:.1f}.'.format(valor_total, media))
