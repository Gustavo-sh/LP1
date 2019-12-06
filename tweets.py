paginas = int(input())

quant = paginas // 400

resto = paginas % 400

percent = (resto / paginas) * 100

print('Serão necessárias {} página(s) para visualizar os tweets.'.format(quant))

print('{:.1f}% dos tweets serão perdidos.'.format(percent))

# Gustavoas 119210741
# Questão tsete.
