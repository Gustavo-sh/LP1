d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

total = d1 + d2 + d3 + d4 + d5
media = (d1 + d2 + d3 + d4 + d5) / 5
porcentagem = (total / 7200) * 100
eps = total // 50

print('Você perdeu {} min na semana (média de {:.1f} min por dia).'.format(total, media))
print('Isso significa {:.2f}% da sua semana produtiva.'.format(porcentagem))
print('Daria para assistir {:01d} episódio(s) de House.'.format(eps))

# Gustavoas 119210741
# UFCG 2019.2
    # Questão 'perdadetemponotransito' do tst
