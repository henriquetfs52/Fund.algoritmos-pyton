qn= 0
total= 0

while True:
    n = int(input("Digite um numero"))
    if n == 0:
        break
    else:
        total = n + total
        qn = qn + 1


print(f"{total}")
