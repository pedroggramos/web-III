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
from tkinter import messagebox

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
# -----------------------
#
# import tkinter as tk
# from tkinter import ttk, messagebox
#
# root = tk.Tk()
# root.title('Exemplo Treeview')
#
# colunas = ('ID', 'Nome', 'Email')
#
# tree = ttk.Treeview(root, columns=colunas, show='headings')
# tree.heading('ID', text='ID')
# tree.column('ID', width='50')
# tree.heading('Nome', text='Nome')
# tree.column('Nome', width='150')
# tree.heading('Email', text='Email')
# tree.column('Email', width='150')
#
# tree.insert('', tk.END, values=(1, 'Gabriella', 'gabriella.hespanhol@soulasalle.com'))
# tree.insert('', tk.END, values=(2, 'Pedro', 'pedrogabriel@soulasalle.com'))
# tree.insert('', tk.END, values=(3, 'JP', 'jp@gmail.com'))
#
# tree.pack(fill=tk.BOTH, expand=True)#empacotar o widget na janela
#
# root.mainloop()

# ------------------------

import mysql.connector
from mysql.connector import errorcode
import tkinter as tk
from tkinter import ttk, messagebox

from studies.bancodedados.databasetest import conexao


def criar_banco_tabela():
    try:
        conexao = mysql.connector.connect(
            host="localhost:3306",
            user="root",
            passwd="",
        )
        if conexao.is_connected():
            print("Conexao estabelecida com sucesso!")
            cursor=conexao.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro")
            print("Banco de dados criado com sucesso!")
            cursor.execute("USE cadastro")

            cursor.execute("""CREATE TABLE IF NOT EXISTS pessoas(
                              id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              nome VARCHAR(255) NOT NULL,
                              email VARCHAR(255) NOT NULL)
                              """)
            print("Tabela criada com sucesso!")
            cursor.close()
            # conexao.close()
    except ValueError as erro:
        print(f'Erro ao conectar ao banco de dados: {erro}')
criar_banco_tabela()

def conectar(): #retornar uma nova conexao com o banco cadastro
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='cadastro'
    )

def adicionar():
    nome = entry_nome.get() #coleta os dados digitados na interface da janela
    email = entry_email.get() #coleta os dados digitados na interface da janela
    if not nome or not email: #os campos não podem estar vazios
        messagebox.showwarning('Atenção', ' Todos os campos são obrigatórios')
        return
    conexao = conectar() #conecta ao banco
    cursor = conexao.cursor() #define o cursor
    cursor.execute("INSERT INTO pessoas(nome, email) VALUES (%s,%s)", (nome, email)) #insere os dados que foram digitados na janela
    conexao.commit() #salva as mudanças
    conexao.close()
    carregar_dados() #atualiza a tabela na interface(janela)
    limpar_dados() #limpa os campos após adicionar

def carregar_dados():
    for item in tree.get_children():
        tree.delete(item)
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas")
    for row in cursor.fetchall():
        tree.insert('', tk.END, values=row)
    conexao.close()

def atualizar():
    item = tree.selection()
    if not item:
        messagebox.showwarning('Atenção', 'Selecione um item para atualizar')
        return
    id_pessoa=tree.item(item[0])['values'][0]
    nome = entry_nome.get()
    email = entry_email.get()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('UPDATE pessoa SET nome=%s, email=%s WHERE id=%s',(nome, email, id_pessoa))

def deletar():
    item = tree.selection()
    if not item:
        messagebox.showwarning('Atenção', 'Selecione um item para deletar')
        return

    id_pessoa = tree.item(item[0])['values'][0]
    if messagebox.askyesno("Confirmação", "Deseja deletar o pessoa?"):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM pessoa WHERE id=%s", (id_pessoa,))
        conexao.commit()
        cursor.close()
        carregar_dados()
        limpar_campos()

def preencher_campos():
    item = tree.selection()
    if item:
        valores = tree.item(item[0])['values']
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_nome.insert(0, valores[0])
        entry_email.insert(0, valores[1])
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    tree.selection_remove(tree.selection())

janela = tk.Tk()
janela.title("Sistema Crud com Treeview")
janela.geometry("500x500")

tk.Label(janela,text='Nome:').pack()
entry_nome = tk.Entry(janela,width=40)
entry_nome.pack()

tk.Label(janela, text='Email: ').pack()
entry_email = tk.Entry(janela, width=50)
entry_email.pack()

frame_botoes = ttk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text='Adicionar', command=adicionar).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text='Atualizar',command=atualizar).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text='Deletar', command=deletar).grid(row=0, column=2, padx=5)

colunas = ('ID', 'Nome', 'Email')
tree = ttk.Treeview(janela, columns=colunas, show='headings')
for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill=tk.BOTH, expand=True)
tree.bind('<<TreeviewSelect>>', preencher_campos)

carregar_dados()
janela.mainloop()
