print('Análise da Turma\n===')

aprovados = int(input('Número de aprovados? '))
reprovados = int(input('Número de reprovados? '))

print('---')

total_al = aprovados + reprovados
p_aprovados = (aprovados / total_al) * 100
p_reprovados = (reprovados / total_al) * 100

print('Total de alunos na turma: {}'.format(total_al))
print('Aprovados: {} = {:.1f}%'.format(aprovados, p_aprovados))
print('Reprovados: {} = {:.1f}%'.format(reprovados, p_reprovados))

# Gustavoas 119210741
# UFCG 2019
# Questão 26 TST
# Arigato
