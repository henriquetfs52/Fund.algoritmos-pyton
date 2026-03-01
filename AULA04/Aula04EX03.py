a = float(input("Digite sua altura:"))

s = input("Você se denomina homem ou mulher").lower()

if s == "homem":
    x = (72.7 * a) - 58
    print(f"sua peso ideal é igual {x}")
elif s == "mulher":
    y = (62.1 * a) - 44.7
    print(f"sua peso ideal é igual {y}")

