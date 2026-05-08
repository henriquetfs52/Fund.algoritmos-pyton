from random import randint

Resultados = {}

def dois_dados():

    soma = 0

    for i in range(2):
        res1 = randint(1, 6)
        soma += res1

    return soma


def mil_dados():

    for i in range(1000):

        n = dois_dados()

        if n in Resultados:
            Resultados[n] += 1

        else:
            Resultados[n] = 1

def frequencia():
    for n in Resultados:
        Resultados[n] = Resultados[n]/10 


mil_dados()

print(Resultados)
frequencia()
print(Resultados)