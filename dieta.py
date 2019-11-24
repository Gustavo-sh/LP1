kilos = float(input())
horas = float(input())
quant = float(input())

umkg = 7700
uma_hora = 900
gasto_normal = 2000

cal_perder = kilos * umkg
cal_perd_dia = horas * uma_hora
dif = cal_perd_dia - quant

dias = cal_perder / (gasto_normal + dif)

print('Você precisará de {:.2f} dias de dieta'.format(dias))

# Gustavoas 119210741
# Questão 'dieta' do tst
