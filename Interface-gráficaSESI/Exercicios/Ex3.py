import customtkinter as tk

tk.set_appearance_mode("Dark")

janela = tk.CTk()

janela.title("Ex1")

janela.geometry("500x400")

janela.configure(fg_color="black")

janela.resizable(width=False, height=False)

colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas, weight=1)
janela.grid_rowconfigure(linhas, weight=1)

def clique():
    ValornumPrestacoes = int(numPrestacoes.get())
    Valorcompra = int(compra.get())

    resposta = Valorcompra / ValornumPrestacoes

    if resposta < 500:
        texto2.configure(text="Pode pagar")
    else:
        texto2.configure(text="Não pode pagar")

texto1 = tk.CTkLabel(janela, text="Valor da compra")
texto1.grid(row=2, column=6)

texto2 = tk.CTkLabel(janela, text="")
texto2.grid(row=3, column=6)

compra = tk.CTkEntry(janela, placeholder_text="Compra", width=120, height=30)
compra.grid(row=5, column=4)

numPrestacoes = tk.CTkEntry(janela, placeholder_text="Prestação", width=120, height=30)
numPrestacoes.grid(row=5, column=7)




botao1 = tk.CTkButton(janela, text="Clique aqui", command=clique, width=50,
                      height=30, fg_color="DarkTurquoise", hover_color="CornflowerBlue",
                      text_color="Black")
botao1.grid(row=6, column=6)

janela.mainloop()