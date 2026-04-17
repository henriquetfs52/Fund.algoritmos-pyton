
def menu():
       while True: 
        global Inicio
        print("FEITV")
        print("0 - Cadastrar")
        print("1 - Logar")
        print("2 - Sair")

        Inicio = int(input("Digite sua resposta "))

        if Inicio == 0:
            askCad()
            appendCad()
            Aplicativo = True


        elif Inicio == 1:
        
                askLog()
                appendLog()
                if Login == Cad:
                    print(f"Olá {Usuário}, você fez o login na sua conta corretamente")
                    Aplicativo = True
                else:
                    print("Você fez o login na sua conta incorretamente")
                    Login.pop()
                    Login.pop()
                    Login.pop()

        elif Inicio == 2:
            break

        else:
            print ("O numero que digitou não é válido")
        


Login = []
Cad = []
Catalogo = ["FilmeA","FilmeA"]
Favoritos = []
Aplicativo = False
def appendCad():
    Cad.append(Usuário)
    Cad.append(Email)
    Cad.append(Senha)

def appendLog():
    Login.append(UsuárioL)
    Login.append(EmailL)
    Login.append(SenhaL)

        

def askCad():
    global Usuário
    global Email
    global Senha

    Usuário = str(input("Digite o seu novo usuário: "))
    Email = str(input("Digite o seu email: "))
    Senha = str(input("Digite a sua nova senha: "))

def askLog():
    global UsuárioL
    global EmailL
    global SenhaL

    UsuárioL = str(input("Digite o seu usuário: "))
    EmailL = str(input("Digite o seu email: "))
    SenhaL = str(input("Digite a sua senha: "))



menu()






