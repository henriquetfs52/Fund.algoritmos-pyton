# Lista de login
Login = []

# Lista de cadastro
Cad = []


# Função geral do menu de inicio 
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
            addCadtxt()


        elif Inicio == 1:
        
                askLog()
                appendLog()
                Banco_de_dados = open("ProjetoStreaming/Login.txt","r")
                for linha in Banco_de_dados:
        
                    if linha.split() == Login:
                        print("Você fez login corretamente\n")
                        print("0 - Abrir o aplicativo")
                        print("1 - Sair")
                        Escolha = int(input("Digite sua resposta "))

                        if Escolha ==0:
                            app()
                        if Escolha ==1:
                            quit()
                    
                else:
                    print("Você fez o login na sua conta incorretamente")
                    Login.pop()
                    Login.pop()
                    Login.pop()

        elif Inicio == 2:
            quit()

        else:
            print ("O numero que digitou não é válido")
        


# Faz o append das informações do cadastro para a lista Cad
def appendCad():
    Cad.append(Usuário)
    Cad.append(Email)
    Cad.append(Senha)

# Faz o append das informações do login para a lista Login
def appendLog():
    Login.append(UsuárioL)
    Login.append(EmailL)
    Login.append(SenhaL)

# Função que pede ao usuário, senha e email quando o cadastro esta sendo feito 
def askCad():
    global Usuário
    global Email
    global Senha

    Usuário = str(input("Digite o seu novo usuário: "))
    Email = str(input("Digite o seu email: "))
    Senha = str(input("Digite a sua nova senha: "))


# Função que pede ao usuário, senha e email quando o login esta sendo feito
def askLog():
    global UsuárioL
    global EmailL
    global SenhaL

    UsuárioL = str(input("Digite o seu usuário: "))
    EmailL = str(input("Digite o seu email: "))
    SenhaL = str(input("Digite a sua senha: "))

# Função que adiciona as inforçõees da lista Cad ao arquivo txt Login.txt
def addCadtxt():
    arquivo_login = open("ProjetoStreaming/Login.txt","a", encoding="utf-8")
    arquivo_login.write(f"{Cad[0]} {Cad[1]} {Cad[2]}\n")
    Cad.pop()
    Cad.pop()
    Cad.pop()

# Função com as funções do aplicativo pós menu inicial
def app():
   
        print("FEITV\n")
        print("Aplicativo ligado")
        print("0 - Buscar um Filme")
        print("1 - Gerenciar favoritos")
        print("2 - Deslogar da sua conta")
        escolha = int(input("Digite sua resposta: "))

        if escolha ==0:
           
            buscar_filmes()

        elif escolha ==1:
            print
        elif escolha ==2:
            menu()
        else:
            print("Escolha não valida, tente novamente")


def buscar_filmes():
    
        modo_filme = False

        Catalogo = open("ProjetoStreaming/Catalogo.txt", "r")
                
        print("\nA busca deve ser feita por nome, digite o nome do filme no espaço a seguir")
        Filme  = input("Filme: ")
                
        for linha in Catalogo:
            
            Infos = linha.split("-")
            if Infos[0] == Filme:
                modo_filme=True
                break
            else:
                print("\nO filme não encontra-se em catalalogo, ou teve seu nome digitado incorretamente")
                buscar_filmes()
        
        if modo_filme == True:    
                print("\nO filme encontra-se em catalalogo")
                print("0 - Ver informações sobre o filme")
                print("1 - Apenas adiciona-lo aos favoritos")
                escolha = int(input("Digite sua resposta: "))

                if escolha ==0:
                    print(f"\n{Infos[0]} \n{Infos[1]} \n{Infos[2]} \n{Infos[3]}")
                    
                    Favoritos = open("ProjetoStreaming/Favoritos.txt", "r+")
                    
                    print(f"\n Deseja adicionar {Filme} aos seus favoritos")

                    print("0 - Ver informações sobre o filme")
                    print("1 - Apenas adiciona-lo aos favoritos")
                    escolha = int(input("Digite sua resposta: "))
                    
                    for linha in Favoritos:
                        Lista_Favoritos = linha.split()
                        if Lista_Favoritos[0] == Filme:
                            Fav = "Repetido"
                    if Fav != "Repetido":
                        Favoritos.write(f"{Filme}\n")


                
    


menu()






