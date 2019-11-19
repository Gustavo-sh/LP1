def somar(a,b):
    soma = a + b
    return soma
def subtrair(a,b):
    subtracao = a - b
    return subtracao
def multiplicacao(a,b):
    multi = a * b
    return multi
def divisao(a,b):
    div = a // b
    return div
while True:
    seq = input().split()
    if seq[0] == '5': break
    if seq[0] == '1': print(somar(int(seq[1]),int(seq[2])))
    elif seq[0] == '2': print(subtrair(int(seq[1]),int(seq[2])))
    elif seq[0] == '3': print(multiplicacao(int(seq[1]),int(seq[2])))
    else:
        if int(seq[2]) != 0:
            print(divisao(int(seq[1]),int(seq[2])))
        else:
            print('Erro: Divisão por 0')
            break
