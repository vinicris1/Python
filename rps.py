import tkinter as tk
from tkinter import ttk

play = ""
play2 = ""


def exibir_popup(ganhador):
    popup = tk.Toplevel(janela)
    popup.title("Ganhador")
    
    label = tk.Label(popup, text="{}".format(ganhador))
    label.pack(padx=20, pady=20)
    
    fechar_botao = tk.Button(popup, text="Fechar", command=janela.destroy)
    fechar_botao.pack(padx=20, pady=10)



def versus(): #Correto seria usar match case, que seria o switch case do python
    if play == "" or play2 == "":
        print("Os dois jogadores devem jogar antes de confrontar os resultados")
    else:
        if play == "Rock" and play2 =="Paper":
            ganhador = "Play2 ganhou"
            exibir_popup(ganhador)
        elif play == "Rock" and play2 == "Scissor":
            ganhador = "Play ganhou"
            exibir_popup(ganhador)
        elif play == "Rock" and play2 == "Rock":
            ganhador = "Deu empate :("
            exibir_popup(ganhador)
        elif play == "Paper" and play2 == "Paper":
            ganhador = "Deu empate :("
            exibir_popup(ganhador)
        elif play == "Paper" and play2 == "Scissor":
            ganhador = 'Play2 ganhou'
            exibir_popup(ganhador)
        elif play == "Paper" and play2 == "Rock":
            ganhador = 'Play ganhou'
            exibir_popup(ganhador)
        elif play == "Scissor" and play2 == "Paper":
            ganhador = 'Play ganhou'
            exibir_popup(ganhador)
        elif play == "Scissor" and play2 == "Scissor":
            ganhador = "Deu empate :("
            exibir_popup(ganhador)
        elif play == "Scissor" and play2 == "Rock":
            ganhador = "Play2 ganhou"
            exibir_popup(ganhador)
    

def clicked(botao, botao2, botao3):
    botao.config(state="disabled")
    botao2.config(state="disabled")
    botao3.config(state="disabled")
    
def Rock2():
    global play2 
    play2 = "Rock"
    change_player()
    clicked(RockButton2, PaperButton2, SciButton2)

def Paper2():
    global play2 
    play2 = "Paper"
    change_player()
    clicked(RockButton2, PaperButton2, SciButton2)

def Scissor2():
    global play2 
    play2 = "Scissor"
    change_player()
    clicked(RockButton2, PaperButton2, SciButton2)

def Rock():
    global play
    play = "Rock"
    change_player()
    clicked(RockButton, PaperButton, SciButton)

def Paper():
    global play
    play = "Paper"
    change_player()
    clicked(RockButton, PaperButton, SciButton)
    

def Scissor():
    global play
    play = "Scissor"
    change_player()
    clicked(RockButton, PaperButton, SciButton)

def change_player():
    global current_player
    if current_player == "1":
        current_player = "2"
    else:
        current_player = "1"
    #label_jogador.config(text=f"Jogador Atual: {current_player}")


janela = tk.Tk()

janela.title('Rock paper scissors')

current_player = "1"

RockButton = tk.Button(janela, text="Rock", command=Rock, width=10)
RockButton.grid(row=0, column=0, padx=10, pady=3)

PaperButton = tk.Button(janela, text="Paper", command=Paper, width=10)
PaperButton.grid(row=1, column=0, padx=10, pady=3)

SciButton = tk.Button(janela, text="Scissor", command=Scissor, width=10)
SciButton.grid(row=2, column=0, padx=10, pady=3)


xButton = tk.Button(janela, text="X", command=versus, width=5)
xButton.grid(row=1, column=1, padx=10, pady=3)


RockButton2 = tk.Button(janela, text="Rock", command=Rock2, width=10)
RockButton2.grid(row=0, column=3, padx=10, pady=3)

PaperButton2 = tk.Button(janela, text="Paper", command=Paper2, width=10)
PaperButton2.grid(row=1, column=3, padx=10, pady=3)

SciButton2 = tk.Button(janela, text="Scissor", command=Scissor2, width=10)
SciButton2.grid(row=2, column=3, padx=10, pady=3)


#label_jogador = tk.Label(janela, text=f"Jogador Atual: {current_player}")
#label_jogador.grid(row=3, columnspan=3)


janela.mainloop()