potencia = int(input())
tempo = int(input())

consumo = (potencia / 1000) * (tempo / 60)

print('{:.1f}'.format(consumo), 'kWh')
