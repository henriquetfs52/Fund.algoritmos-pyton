M =  []
impares = []
for i in range (4):
    linha = []
    for j in range(4):
        n = int(input("Digite um numero"))
        linha.append(n)
        if n%2 != 0:
            impares.append(n)
        
    M.append(linha)

for linha in M:
    print(*linha)
print(f"impares:{impares}")
