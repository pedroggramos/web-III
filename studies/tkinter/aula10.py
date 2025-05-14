from tkinter import *

def abrir_janela():
    nova_janela = Toplevel()
    nova_janela.title("Janela Secundária")
    nova_janela.geometry("400x400")
    label = Label(nova_janela, text="Nova janela").pack()

r = Tk()
r.title("Aula 10")
r.geometry("400x400")
r['bg']= 'aquamarine'

x = Menu(r)

arquivoMenu = Menu(x, tearoff=0)

arquivoMenu.add_command(label='Novo')
arquivoMenu.add_command(label='Abrir', command=abrir_janela)
arquivoMenu.add_command(label='Salvar')
arquivoMenu.add_command(label='Sair')

x.add_cascade(label='Arquivo', menu=arquivoMenu)
r.config(menu=x)

button = Button(r, text="Abrir nova janela", command=abrir_janela)
button.pack(pady=20)



# r = Tk()
# r.title("Janela Principal")
# r.geometry("400x400")
# button = Button(r, text="Abrir nova janela", command=abrir_janela).pack()



r.mainloop()