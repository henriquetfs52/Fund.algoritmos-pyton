n = int(input("Digite um número inteiro positivo: "))

cont = 1
soma = 0

while cont <= n:
    soma = soma + (1/cont)
    cont = cont + 1

print(f"S = {soma}")