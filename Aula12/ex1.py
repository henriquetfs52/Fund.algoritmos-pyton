pares = open("Aula12/ex1_pares.txt","w")
impares = open("Aula12/ex1_impares.txt","w")

for n in range(999):
    if n%2 == 0:
        pares.write(f"{n}\n")
    else:
        impares.write(f"{n}\n")
pares.close()
impares.close()