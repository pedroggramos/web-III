# import tkinter as tk
# from tkinter import ttk, messagebox
#
# root = tk.Tk()
# root.title("Exemplo Treeview")
#
# colunas = ('ID', 'Nome', 'Email')
# tree = ttk.Treeview(root, columns=colunas, show='headings')
# tree.heading('ID', text='ID')
# tree.column('ID', width=50)
# tree.heading('Nome', text='Nome')
# tree.column('Nome', width=150)
# tree.heading('Email', text='Email')
# tree.column('Email', width=150)
#
# tree.insert('', tk.END, values=(1,'Gabriella','gabriella.hespanhol@soulasalle.com.br'))
# tree.insert('', tk.END, values=(2, 'Pedro', 'pedrogabriel@soulasalle.com.br'))
# tree.insert('', tk.END, values=(3, 'JP', 'jp@gmail.com'))
# tree.pack(fill=tk.BOTH, expand=True) #Importante empacotar o widget na janela
#
# root.mainloop()

# import mysql.connector
# from mysql.connector import errorcode
#
# def criar_banco_tabela():
#     try:
#         conexao = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             passwd=""
#         )
#         if conexao.is_connected():
#             print('Conexao estabelecida com o banco!')
#             cursor = conexao.cursor()
#
#             cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro")
#             cursor.execute("USE cadastro")
#             cursor.execute("""CREATE TABLE IF NOT EXISTS pessoa(
#                               id int auto_increment PRIMARY KEY,
#                               nome varchar(50) NOT NULL,),
#                               email varchar(80))""")
#             print("Tabela criada com sucesso!")
#             cursor.close()
#             conexao.close()
#     except ValueError as erro:
#         print(f'Erro ao conectar com o banco: {erro}')
# criar_banco_tabela()
#
