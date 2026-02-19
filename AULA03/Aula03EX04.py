salario = float(input("Digite seu salario"))

if salario <= 1250:
    Nsalario = salario * 1.15
    print(f'Seu salario novo é {Nsalario:.2f}')
else:
    N2salario = salario * 1.1
    print(f'Seu salario novo é {N2salario:.2f}')