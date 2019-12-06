cre = float(input())
exp = int(input())
nota = float(input())

if cre < 7 and exp < 6:
    print('Candidato eliminado. CRE e experiência abaixo do limite.')

elif cre < 7 and exp >= 6:
    print('Candidato eliminado. CRE abaixo do limite.')

elif cre >= 7 and exp < 6:
    print('Candidato eliminado. Experiência abaixo do limite.')

elif cre >= 7 and exp >= 6 and nota > 3:
    print('Candidato aprovado.')

else:
    print('Candidato classificado.')

# Gustavoas 119210741
# UFC 2019.2
# Questão 'selecaoprojeto' do tst
