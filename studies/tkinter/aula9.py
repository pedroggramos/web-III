# from tkinter import *
# import mysql.connector
# import tkinter.messagebox as MessageBox
#
# con = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd=""
# )
#
# c = con.cursor()
#
# # c.execute('create DATABASE loja')
# c.execute("use loja")
#
# c.execute('''CREATE TABLE IF NOT EXISTS produto(
#         codigo int PRIMARY KEY,
#         nome varchar(50),
#         preco decimal(10,2),
#         quantidade int)''')
#
# root = Tk()
# root.geometry("500x500")
# root.title("Produtos")
#
# def incluir():
#         codigo = e_codigo.get()
#         nome = e_nome.get().replace(',', '.')
#         preco = e_preco.get()
#         quantidade = e_quantidade.get()
#
#         if(codigo == '' or nome == '' or preco == '' or quantidade == ''):
#             MessageBox.showerror("Error", "Todos os campos são obrigatórios")
#         else:
#             c.execute('INSERT INTO produto(codigo,nome,preco,quantidade) VALUES (%s,%s,%s,%s)', (codigo, nome, preco, quantidade))
#             con.commit()
#             MessageBox.showinfo("Success", "Produto cadastrado com sucesso")
#             e_codigo.delete(0, END)
#             e_nome.delete(0, END)
#             e_preco.delete(0, END)
#             e_quantidade.delete(0, END)
#
# def excluir():
#     codigo = e_codigo.get()
#
#     if codigo == '':
#         MessageBox.showerror('Error', 'Todos os campos são obrigatórios')
#     else:
#         c.execute('DELETE FROM produto WHERE codigo = %s',(codigo,))
#         con.commit()
#         MessageBox.showinfo("Success", "Produto excluido com sucesso")
#         e_codigo.delete(0, END)
#
# def atualizar():
#     codigo = e_codigo.get()
#     nome = e_nome.get()
#     preco = e_preco.get().replace(',', '.')
#     quantidade = e_quantidade.get()
#     if codigo == '':
#         MessageBox.showerror('Error', 'Informe o código do Produto')
#     else:
#         c.execute('UPDATE produto SET nome=%s, preco=%s, quantidade=%s WHERE codigo=%s', (nome, preco, quantidade, codigo))
#         con.commit()
#         MessageBox.showinfo("Success", "Produto atualizado com sucesso")
#
#         e_codigo.delete(0, END)
#         e_nome.delete(0, END)
#         e_preco.delete(0, END)
#         e_quantidade.delete(0, END)
#
# def selecionar():
#     codigo = e_codigo.get()
#     if codigo == '':
#         MessageBox.showerror('Error', 'Informe o codigo do produto')
#     else:
#         c.execute('SELECT * FROM produto WHERE codigo = %s', (codigo,))
#         rows = c.fetchall()
#
#         if rows:
#             for row in rows:
#                 e_nome.delete(0, END)
#                 e_preco.delete(0, END)
#                 e_quantidade.delete(0, END)
#
#                 e_nome.insert(0, row[1])
#                 e_preco.insert(0, row[2])
#                 e_quantidade.insert(0, row[3])
#             MessageBox.showinfo("Success", f'Produto selecionado com sucesso\nCodigo:{row[0]}\nNome:{row[1]}\nPreco:{row[2]}\nQuantidade:{row[3]}')
#         else:
#             MessageBox.showerror('Error', 'Produto não encontrado')
#
#
# Label(root, text='Codigo').place(x=20,y=30)
# Label(root, text='Nome').place(x=20,y=60)
# Label(root, text='Preço').place(x=20,y=90)
# Label(root, text='Quantidade').place(x=20,y=120)
#
# e_codigo = Entry(root)
# e_codigo.place(x=100,y=30)
# e_nome = Entry(root)
# e_nome.place(x=100,y=60)
# e_preco = Entry(root)
# e_preco.place(x=100,y=90)
# e_quantidade = Entry(root)
# e_quantidade.place(x=100, y=120)
#
# Button(root, text='Incluir', command=incluir).place(x=20, y=160)
# Button(root, text='Excluir', command=excluir).place(x=80, y=160)
# Button(root, text='Atualizar', command=atualizar).place(x=140, y=160)
# Button(root, text='Selecionar', command=selecionar).place(x=220, y=160)
#
#
#
# root.mainloop()
#
#
#
#
