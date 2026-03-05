qn= 0
total= 0
media = 0

while True:
    n = int(input("Digite um numero"))
    if n == 0:
        break
    else:
        total = n + total
        qn = qn + 1
media = total/qn
print(f"{qn}")
print(f"{total}")
print(f"{media}")


