import math

r = float(input("Digite o raio em metros"))
a = float(input("Digite a altura em metros"))

area = 2*(3.14 * r**2) + (2 * 3.14 * r * a)

nLata = math.ceil(area/15)

if nLata ==1:
    valorL = 50
if nLata ==2:
    valorL = 48
if nLata ==3:
    valorL = 46
if nLata > 3:
    valorL = 45

preco = valorL * nLata

print(f"A quantidade de latas necessárias é {nLata} \n e o valor a ser pago é {preco}")




