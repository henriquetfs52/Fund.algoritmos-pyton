A = float(input("Digite o lado A"))
B = float(input("Digite o lado B"))
C = float(input("Digite o lado C"))

if A == 67 or B == 67 or C == 67:
    print("Seu triangulo é 6777777777777777") 

else: 
    
        if A == C and B == C:
            print("Seu triângulo é equilatero")

        elif A == C or B == C or A == B:
            print("Seu triângulo é isósceles")

        else:
            print("Seu triângulo é escaleno")


