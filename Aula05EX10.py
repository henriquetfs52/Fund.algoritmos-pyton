cont = 0
Tnota = 0
media = 0
rep = 0
apr = 0

while cont < 80:
    nota = int(input("digite sua nota"))

    if nota < 0 or nota > 10:
        print("Nota inválida")
    
    
    elif nota >= 6:
        apr = apr + 1
        Tnota = Tnota + nota
        cont = cont +1
        
    else:
        rep = rep + 1
        Tnota = Tnota + nota
        cont = cont +1

media = Tnota/cont
print(f"Media {media}, Aprovados {apr}, Reprovados {rep}")
