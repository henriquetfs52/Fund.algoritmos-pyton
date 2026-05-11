# Lista de login
Login = []

# Lista de cadastro
Cad = []


# Função geral do menu de inicio 
def menu():
       while True: 
        global Inicio
    
        print("\n FEITV")
        print("0 - Cadastrar")
        print("1 - Logar")
        print("2 - Sair")

        Inicio = int(input("Digite sua resposta: "))

        #Escolha cadastro
        if Inicio == 0:
            askCad()
            appendCad()
            addCadtxt()
            print('\n Você foi cadastrado com sucesso, agora, faça o Login para entrar no app')

        #Escolha login
        elif Inicio == 1:
            
                askLog()
                appendLog()
                Banco_de_dados = open("Login.txt","r", encoding="utf-8")
                for linha in Banco_de_dados:
        
                    if linha.split() == Login:
                        print(f"\n {Login[0]} Você fez login corretamente!\n")
                        print("0 - Abrir o aplicativo")
                        print("1 - Sair")
                        Escolha = int(input("Digite sua resposta: "))

                        if Escolha ==0:
                            app()
                        if Escolha ==1:
                            quit()
                    
                else:
                    print("Você fez o login na sua conta incorretamente, tente novamente")
                    Login.pop()
                    Login.pop()
                    Login.pop()
        
        #Escolha sair
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
    arquivo_login = open("Login.txt","a", encoding="utf-8")
    arquivo_login.write(f"{Cad[0]} {Cad[1]} {Cad[2]}\n")
    Cad.pop()
    Cad.pop()
    Cad.pop()

# Função com as funções do aplicativo pós menu inicial
def app():
        global Filme
        print("\n FEITV\n")
        print("Aplicativo ligado")
        print("0 - Buscar um Filme")
        print("1 - Gerenciar favoritos")
        print("2 - Abrir o catalogo")
        print("3 - Deslogar da sua conta")
        escolha = int(input("Digite sua resposta: "))

        if escolha ==0:
           
            buscar_filmes()
            app()

        elif escolha ==1:
            gerenciar_fav = True
            print("\n Você acessou o gerenciamento de favoritos")
            while gerenciar_fav:
                print("\n 0 - Sair de gerenciamento de favoritos")
                print("1 - Ver lista de favoritos")
                print("2 - Adicionar favoritos")
                print("3 - Remover favoritos")
                fav_escolha = int(input("Digite sua resposta: "))

                if fav_escolha == 0:
                     app()
                
                if fav_escolha == 1:
                    n = 0
                    print("\n Sua lista de favoritos é:")
                    Favoritos = open("Favoritos.txt", "r+", encoding="utf-8")
                    for linha in Favoritos:

                        Lista_Favoritos = linha.split("-")
                        if Lista_Favoritos[0] == Login[0]:
                             n +=1
                             print(f"\n Filme {n}: {Lista_Favoritos[1]}")
                
                if fav_escolha == 2:
                    print("\n Digite o nome do filme que deseja adicionar aos favoritos")
                    Filme = input("Filme: ")
                    favoritar()
                    app()
                     
                if fav_escolha == 3:
                    remover_favorito()
                    app()
                
        
        elif escolha ==2:
             print("\n Este são os filmes disponiveis no catalogo da FeiTv")
             Catalogo = open("Catalogo.txt", "r", encoding="utf-8")
             for linha in Catalogo:
                  Infos = linha.split("-")
                  print(f"\n {Infos[0]}")
            
             app()

        elif escolha ==3:
            Login.pop()
            Login.pop()
            Login.pop()
            menu()

        else:
            print("Escolha não valida, tente novamente")


def buscar_filmes():

        global Filme
        modo_filme = False
       

        Catalogo = open("Catalogo.txt", "r", encoding="utf-8")
                
        print("\nA busca deve ser feita por nome, digite o nome do filme no espaço a seguir")
        Filme  = input("Filme: ")
                
        for linha in Catalogo:
            
            Infos = linha.split("-")
            if Infos[0] == Filme:
                modo_filme=True
                break
        else:
            print("\nO filme não encontra-se em catalogo, ou teve seu nome digitado incorretamente")
            buscar_filmes()
        
        if modo_filme == True:    
                print("\nO filme encontra-se em catalalogo")
                print("0 - Ver informações sobre o filme")
                print("1 - Apenas adiciona-lo aos favoritos")
                escolha = int(input("Digite sua resposta: "))

                if escolha ==0:
                    print(f"\n{Infos[0]} \n{Infos[1]} \n{Infos[2]} \n{Infos[3]}")
                    modo_filme == False
                    
                    
                    print(f"\n Deseja adicionar {Filme} aos seus favoritos")

                    print("0 - Para adicionar")
                    print("1 - Para não adicionar")
                    add_fav = int(input("Digite sua resposta: "))
                    
                    if add_fav ==0: 
                        favoritar()
                    
                    if add_fav ==1:
                        Filme = " "
                        app()

                if escolha == 1:
                     favoritar()
                    

                        


                
    
def favoritar():
     global Filme
     Favoritos = open("Favoritos.txt", "r+", encoding="utf-8")
     Fav =  " "
     for linha in Favoritos:
        Lista_Favoritos = linha.strip().split("-")
        if Lista_Favoritos[1] == Filme and Login[0] == Lista_Favoritos[0]:
                Fav = "Repetido"
                print("Esse filme já faz parte de seus favoritos")
     if Fav != "Repetido":
            Favoritos.write(f"{Login[0]}-{Filme}\n")
            print(f"\n{Filme} foi adicionado aos seus favoritos")
            Filme = " "

def remover_favorito():

    global Filme

    Favoritos = open("Favoritos.txt", "r", encoding="utf-8")

    linhas = []

    print("\nSeus favoritos:\n")

    for linha in Favoritos:

        Lista_Favoritos = linha.strip().split("-")

        if Lista_Favoritos[0] == Login[0]:

            print(Lista_Favoritos[1])

        linhas.append(linha)

    Favoritos.close()

    Filme = input("\nDigite o nome do filme que deseja remover: ")

    Novo_Favoritos = open("Favoritos.txt", "w", encoding="utf-8")

    for linha in linhas:

        Lista_Favoritos = linha.strip().split("-")

        if not (Lista_Favoritos[0] == Login[0] and Lista_Favoritos[1] == Filme):

            Novo_Favoritos.write(linha)

    Novo_Favoritos.close()

    Filme = ' '

    print("Filme removido dos favoritos")




menu()






