# from tkinter import *
#
#
# i = Tk() # cria a instancia da janela
# i.title('Primeira Janela') #inserir titulo na janela
# i.geometry('600x400')
# # i.wm_iconbitmap('file.ico') # inserir icone na janela
# # i.resizable(0,0) #para bloquear o redimensionamento, pode ser true ou false ou 0 ou 1
# # i.state('zoomed')#abre a janela em tela cheia
# # i.state('iconic')#abre janela minimizada na barra de tarefas
# i.minsize(300,200)#menor tamanho da janela
# i.maxsize(900,600)#maior tamanho da janela
# i['bg'] = 'aquamarine' #cor de fundo da janela

# Entry() - cria uma caixa de entrada na janela ---------------------------

# e = Entry(i).pack()
# e.pack()
# e = Entry(i)
# e.pack

# Button() - cria um botão na janela ------------------

# btn = Button(i, text='Sair', font='Arial 15 bold').pack(pady=5)
# btn = Button(i,text='Sair', font='Arial 12 bold', command=i.destroy).pack(pady=5)

# ---------------------------------------------------------------------


# def botao_clicado():
#     label1.config(text='Olá, você clicou no botão!')
#
# btn1 = Button(i,
#               text='Clique Aqui',
#               font='Helvica 12 bold',
#               fg='blue',
#               bg='#4CAF50',
#               relief='ridge',
#               bd = 5,
#               padx = 20,
#               pady = 10,
#               activeforeground='yellow',
#               activebackground='red',
#               command=botao_clicado
#               ).pack(pady=20)
#
#
# label1 = Label(i,
#                font = 'Verdana 12 bold',
#                fg = 'white',#cor da fonte
#                bg = 'purple',#cor de fundo
#                relief = 'raised',#flat,raised,suken,groove,double,solid
#                bd = 5, #tamanho da borda
#                padx = 30, #espaço na horizontal
#                pady = 10,#espaço na vertical
#                width= 20 #largura do label
#                )
# label1.pack(pady=10)

# sistema grid(linha, coluna) -----------------------

# x1 = Label(i,text='Teste1',font='Arial 20',bg ='blue')
# x2 = Label(i,text='Teste2',font='Arial 20',bg ='red')
# x3 = Label(i,text='Teste3',font='Arial 20',bg ='pink')

# x1.grid(row=0, column=0)
# x2.grid(row=0, column=1)
# x3.grid(row=0, column=2)

# x1.grid(row=0, column=0)
# x2.grid(row=1, column=1)
# x3.grid(row=2, column=2)

# outro exemplo de grid -----------------------------------------
#
# l_nome=Label(i, text='Nome: ', bg='aquamarine')
# l_nome.grid(row=0, column=0, padx=10, pady=10)
#
# e_nome=Entry(i)
# e_nome.grid(row=0, column=1, padx=10, pady=10)
#
# l_idade=Label(i, text='Idade: ', bg='aquamarine')
# l_idade.grid(row=1, column=0, padx=10,pady=10)
#
# e_idade=Entry(i)
# e_idade.grid(row=1, column=1, padx=10,pady=10)
#
# def mostrar_informacoes():
#     nome=e_nome.get()
#     idade=e_idade.get()
#     resultado_label.config(text=f'Nome: {nome}, \nIdade: {idade}')
#
# btn = Button(i, text='Mostrar', font='Arial 10',
#              command=mostrar_informacoes)
#
# btn.grid(row=2,column=0, padx=10,pady=0)
#
# resultado_label = Label(i, text='Nome e idade: ', bg='aquamarine')
# resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


# ---------------------------------------
# Checkbutton() - seleção múltipla ----------------------------------------

# t = Label(i, text='Escolha o seu esporte favorito', bg='aquamarine')
# a1 = Checkbutton(i, text='Futebol', bg='aquamarine')
# a2 = Checkbutton(i, text='Volei', bg='aquamarine')
# a3 = Checkbutton(i, text='Natação', bg='aquamarine')
# a4 = Checkbutton(i, text='Tenis', bg='aquamarine')
# a5 = Checkbutton(i, text='Basquete', bg='aquamarine')
# a6 = Checkbutton(i, text='Surf', bg='aquamarine')
#
# t.place(x = 10, y = 10) #elemento t
# a1.place(x=5, y=30) #elemento a1
# a2.place(x=100, y=30) #elemento a2
# a3.place(x=5, y=70) #elemento a3, ajustado para não se sobrepor ao t
# a4.place(x=100, y=70) #elemento a4, ajustado para não se sobrepor ao a1
# a5.place(x=5, y=110) #elemento a5, ajustado para não se sobrepor ao a3
# a6.place(x=100, y= 110) #elemento a6, ajustado pata ficar abaixo de a5

