cont=0
ac= 0
n = 0
while True:
    if cont < 10:
        n = int(input("digite um numero"))
        ac = ac + n
        cont = cont +1
    else:
        break

print(f"{ac}")
print(f"{cont}")