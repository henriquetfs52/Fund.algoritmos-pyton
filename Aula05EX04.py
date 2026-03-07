maior = -9999999

for i in range(6):
    num = int(input("Digite um número inteiro positivo: "))
    
    if num > maior:
        maior = num

print(f"O maior número lido foi: {maior}")