x = []
maior= -99999999
menor= 99999999
soma = 0
for i in range(8):
    n = int(input("Digite um numero"))
    x.append(n)
    soma = soma + n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

media = soma/10

print(maior)
print(menor)
print(media)