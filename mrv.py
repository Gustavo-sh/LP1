pos_inicial = float(input('Posição inicial? '))
velocidade_ini = float(input('Velocidade inicial? '))
tempo_desl = float(input('Tempo? '))
aceleracao = float(input('Aceleração? '))

at = aceleracao * tempo_desl
xt = tempo_desl * aceleracao

velocidade_f = velocidade_ini + (xt)
posicao_f = pos_inicial + (velocidade_ini * tempo_desl) + aceleracao * (tempo_desl ** 2) / 2
velocidade_m = velocidade_ini + (at / 2)

print('')
print('Dados da questão')
print('================')
print('   Posição inicial: {:.2f} m'.format(pos_inicial))
print('Velocidade inicial: {:.2f} m/s'.format(velocidade_ini))
print('        Aceleração: {:.2f} m/s2'.format(aceleracao))
print('             Tempo: {:.2f} s'.format(tempo_desl))
print('  Velocidade final: {:.2f} m/s'.format(velocidade_f))
print('  Velocidade média: {:.2f} m/s'.format(velocidade_m))
print('     Posição final: {:.2f} m'.format(posicao_f))

# Gustavoas 119210741
# UFCG 2019.2
# Questão muv do tst
