Dicionario = {
    1: 10,
    2: 20,
    3: 10
}

def busca_chave():
    lista = []
    n = int(input("Digite o valor para buscar a chave"))
    for chave in Dicionario:
        
        if Dicionario[chave]== n:
            lista.append(chave)

    return lista

print(busca_chave())


