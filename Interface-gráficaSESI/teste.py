import customtkinter as tk

tk.set_appearance_mode("Dark")

janela = tk.CTk()

janela.title("Vai toma no cu")

janela.geometry("500x500")

janela.configure(fg_color="black")

janela.resizable(width=False, height=False)

colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas, weight=1)
janela.grid_rowconfigure(linhas, weight=1)

texto1 = tk.CTkLabel(janela, text="Bom dia")
texto1.grid(row=6, column=6)

def clique():
    botao1.configure(text=caixa.get())

botao1 = tk.CTkButton(janela, text="Clique aqui", command=clique, width=50,
                      height=30, fg_color="DarkTurquoise", hover_color="CornflowerBlue",
                      text_color="Black")
botao1.grid(row=8, column=6)


caixa = tk.CTkEntry(janela, placeholder_text="Digite seu nome", width=200, height=30)
caixa.grid(row=7, column=6)


janela.mainloop()


