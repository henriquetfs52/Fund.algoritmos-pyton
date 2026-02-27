kms = int(input("Digite a distância a ser percorida"))

if kms <= 200:
    preco = kms * 0.5
else:
    preco = kms * 0.45


print(f"O preço a se pagar é {preco}")
