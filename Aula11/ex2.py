from random import randint

contador = {}

for i in range(100):
    n = randint(0,20)
    if n in contador:
        contador[n] +=1

    else:
        contador[n] = 1

print(contador)