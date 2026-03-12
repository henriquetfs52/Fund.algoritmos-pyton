N= int(input("Informe a quantidade de linhas"))


for i in range(N):
    for j in range(i):
        print("$", end=" ")
    for j in range(N-i):
        print("@", end=" ")
    print()
        
