# Gustavo
# Questão 5 do tst

valor = float(input('Digite o preço da unidade do tijolo (Em reais): '))
tijolo = float(input('Digite a altura do tijolo (Em metros): '))
c_tijolo = float(input('Digite o comprimento do tijolo (Em metros): '))
parede = float(input('Digite a altura das paredes (Em metros): '))
c_parede = float(input('Digite o comprimento das paredes (Em metros): '))

num_tijolos_altura = parede / tijolo
num_tijolos_comprimento = c_parede / c_tijolo
num_tijolos_totais = num_tijolos_altura * num_tijolos_comprimento
orcamento = valor * num_tijolos_totais

print('O número total de tijolos é {:.1f} e o orçamento final é de R$ {:.1f}'.format(num_tijolos_totais, orcamento))
