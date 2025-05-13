from tkinter import *

from reportlab.lib.colors import aquamarine

i = Tk() # cria a instancia da janela
i.title('Primeira Janela') #inserir titulo na janela
i.geometry('600x400')
# i.wm_iconbitmap('file.ico') # inserir icone na janela
# i.resizable(0,0) #para bloquear o redimensionamento, pode ser true ou false ou 0 ou 1
# i.state('zoomed')#abre a janela em tela cheia
# i.state('iconic')#abre janela minimizada na barra de tarefas
i.minsize(300,200)#menor tamanho da janela
i.maxsize(900,600)#maior tamanho da janela
i['bg'] = 'aquamarine' #cor de fundo da janela

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

l_nome=Label(i, text='Nome: ', bg='aquamarine')
l_nome.grid(row=0, column=0, padx=10, pady=10)

e_nome=Entry(i)
e_nome.grid(row=0, column=1, padx=10, pady=10)

l_idade=Label(i, text='Idade: ', bg='aquamarine')
l_idade.grid(row=1, column=0, padx=10,pady=10)

e_idade=Entry(i)
e_idade.grid(row=1, column=1, padx=10,pady=10)

def mostrar_informacoes():
    nome=e_nome.get()
    idade=e_idade.get()
    resultado_label.config(text=f'Nome: {nome}, \nIdade: {idade}')




# ---------------------------------------


























































i.mainloop()