I_C = int(input("Digite a idade do seu carro"))

ListaCarros = [carro1, carro2, carro3]

if I_C > 0:
    if I_C >= 3:
            print("Seu carro está velho")
    else:
        print("Seu carro esta novo")
else:
     R1 = int(input("gostaria de coprar um carro então? \n Digite 1 para sim e 0 para não"))
     if R1 == 1:
          for carros in ListaCarros:
            print(carros)
     else: print("Saia do site então")
