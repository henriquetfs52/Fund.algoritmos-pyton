pares = open("Aula12/ex1_pares.txt","r")
paresM4 = open("Aula12/ex1_multiplos_de_quatro","a")

for linha in pares:
    n = int(linha)
    if n%4==0:
        n = str(f"{n}")
        paresM4.write(f"{n}\n")
