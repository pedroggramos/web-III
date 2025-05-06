import mysql.connector
from tkinter import *
import tkinter.messagebox as MessageBox


con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = 'loja'
)
c = con.cursor()
# cur.execute("create database loja")

# c.execute('use loja')
# c.execute('''create table produto(
#             codigo int primary key,
#             nome varchar(50),
#             preco decimal(10,2),
#             quantidade int)''')

root = Tk()
root.geometry('500x500')
root.title('Produtos')

def inserir():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade = e_quantidade.get()

    if(codigo == '' or nome == '' or preco == '' or quantidade == ''):
        MessageBox.showinfo('Inserir', 'Todos os campos são obrigatórios!')
    else:
        c.execute('''INSERT INTO produto (codigo, nome, preco, quantidade) values (%s,%s,%s,%s)''', (codigo, nome, preco, quantidade))
        con.commit()
        MessageBox.showinfo('Inserir', 'Produtos salvos com sucesso!')
        e_codigo.delete(0, END)
        e_nome.delete(0, END)
        e_preco.delete(0, END)
        e_quantidade.delete(0, END)

def excluir():
    codigo = e_codigo.get()

    if codigo == '':
        MessageBox.showinfo(('Excluir', 'Informe o código do produto'))
    else:
        c.execute('DELETE FROM produto WHERE codigo = %s', (codigo,))
        con.commit()
        MessageBox.showinfo('Excluir', 'Produtos salvos com sucesso!')

        e_codigo.delete(0, END)

def atualizar():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade = e_quantidade.get()
    if(codigo == ''):
        MessageBox.showinfo('Atualizar', 'Produtos salvos com sucesso!')
    else:
        c.execute('update produto set nome=%s, preco=%s, quantidade=%s where codigo=%s', (nome, preco, quantidade, codigo))
        con.commit()
        MessageBox.showinfo('Atualizar', 'Produtos salvos com sucesso!')
        e_codigo.delete(0, END)
        e_nome.delete(0, END)
        e_preco.delete(0, END)
        e_quantidade.delete(0, END)

# def selecionar():
#     codigo = e_codigo.get()
#
#     if codigo == '':
#         MessageBox.showinfo(('Seleccionar', 'Produtos salvos com sucesso!'))
#         c.execute('SELECT * FROM produto where codigo = %s', (codigo,))
#         rows = c.fetchall()
#         if rows:
#             for row in rows:
#                 e_nome.delete(0, END)
#                 e_preco.delete(0, END)
#                 e_quantidade.delete(0, END)
#
#                 e_nome.insert(0, row[1])
#                 e_preco.insert(0, row[2])
#                 e_quantidade.insert(0, row[3])
#                 MessageBox.showinfo('Seleccionar', f'Produto encontrado!\nCodigo: {row[0]}\nNome: {row[1]}\nPreço: {row[2]}\nQuantidade: {row[3]}')
#     else:
#         MessageBox.showinfo('Seleccionar', 'Erro ao selecionar produto!')
#
#

def selecionar():
    codigo = e_codigo.get()

    if codigo == '':
        MessageBox.showinfo('Seleccionar', 'Informe o código do produto')
    else:
        c.execute('SELECT * FROM produto WHERE codigo = %s', (codigo,))
        rows = c.fetchall()
        if rows:
            for row in rows:
                e_nome.delete(0, END)
                e_preco.delete(0, END)
                e_quantidade.delete(0, END)

                e_nome.insert(0, row[1])
                e_preco.insert(0, row[2])
                e_quantidade.insert(0, row[3])
            MessageBox.showinfo('Seleccionar', f'Produto encontrado!\nCodigo: {row[0]}\nNome: {row[1]}\nPreço: {row[2]}\nQuantidade: {row[3]}')
        else:
            MessageBox.showinfo('Seleccionar', 'Produto não encontrado!')




Label(root, text='Codigo').place(x=20, y=30)
Label(root, text='Nome').place(x=20, y=60)
Label(root, text='Preço').place(x=20, y=90)
Label(root, text='Quantidade').place(x=20, y=120)

e_codigo = Entry(root)
e_codigo.place(x=100, y=30)
e_nome = Entry(root)
e_nome.place(x=100, y=60)
e_preco = Entry(root)
e_preco.place(x=100, y=90)
e_quantidade = Entry(root)
e_quantidade.place(x=100, y=120)

Button(root, text='Incluir', command=inserir).place(x=20, y=150)
Button(root, text='Excluir', command=excluir).place(x=80, y=160)
Button(root, text='Alterar', command=atualizar).place(x=140, y=160)
Button(root, text='Consultar', command=selecionar).place(x=200, y=160)






root.mainloop()