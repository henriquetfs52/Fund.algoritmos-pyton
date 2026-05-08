from random import randint, random
M = []
soma = 0
for i in range(12):
    linha = []
    for j in range(12):
        n = randint(0, 10)
        linha.append(n)
        if j > i:
            soma = soma +  n


    M.append(linha)
for linha in M:
    print(*linha)

print(soma)