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

texto1 = tk.CTkLabel(janela, text="Calculadora")
texto1.grid(row=2, column=6)

texto2 = tk.CTkLabel(janela, text="")
texto2.grid(row=3, column=6)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite um num", width=120, height=30)
caixa1.grid(row=5, column=4)

caixa2 = tk.CTkEntry(janela, placeholder_text="Digite um num", width=120, height=30)
caixa2.grid(row=5, column=7)

def cliquesoma():
    num1 = int(caixa1.get())
    num2 = int(caixa2.get())

    texto2.configure(text=num1+num2)


def cliquemenos():
    num1 = int(caixa1.get())
    num2 = int(caixa2.get())

    texto2.configure(text=num1 - num2)


def cliquevezes():
    num1 = int(caixa1.get())
    num2 = int(caixa2.get())

    texto2.configure(text=num1 * num2)


def cliquedivide():
    num1 = int(caixa1.get())
    num2 = int(caixa2.get())

    texto2.configure(text=num1 / num2)



botao1 = tk.CTkButton(janela, text="Soma", command=cliquesoma, width=50,
                      height=30, fg_color="DarkTurquoise", hover_color="CornflowerBlue",
                      text_color="Black")
botao1.grid(row=6, column=6)

botao2 = tk.CTkButton(janela, text="Subtração", command=cliquemenos, width=50,
                      height=30, fg_color="DarkTurquoise", hover_color="CornflowerBlue",
                      text_color="Black")
botao2.grid(row=7, column=6)

botao3 = tk.CTkButton(janela, text="Multiplicação", command=cliquevezes, width=50,
                      height=30, fg_color="DarkTurquoise", hover_color="CornflowerBlue",
                      text_color="Black")
botao3.grid(row=8, column=6)

botao4 = tk.CTkButton(janela, text="Divisão", command=cliquedivide, width=50,
                      height=30, fg_color="DarkTurquoise", hover_color="CornflowerBlue",
                      text_color="Black")
botao4.grid(row=9, column=6)

janela.mainloop()