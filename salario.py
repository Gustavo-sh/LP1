salario_bruto = float(input())
horas_de_trabalho = int(input())

print('Salário Bruto = {:.2f}'.format(salario_bruto))

hora_bruta = salario_bruto / horas_de_trabalho

print('Hora Bruta = {:.2f}'.format(hora_bruta))

ir = 0.11 * salario_bruto

print('Desconto IR = {:.2f}'.format(ir))

inss = 0.08 * salario_bruto

print('Desconto INSS = {:.2f}'.format(inss))

sind = 0.05 * salario_bruto

print('Desconto Sindicato = {:.2f}'.format(sind))

salario_liquido = salario_bruto - (ir + inss + sind)
hora_liquida = salario_liquido / horas_de_trabalho

print('Salário Líquido = {:.2f}'.format(salario_liquido))

print('Hora Líquida = {:.2f}'.format(hora_liquida))

# Gustavoas 119210741
# UFCG 2019.2
# Questão 27 do TST
# Arigato
