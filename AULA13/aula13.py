from tkinter import *

 #cria a janela
janela = Tk()

 # titulo para a janela
janela.title("Algoritmos")

 #configura o tamanho da janela
janela.geometry("400x400")

rotulo = Label(janela, text="Ronaldo", font=("Arial Bold", 14))
rotulo.place(x=200, y=100, anchor="center")

bx = 0
by = 200

def resenha ():
    while bx < 1000:
        bx = bx+1

botao = Button(janela, text="Clique")
botao.place (bx, by, anchor="center")
 #chama a funcao mainloop:
 #loop infinito para manter a janela aberta
janela.mainloop()
resenha()