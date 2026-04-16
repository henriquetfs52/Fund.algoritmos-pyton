Inicio = int(input("Deseja se cadastrar, ou logar no serviço da FeiTv? Digite 0 para cadastrar e 1 para logar"))
Login = []
Cad = []
Aplicativo = False
def appendCad():
    Cad.append(Usuário)
    Cad.append(Email)
    Cad.append(Senha)

def appendLog():
    Login.append(Usuário)
    Login.append(Email)
    Login.append(Senha)

def askCad():
    Usuário = input("Digite o seu novo usuário")
    Email = input("Digite o seu email")
    Senha = input("Digite a sua nova senha")

def askLog():
    UsuárioL = input("Digite o seu usuário")
    EmailL = input("Digite o seu email")
    SenhaL = input("Digite a sua senha")

if Inicio == 0:
    askCad()
    appendCad()
    Aplicativo = True


elif Inicio == 1:
    while Aplicativo == False:
        askLog()
        appendLog()
        if Login == Cad:
            print("Você fez o login na sua conta corretamente")
            Aplicativo = True
        else:
            print("Você fez o login na sua conta incorretamente")

else:
    print ("O numero que digitou não é válido")







