#FeiTv.py contém exatamente o mesmo código que o FeiTv_v2.py entretanto todas as vezes que um arquivo .txt é chamado, o endereço contém a pasta /ProjetoStreaming, pois o terminal do vscode
#não reconhecia o arquivo normalmente

# Lista de login, sempre contem as informações do usuário quando ele está logado
Login = []

# Lista de cadastro, serve para ser reescrita no aquivo txt, depois é apagada
Cad = []


# Função geral do menu de inicio
def menu():
    while True:
        global Inicio

        print("\n FEITV")
        print("O melhor streaming do terminal do seu computdor!")
        print("Siga as instruções para usar-lo")
        print("0 - Cadastrar")
        print("1 - Logar")
        print("2 - Sair")

        Inicio = int(input("Digite sua resposta: "))

        # Escolha cadastro
        if Inicio == 0:
            askCad()
            appendCad()
            addCadtxt()
            print(f'\nVocê foi cadastrado com sucesso, agora, faça o Login para entrar no app')

        # Escolha login
        elif Inicio == 1:

            askLog()
            appendLog()

            Banco_de_dados = open("ProjetoStreaming/Login.txt", "r", encoding="utf-8")

            # Verifica se os dados digitados existem no banco de dados
            for linha in Banco_de_dados:

                if linha.split() == Login:
                    print(f"\n {Login[0]} Você fez login corretamente!\n")
                    print("0 - Abrir o aplicativo")
                    print("1 - Sair")

                    Escolha = int(input("Digite sua resposta: "))

                    if Escolha == 0:
                        app()

                    if Escolha == 1:
                        quit()

            else:
                print("Você fez o login na sua conta incorretamente, tente novamente")

                Login.pop()
                Login.pop()
                Login.pop()

        # Escolha sair
        elif Inicio == 2:
            quit()

        else:
            print("O numero que digitou não é válido")


# Função com as funções do aplicativo pós menu inicial
def app():

    global Filme

    print("\n FEITV\n")
    print("Aplicativo ligado")
    print("0 - Buscar um Filme")
    print("1 - Gerenciar favoritos")
    print("2 - Abrir o catalogo")
    print("3 - Ver a lista de curtidos")
    print("4 - Deslogar da sua conta")

    escolha = int(input("Digite sua resposta: "))

    # Escolha buscar filmes
    if escolha == 0:

        buscar_filmes()
        app()

    # Gerenciamento de favoritos
    elif escolha == 1:

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

            # Visualização dos favoritos do usuário
            if fav_escolha == 1:

                n = 0

                print("\n Sua lista de favoritos é:")

                Favoritos = open("ProjetoStreaming/Favoritos.txt", "r+", encoding="utf-8")

                for linha in Favoritos:

                    Lista_Favoritos = linha.split("-")

                    if Lista_Favoritos[0] == Login[0]:

                        n += 1

                        print(f"\n Filme {n}: {Lista_Favoritos[1]}")

                # Reprodução dos favoritos
                print(f"\n Deseja reproduzir sua lista de favoritos?")

                print("0 - Reproduzir favoritos")

                print("1 - Não reproduzir")
                fav_reprod = int(input("Digite sua resposta: "))

                if fav_reprod == 0:

                    Favoritos = open("ProjetoStreaming/Favoritos.txt", "r", encoding="utf-8")
                    Catalogo = open("ProjetoStreaming/Catalogo.txt", "r", encoding="utf-8")

                    favoritos_usuario = []

                    # Salva os favoritos do usuário
                    for linha in Favoritos:

                        Lista_Favoritos = linha.strip().split("-")

                        if Lista_Favoritos[0] == Login[0]:

                            favoritos_usuario.append(Lista_Favoritos[1].strip().lower())

                    # Percorre o catálogo e reproduz os favoritos
                    for linha in Catalogo:

                        Lista_Catalogo = linha.strip().split("-")

                        nome_filme = Lista_Catalogo[0].strip().lower()

                        if nome_filme in favoritos_usuario:

                            print(f"\n{Lista_Catalogo[0]}")
                            print(f"{Lista_Catalogo[1]}")
                            print(f"{Lista_Catalogo[2]}")
                            print(f"{Lista_Catalogo[3]}")

                if fav_reprod == 1:
                    app()

            # Adiciona um filme aos favoritos
            if fav_escolha == 2:

                print("\n Digite o nome do filme que deseja adicionar aos favoritos")

                Filme = input("Filme: ").strip().lower()

                favoritar()

                app()

            # Remove um filme dos favoritos
            if fav_escolha == 3:

                remover_favorito()

                app()

    # Abrir o catálogo
    elif escolha == 2:

        print("\n Este são os filmes disponiveis no catalogo da FeiTv")

        Catalogo = open("ProjetoStreaming/Catalogo.txt", "r", encoding="utf-8")

        # Exibe todos os filmes disponíveis
        for linha in Catalogo:

            Infos = linha.split("-")

            print(f"\n {Infos[0]}")

        app()

    # Ver lista de curtidos
    elif escolha == 3:

        Curtidos = open("ProjetoStreaming/Curtidos.txt", "r", encoding="utf-8")

        n = 0

        print("\nEsses são os filmes curtidos por você")

        # Mostra apenas os filmes curtidos do usuário logado
        for linha in Curtidos:

            Lista_Curtidos = linha.split("-")

            if Lista_Curtidos[0] == Login[0]:

                n += 1

                print(f"\nFilme {n}: {Lista_Curtidos[1]}")
        app()

    # Deslogar da conta
    elif escolha == 4:

        # Remove os dados do usuário atual da lista Login
        Login.pop()
        Login.pop()
        Login.pop()

        menu()

    else:
        print("Escolha não valida, tente novamente")


