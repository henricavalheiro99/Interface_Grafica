import customtkinter as tk
from statistics import mode
lista = []
media = 0
def clicar():
    valor = input1.get()
    lista.append(int(valor))
    print(lista)
def enviar():
    media = sum(lista)/len(lista)
    media = round(media,2)
    lista.sort()
    leng = len(lista)/2
    leng = int(leng)

    medianapar = ((lista[leng])+ (lista[leng-1]))/2
    if len(lista) %2 != 0:
        texto1.configure(text=f'A média é: {media}\nmediana é {lista[leng]}\na moda é: {mode(lista)}')
    else:
        texto1.configure(text=f'A média é: {media}\nmediana é {medianapar}\nmoda é: {mode(lista)}')

tk.set_appearance_mode('Dark')
janela = tk.CTk()
janela.title('Janelinha daora')
janela.geometry('600x600')
janela.configure(fg_color='#333339')
janela.resizable(width=False, height=False)
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)
texto1 = tk.CTkLabel(janela, text='Janelinha daora', font=("Quicksand"'bold',16),text_color='white')
btn1 = tk.CTkButton(janela, text='Aperte',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= clicar)
btn1 = tk.CTkButton(janela, text='Enviar',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= clicar)
btn2 = tk.CTkButton(janela, text='Exibir',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= enviar)
input1 = tk.CTkEntry(janela,placeholder_text='Número 2', text_color='white',width=200, height=35, fg_color='transparent',placeholder_text_color='white',border_color='#f5365f')
input1.grid(row=4,column=5, columnspan=2)
btn1.grid(row=6,column=5)
btn2.grid(row=6,column=6)
texto1.grid(row=3,column=5,columnspan=2)
janela.mainloop()