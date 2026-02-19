N = int(input("Digite seu ano de nascimento"))
A = int(input("Digite o ano atual"))
I = A - N

if I >= 18:
    print("Voce esta habilitado para a CNH")
else:
    print("Voce não esta habilitado para a CNH")