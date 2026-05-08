from random import randint, random
M = []

for n_linha in range(15):
    linha = []
    for n_coluna in range(15):
            linha.append(randint(0, 10))
M.append(linha)

for elemento in linha:
    print(linha)