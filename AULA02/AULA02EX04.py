HorasTrab = float(input("Digite a quantidade de horas trabalhadas")) 
HorasVal = float(input("Digite o valor da hora trabalhada"))

SalarioBruto = HorasTrab * HorasVal

IR = SalarioBruto * 0.11
INSS = SalarioBruto * 0.08
SIND = SalarioBruto * 0.05

Salario = SalarioBruto - (IR + INSS + SIND)

print (f"Seu salario bruto é = {SalarioBruto} \n Desconto IR {IR} \n Desconto INSS {INSS} \n Desconto Sindicato {SIND} \n Seu salario apos descontos é = {Salario}")
