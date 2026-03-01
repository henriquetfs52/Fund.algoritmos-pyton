C = int(input("Digite seu código de origem"))

if C == 1:
    print("Sul")
elif C == 2:
    print("Norte")
elif C == 3:
    print("Leste")
elif C == 4:
    print("Oeste")
elif C == 5 or C == 6:
    print("Nordeste")
elif C >= 7 and C <= 9:
    print("Sudeste")
elif C>= 10 and C <= 20:
    print("Centro-oeste")
elif C>= 25 and C <= 30:
    print("Nordeste")
else:
    print("Importado")