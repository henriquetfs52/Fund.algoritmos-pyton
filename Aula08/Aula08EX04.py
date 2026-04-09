x = []
par = 0
impar = 0
for i in range(10):
    n = int(input("Digite um numero"))
    if n%2==0:
        par = par + n
    else:
        impar = impar + n
    x.append(n)

print(*x)
print(par)
print(impar)

