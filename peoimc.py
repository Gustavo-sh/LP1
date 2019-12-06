peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

print('IMC atual = {:.2f}'.format(imc))

# x = float
# if imc < 24.9:
# else imc > 24.9:

pesoideal = (peso * 24.9) / imc

resultado = pesoideal - peso

# ganhar/perder = 'Peso a ser ganho/perdido = {:.2f}'.format(resultado)

print('Peso a ser ganho/perdido = {:.2f}'.format(resultado))
