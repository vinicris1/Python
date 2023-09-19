import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.resizable(0,0)




janela.title('Teste botão')

def teste():
    print("Teste")
    janela.quit()

botao = ttk.Button(janela, text="Clique aqui", command=teste)
botao.pack()




janela.mainloop()
