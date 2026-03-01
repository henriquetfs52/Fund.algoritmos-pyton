mes_atual = 3
ano_atual = 2026
dia_atual = 2

A, B, C = map(int, input("Digite seu ano, mês e dia de nascimento, nessa ordem").split())
if B > mes_atual and C > dia_atual:
    I = (ano_atual - 1) - A
else:
    I = ano_atual - A    
    
    if I >= 18:
        print("Você está apto a votar e dirigir")
    elif I >= 16:
        print("Você etsá apto a votar")
    else:
        print("Você não está apto a nada")
