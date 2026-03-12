N= int(input("Informe a quantidade de linhas"))


for i in range(N):
    for j in range(i):
        if i%2 == 0 or i == 0:
            if j%2 == 0 or j ==0:
              print("#", end=" ")
            else:
              print("%", end=" ")  
        else:
            if j%2 == 0 or j== 0:
              print("&", end=" ")
            else:
              print("$", end=" ") 
  
    print()
        