# Aqui começam as funções que executam ações específicas dentro do código

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


# Função que adiciona as informações da lista Cad ao arquivo txt Login.txt
def addCadtxt():

    arquivo_login = open("ProjetoStreaming/Login.txt", "a", encoding="utf-8")

    arquivo_login.write(f"{Cad[0]} {Cad[1]} {Cad[2]}\n")

    # Limpa a lista Cad após salvar os dados
    Cad.pop()
    Cad.pop()
    Cad.pop()


# Função chamada pelo app para buscar um filme diretamente pelo nome
def buscar_filmes():

    global Filme

    modo_filme = False

    Catalogo = open("ProjetoStreaming/Catalogo.txt", "r", encoding="utf-8")

    print("\nA busca deve ser feita por nome, digite o nome do filme no espaço a seguir")

    Filme = input("Filme: ").strip().lower()

    # Procura o filme digitado dentro do catálogo
    for linha in Catalogo:

        Infos = linha.split("-")

        if Infos[0].strip().lower() == Filme:

            modo_filme = True
            break

    else:

        print("\nO filme não encontra-se em catalogo, ou teve seu nome digitado incorretamente")

        buscar_filmes()

    if modo_filme == True:

        print("\nO filme encontra-se em catalogo")

        print("0 - Ver informações sobre o filme")
        print("1 - Apenas adiciona-lo aos favoritos")

        escolha = int(input("Digite sua resposta: "))

        # Ver as informações padrão
        if escolha == 0:

            print(f"\n{Infos[0]} \n{Infos[1]} \n{Infos[2]} \n{Infos[3]}")

            Curtidos = open("ProjetoStreaming/Curtidos.txt", "r+", encoding="utf-8")

            like = False

            # Verifica se o filme já foi curtido
            for linha in Curtidos:

                Lista_Curtidos = linha.strip().split("-")

                if len(Lista_Curtidos) < 2:
                    continue

                if Login[0] == Lista_Curtidos[0] and Filme == Lista_Curtidos[1].lower():
                    like = True

            if like == False:

                print(f"\n Deseja adicionar {Filme.title()} aos seus filmes curtidos?")

                print("0 - Para adicionar")
                print("1 - Para não adicionar")

                add_like = int(input("Digite sua resposta: "))

                if add_like == 0:
                    curtir()

            if like == True:

                print(f"\n Deseja remover {Filme.title()} dos seus filmes curtidos?")

                print("0 - Para remover")
                print("1 - Para não remover")

                remover_like = int(input("Digite sua resposta: "))

                if remover_like == 0:
                    remover_curtida()

            print(f"\n Deseja adicionar {Filme.title()} aos seus favoritos?")

            print("0 - Para adicionar")
            print("1 - Para não adicionar")

            add_fav = int(input("Digite sua resposta: "))

            if add_fav == 0:
                favoritar()

            if add_fav == 1:

                Filme = " "

                app()

        if escolha == 1:

            favoritar()