# Outro exemplo ----------------------------------------

#
# def mostrar_selecionados():
#     selecionados = []
#     if futebol_var.get():
#         selecionados.append('Futebol')
#     if volei_var.get():
#         selecionados.append('Volei')
#     if basquete_var.get():
#         selecionados.append('Basquete')
#     if natacao_var.get():
#         selecionados.append('Natacao')
#     if tenis_var.get():
#         selecionados.append('Tenis')
#     resultado_label.config(text="Esporte(s) selecionados(s): "+",\n".join(selecionados))
#
# futebol_var = IntVar()
# volei_var = IntVar()
# basquete_var = IntVar()
# natacao_var = IntVar()
# tenis_var= IntVar()
#
# futebol = Checkbutton(i, text='Futebol', variable=futebol_var)
# volei = Checkbutton(i, text='Volei', variable=volei_var)
# basquete = Checkbutton(i, text='Basquete', variable=basquete_var)
# natacao = Checkbutton(i, text='Natacao', variable=natacao_var)
# tenis = Checkbutton(i, text='Tenis', variable=tenis_var)
#
# futebol.grid(row=0, column=0, padx=10, pady=0)
# volei.grid(row=1, column=0, padx=10, pady=5)
# basquete.grid(row=2, column=0, padx=10, pady=5)
# natacao.grid(row=3, column=0, padx=10, pady=5)
# tenis.grid(row=4, column=0, padx=10, pady=5)
#
# mostrar_button = Button(i, text='Mostrar Selecionados',
#                         command=mostrar_selecionados)
# mostrar_button.grid(row=5, column=0, pady=20)
#
# resultado_label = Label(i, text='Esporte Selecionados: Nenhum')
# resultado_label.grid(row=6, column=0,pady=20, padx=20)


# Radiobutton() - seleção simples --------------------------------------------

# var = IntVar()
#
# r1 = Radiobutton(i, text='Futebol', variable=var, value=1, bg='aquamarine')
# r2 = Radiobutton(i, text='Volei', variable=var, value=2, bg='aquamarine')
# r3 = Radiobutton(i, text='Basquete', variable=var, value=3, bg='aquamarine')
#
# r1.place(x=10, y=10)
# r2.place(x=100, y=10)
# r3.place(x=200, y=10)

# listbox() - criar uma lista ----------------------------------------------

# lista = Listbox(i)
# lista.insert(0, 'Futebol')
# lista.insert(1, 'Volei')
# lista.insert(2, 'Basquete')
# lista.insert(3, 'Tenis')
# lista.insert(4, 'Surf')
# lista.pack(side ='left', fill='x',expand='True')

# forma sequencial ---------------------------------------------------------

# lista = Listbox(i)
# lista.insert(END,'Futebol')
# lista.insert(END,'Volei')
# lista.insert(END,'Basquete')
# lista.insert(END,'Tenis')
# lista.insert(END,'Surf')
# lista.pack()

# laço de repetição ---------------------------------------------------

# lista = Listbox()
# estado = ['Ac','MG','SP','RJ']
# for e in estado:
#     lista.insert(END,e)
# lista.pack()
#
# i.mainloop()

# -----------------------
# Usuário adiciona
#
# def adcionar_lista(event=None):
#     item = entrada.get()
#     if item:
#         lista.insert(END, item)
#         entrada.delete(0, END)
#
# entrada = Entry(i)
# entrada.pack(pady=10)
# entrada.bind('<Return>',adcionar_lista)
#
# lista = Listbox(i)
# lista.pack(pady=10)
#
# i.mainloop()

# NOVO IMPORT ----------------------------------

import tkinter as tk

#Criando a janela principal

root = tk.Tk()

#Adicionando  widgets e funcionalidades ----------------------------

# lista = tk.Listbox(root)
# estado = ['Ac', 'MG', 'SP', 'RJ']
# for i in estado:
#     lista.insert(tk.END, i)
# lista.pack()
#
# # Iniciando o loop principal da interface gráfica
# root.mainloop()

# -------------------------------------


# def adicionar_nomes(event=None):
#     nome = entrada.get()
#     lista.insert(tk.END, nome)
#     entrada.delete(0, tk.END)
#
#
# entrada = tk.Entry(root)
# entrada.pack(pady=10)
# entrada.bind('<Return>', adicionar_nomes)
#
# botao = tk.Button(root, text="Adicionar", command=adicionar_nomes)
# botao.pack(pady=10)
#
# lista = tk.Listbox(root)
# lista.pack(pady=10)
#
# root.mainloop()
#

