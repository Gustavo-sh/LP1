vezes = int(input())
lista = []
antes = 0
depois = 0

for i in range(vezes):
    palavra = input()
    lista.append(palavra)

print('---')
chave = input()

for e in range(len(lista)):
    if lista[e] == chave:
        vezes = 0
    if lista[e] < chave:
        antes += 1
    if lista[e] > chave:
        depois += 1

print('{} antes'.format(antes))
print('{} depois'.format(depois))

