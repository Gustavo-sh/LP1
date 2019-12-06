nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
# ponderacao1 = nota1 * 0.2
# ponderacao2 = nota2 * 0.5
peso1 = float(input())
peso2 = float(input())
peso3 = 100 - (peso1 + peso2)

print("Média Final: %.1f" % ((nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / 100))
