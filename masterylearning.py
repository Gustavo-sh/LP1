print('Mastery Learning')
print('Cálculo da nota na unidade')
print('')

media = 5
teste = 0
quant = 0
penal = 0.5
notasv = []

nota1 = float(input('Nota? '))
nota2 = float(input('Nota? '))
if nota1 < 5 or nota2 < 5:
  print('Média: 5.0 (cursando)')
  print('Penalização: 0.0')
elif nota1 >= 5 and nota2 >= 5:
  teste += nota1
  notasv.append(nota1)
  teste += nota2
  notasv.append(nota2)
  if nota1 > nota2:
      nottma = nota1
      nottme = nota2
  else: 
      nottma = nota2
      nottme = nota1
  print('Média: {:.1f} (aprovado)'.format(teste/2))
  print('Penalização: 0.0')
  print('')
  print('===')
  print('Notas válidas: {:.1f} e {:.1f}'.format(nottma, nottme))
  print('Média parcial na unidade: {:.1f}'.format(teste/2))
  print('Penalizações: 0.0')
  print('Média final na unidade: {:.1f}'.format((teste/2)))
  exit()

while True:
  if nota1 < 5 and nota2 < 5:
    nota1 = float(input('Nota? '))
    nota2 = float(input('Nota? '))
  if nota1 >= 5:
    teste += nota1
    notasv.append(nota1)
    quant += 1
  if nota2 >= 5:
    teste += nota2
    notasv.append(nota2)
    quant += 1
  if quant == 2:
    print('Média: {:.1f} (aprovado)'.format(teste/2))
    print('Penalização: {:.1f}'.format(penal))
    break
  if quant == 1:
    break
  penal += 0.5

while True:
  if quant == 2:
    break
  print('')
  nota1 = float(input('Nota? '))
  if nota1 >= 5:
    teste += nota1
    notasv.append(nota1)
    print('Média: {:.1f} (aprovado)'.format(teste/2))
    print('Penalização: {:.1f}'.format(penal))
    break
  else:
    print('Média: 5.0 (cursando)')
    print('Penalização: {:.1f}'.format(penal))
  penal += 0.5

nottma = 0
nottme = 0

if notasv[0] > notasv[1]:
    nottma = notasv[0]
    nottme = notasv[1]
else:
    nottma = notasv[1]
    nottme = notasv[0]

print('')
print('===')
print('Notas válidas: {:.1f} e {:.1f}'.format(nottma, nottme))
print('Média parcial na unidade: {:.1f}'.format(teste/2))
print('Penalizações: {:.1f}'.format(penal))
print('Média final na unidade: {:.1f}'.format((teste/2) - penal))
