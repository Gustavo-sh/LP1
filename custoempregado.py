salario_bruto = float(input())
dias_trabalhados = float(input())
custo_transporte = float(input())

custo = dias_trabalhados * custo_transporte

gastos_transporte = (custo  / salario_bruto) * 100

fgts = (salario_bruto / 100) * 8
inss = (salario_bruto / 100) * 12
desconto_transporte = (salario_bruto / 100) * 6

if salario_bruto <= 1317.07:
    inss_do_empregado = (salario_bruto / 100) * 8

elif salario_bruto >= 1317.08 and salario_bruto <= 2195.12:
    inss_do_empregado = (salario_bruto / 100) * 9

elif salario_bruto >= 2195.13:
    inss_do_empregado = (salario_bruto / 100) * 11

if gastos_transporte > 6:
    valor = gastos_transporte - 6
    valor_desconto = (salario_bruto / 100) * valor
    total = valor_desconto + fgts + inss + salario_bruto
    salario_liquido = salario_bruto - (desconto_transporte + inss_do_empregado)

elif gastos_transporte < 6:
    gasto_extra = (salario_bruto / 100) * gastos_transporte
    salario_liquido = salario_bruto - (gasto_extra + inss_do_empregado)
    total = fgts + inss + salario_bruto

print('salário bruto = R$ {:.2f}'.format(salario_bruto))
print('custo mensal = R$ {:.2f}'.format(total))
print('salário líquido = R$ {:.2f}'.format(salario_liquido))

# Gustavoas 119210741
# UFCG 2019.2
# Questão 'custoempregado' do tst
