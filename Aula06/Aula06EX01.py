q_n = int(input("Digite a quanidade de numeros a serem testados"))

total_primos = 0

cont= 1

while cont>q_n:
    n = int(input("Digite um numero"))
    if n>1:
        for x in range (2, n):
            if n%x == 0:
                total_primos = total_primos = total_primos + 1
    cont = cont + 1

