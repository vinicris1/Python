import tkinter as tk

# Função chamada quando um botão do tabuleiro é clicado
def clicar_botao(row, col):
    if tabuleiro[row][col] == "":
        tabuleiro[row][col] = jogador_atual
        botoes[row][col].config(text=jogador_atual)
        alterar_jogador()

# Função para alternar o jogador atual
def alterar_jogador():
    global jogador_atual
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"
    label_jogador.config(text=f"Jogador Atual: {jogador_atual}")

# Inicialização do jogo
janela = tk.Tk()
janela.title("Jogo da Velha")

tabuleiro = [["" for _ in range(3)] for _ in range(3)]
jogador_atual = "X"

botoes = [[None, None, None] for _ in range(3)]

# Crie e coloque os botões no tabuleiro
for i in range(3):
    for j in range(3):
        botoes[i][j] = tk.Button(janela, text="", width=10, height=3, command=lambda row=i, col=j: clicar_botao(row, col))
        botoes[i][j].grid(row=i, column=j)

label_jogador = tk.Label(janela, text=f"Jogador Atual: {jogador_atual}")
label_jogador.grid(row=3, columnspan=3)

janela.mainloop()