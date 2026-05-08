pares = open("Aula12/ex1_pares.txt","r")
Invertido = open("Aula12/inverido.txt","w")
lista = []
for linha in pares:
    lista.append(linha)

invertido = lista[::-1]

for n in invertido:
    Invertido.write(n)