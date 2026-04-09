Homens= 0
mulheres= 0
outros= 0
SalarioHomens= 0
Salariomulheres= 0
Salariooutros= 0
IdadetotalH = 0
IdadetotalM = 0
IdadetotalO = 0
MBaixoS = 0


while True:
    s =input("Digite M para mulher H para homem e O para outro").lower()
    i = int(input("Digite sua idade"))
    salario = int(input("Digite seu salario"))
    if i < 0:
        break
    
    if s == "h":
        Homens= Homens + 1
        SalarioHomens= SalarioHomens + salario
        IdadetotalH = IdadetotalH + i
    elif s == "m":
        mulheres= mulheres + 1
        Salariomulheres= Salariomulheres + salario
        IdadetotalM = IdadetotalM + i
        if salario < 600:
            MBaixoS = MBaixoS + 1
    elif s == "o":
        outros = outros + 1
        Salariooutros = Salariooutros + salario
        IdadetotalO = IdadetotalO + i
mediah = SalarioHomens/Homens
mediam = Salariomulheres/mulheres
mediao = Salariooutros/outros
mediaIh= IdadetotalH/ Homens
mediaIm= IdadetotalM/ mulheres
mediaOm= IdadetotalO/outros

print(f"Quantidade de homens: {Homens} Media salarial: {mediah} Media de idade: {mediaIh}")
print(f"Quantidade de mulheres: {mulheres} Media salarial: {mediam} Media de idade: {mediaIm} Quantidade de mulheres com baixa renda: {MBaixoS} ")
print(f"Quantidade de outros:{outros} Media salarial: {mediao} Media de idade: {mediaOm}")