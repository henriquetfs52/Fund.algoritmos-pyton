from random import randint, random

M = []

for i in range(10):
    linha = []
    for j in range(5):
        linha.append(randint(0, 10))
    M.append(linha)


T = []

for i in range(5):
    linha=[]
    for j in range(10):
        linha.append(M[j][i])
    T.append(linha)

for linha in M:
    print(*linha)

for linha in T:
    print(*linha)