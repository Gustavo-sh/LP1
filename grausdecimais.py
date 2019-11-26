graus = int(input())
minutos = int(input())
segundos = int(input())

grausD = graus + ((minutos / 60) + (segundos / 3600))

print('graus = {:.4f}'.format(grausD))
