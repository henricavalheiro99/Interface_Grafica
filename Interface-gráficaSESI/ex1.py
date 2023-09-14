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

texto1 = tk.CTkLabel(janela, text="Descubra o maior número")
texto1.grid(row=2, column=6)

texto2 = tk.CTkLabel(janela, text="")
texto2.grid(row=3, column=6)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite um número", width=120, height=30)
caixa1.grid(row=5, column=4)

caixa2 = tk.CTkEntry(janela, placeholder_text="Digite um número", width=120, height=30)
caixa2.grid(row=5, column=7)

def clique():
    if (caixa1.get() > caixa2.get()):
        texto2.configure(text=caixa1.get() + " é maior")
    elif (caixa1.get() == caixa2.get()):
        texto2.configure(text="São iguais")
    else:
        texto2.configure(text=caixa2.get() + " é maior")


botao1 = tk.CTkButton(janela, text="Clique aqui", command=clique, width=50,
                      height=30, fg_color="DarkTurquoise", hover_color="CornflowerBlue",
                      text_color="Black")
botao1.grid(row=6, column=6)







janela.mainloop()