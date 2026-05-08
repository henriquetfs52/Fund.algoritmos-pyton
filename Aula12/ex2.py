Contato = []

def inicio():
    n = int(input("Digite 1 para sair, e 2 adicionar seu contato"))
    if n == 1:
        quit()
    if n ==2:
        pedir_Contato()
    else:
        inicio()




def pedir_Contato():
    Nome = input("Digite seu nome")
    if Nome =="":
        pedir_Contato()
    else:
        Contato.append(Nome)

    Telefone = input("Digite seu numero")
    if Telefone =="":
        pedir_Contato()
    else:
        Contato.append(Telefone)
        
        Contatos = open("Aula12/ex2_contatos.txt","a")
        Contatos.write(f"Nome: {Contato[0]} | Telefone: {Contato[1]}\n")
        Contatos.close()
        
        escolha()


def escolha():
    n = int(input("Seu contato foi adicionado com sucesso, digite 1 para sair, e 2 para pegar contatos"))
    if n == 1:
        quit()
    if n ==2:
        Contatos = open("Aula12/ex2_contatos.txt","r")
        for linha in Contatos:
            print(f"{linha}")

    else:
        escolha()


inicio()