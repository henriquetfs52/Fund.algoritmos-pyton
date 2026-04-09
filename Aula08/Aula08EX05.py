x = []

for i in range(5):
    n = int(input("Digite um numero"))
    x.append(n)

print(*x[::-1])