# Função chamada pelo app na hora de favoritar filmes
def favoritar():

    global Filme

    Favoritos = open("ProjetoStreaming/Favoritos.txt", "r+", encoding="utf-8")

    Fav = " "

    # Verifica se o filme já existe nos favoritos
    for linha in Favoritos:

        Lista_Favoritos = linha.strip().split("-")

        # Ignora linhas vazias ou inválidas
        if len(Lista_Favoritos) < 2:
            continue

        if Lista_Favoritos[1].strip().lower() == Filme and Login[0] == Lista_Favoritos[0]:

            Fav = "Repetido"

            print("Esse filme já faz parte de seus favoritos")

    if Fav != "Repetido":

        Favoritos.write(f"{Login[0]}-{Filme.title()}\n")

        print(f"\n{Filme.title()} foi adicionado aos seus favoritos")

        Filme = " "


# Função chamada pelo app na hora de curtir filmes
def curtir():

    global Filme

    Curtidos = open("ProjetoStreaming/Curtidos.txt", "r+", encoding="utf-8")

    like = " "

    # Verifica se o filme já foi curtido anteriormente
    for linha in Curtidos:

        Lista_Curtidos = linha.strip().split("-")

        # Ignora linhas vazias ou inválidas
        if len(Lista_Curtidos) < 2:
            continue

        if Lista_Curtidos[1].strip().lower() == Filme and Login[0] == Lista_Curtidos[0]:

            like = "Repetido"

            print("Esse filme já faz parte de seus curtidos")

    if like != "Repetido":

        Curtidos.write(f"{Login[0]}-{Filme.title()}\n")

        print(f"\n{Filme.title()} foi adicionado aos seus curtidos")


# Função chamada pelo app na hora de remover um filme dos favoritos
def remover_favorito():

    global Filme

    Favoritos = open("ProjetoStreaming/Favoritos.txt", "r", encoding="utf-8")

    linhas = []

    print("\nSeus favoritos:\n")
    n = 0

    # Exibe os favoritos atuais do usuário
    for linha in Favoritos:

        Lista_Favoritos = linha.strip().split("-")

        if Lista_Favoritos[0] == Login[0]:
            n += 1
            print(f"\nFilme {n}: {Lista_Favoritos[1]}")

        linhas.append(linha)

    Favoritos.close()

    Filme = input("\nDigite o nome do filme que deseja remover: ").strip().lower()

    Novo_Favoritos = open("ProjetoStreaming/Favoritos.txt", "w", encoding="utf-8")

    # Reescreve o arquivo sem o filme removido
    for linha in linhas:

        Lista_Favoritos = linha.strip().split("-")

        if not (Lista_Favoritos[0] == Login[0] and Lista_Favoritos[1].strip().lower() == Filme):

            Novo_Favoritos.write(linha)

    Novo_Favoritos.close()

    print(f"{Filme} removido dos favoritos")

    Filme = ' '


# Função chamada pelo app na hora de remover um filme dos curtidos
def remover_curtida():

    global Filme

    Curtidos = open("ProjetoStreaming/Curtidos.txt", "r", encoding="utf-8")

    linhas = []

    # Salva todas as linhas do arquivo temporariamente
    for linha in Curtidos:

        linhas.append(linha)

    Curtidos.close()

    Novo_Curtidos = open("ProjetoStreaming/Curtidos.txt", "w", encoding="utf-8")

    for linha in linhas:

        Lista_Curtidos = linha.strip().split("-")

        # Ignora linhas inválidas
        if len(Lista_Curtidos) < 2:
            continue

        usuario = Lista_Curtidos[0].strip()
        filme_salvo = Lista_Curtidos[1].strip().lower()

        # Remove apenas o filme curtido atual
        if usuario == Login[0] and filme_salvo == Filme.lower():

            continue

        Novo_Curtidos.write(linha)

    Novo_Curtidos.close()

    print(f"{Filme.title()} removido dos curtidos")


# Chamada original da função menu ao inicio do terminal
menu()