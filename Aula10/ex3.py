M = []
for i in range(3):
    linha = []
    for x in range(3):
        n = int(input("Digite um numero"))
        linha.append(n)
    M.append(linha)


soma = M[0][0] + M[1][1] + M[2][2]
for linha in M:
    print(*linha)
print(f"soma:{soma}")