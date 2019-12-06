# Gustavoas
# Q17TST

print('== Estágio 1 ==')

peso1 = float(input('Peso? '))
nota1 = float(input('Nota? '))

print('== Estágio 2 ==')

peso2 = float(input('Peso? '))
nota2 = float(input('Nota? '))

print('== Estágio 3 ==')

peso3 = float(input('Peso? '))
nota3 = float(input('Nota? '))

print('== Resultados ==')

mediaP = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / 1.0
n_final5 = abs((mediaP * 0.6 - 5.0)) / 0.4
n_final7 = abs((mediaP * 0.6 - 7.0)) / 0.4

print('Média parcial: {:.1f}'.format(mediaP))
print('Nota na final, pra média 5.0 = {:.1f}'.format(n_final5))
print('Nota na final, pra média 7.0 = {:.1f}'.format(n_final7))
