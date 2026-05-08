from random import randint, random

inteiros = []

for i in range (10):
    inteiros.append(randint(0, 100))

reais = []

for x in range (5):
    reais.append(random()*10)

strings = ["a","b","c"]

completa = []

completa.append(inteiros)
completa.append(reais)
completa.append(strings)

del reais
del inteiros
del strings

for lista in completa:
    print(lista)