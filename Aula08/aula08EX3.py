x = []
mvalor = -999999
mI = -1
for i in range(10):
    n = float(input("Digite um n"))
    x.append(n)
    if n > mvalor:
        mvalor = n

for i in range(len(x)):
    if x[i] > mI:
        mI = i

print(mvalor)
print(mI)