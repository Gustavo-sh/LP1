import math

angulo = float(input())
salto = float(input())
vezes = int(input())

print('|Angulo|   Seno|Cosseno|')

for e in range(vezes):
    ant = math.radians(angulo)
    seno = math.sin(ant)
    cosseno = math.cos(ant)
    if angulo <= 10:
        esp = '   '
    elif angulo <= 100:
        esp = '  '
    else:
        esp = ' '
    for e in range(1):
        if angulo <= 90:
            print('|{}{:.1f}|{:.5f}|{:.5f}|'.format(esp, angulo, seno, cosseno))
            break
        elif angulo > 90 and angulo <= 180:
            print('|{}{:.1f}|{:.5f}|{:.4f}|'.format(esp, angulo, seno, cosseno))
            break
        elif angulo > 180 and angulo <= 270:
            print('|{}{:.1f}|{:.4f}|{:.4f}|'.format(esp, angulo, seno, cosseno))
            break
        elif angulo > 270 and angulo <= 360:
            print('|{}{:.1f}|{:.4f}|{:.5f}|'.format(esp, angulo, seno, cosseno))
            break
    angulo += salto

