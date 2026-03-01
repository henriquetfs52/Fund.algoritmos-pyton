Cod = int(input("Digite o código do produto"))

if Cod == 1:
    print("Alimento não perecível")
elif Cod >= 2 and Cod <= 4:
    print("Alimento perecível")
elif Cod == 5 or Cod == 6:
    print("Vestuário")
elif Cod >= 8 and Cod <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("inválido") 