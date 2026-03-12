N = int(input("digite um número"))
cont= 0

while N>=0:
    cont= cont +1
    N = N - (10**cont)

print(f"{cont}")