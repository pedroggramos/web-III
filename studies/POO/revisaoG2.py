import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=''
)

cursor = conexao.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS escolaReview")
cursor.execute("use escolaReview")

cursor.execute("""CREATE TABLE IF NOT EXISTS alunosReview(
                  id_aluno INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                  nome VARCHAR(255) NOT NULL,
                  email VARCHAR(255) NOT NULL,
                  telefone VARCHAR(20),
                  data_nascimento DATE,
                  status VARCHAR(20)
                  )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS cursosReview(
                  id_curso INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                  nome_curso VARCHAR(50),
                  descricao VARCHAR(255)
                  )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS matriculasReview(
                  id_matricula INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                  data_matricula VARCHAR(50),
                  id_aluno INT,
                  id_curso INT,
                  FOREIGN KEY (id_aluno) REFERENCES alunosReview(id_aluno),
                  FOREIGN KEY (id_curso) REFERENCES cursosReview(id_curso)
                  )""")

janela = tk.Tk()
janela.title("Sistema Escolar")
janela.geometry("300x300")

def conectar():
    return mysql.connector.connect(
        host="localhost", user = "root", passwd = "", database = "escolaReview"
    )


def cadastrar_aluno():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    data_nasc = entry_nascimento.get()

    if not nome or not email:
        messagebox.showwarning("Erro", "É necessário preencher os campos de nome e email")
        return

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunosReview(nome, email, telefone, data_nascimento, status) VALUES (%s,%s,%s,%s,%s)", (nome, email, telefone, data_nasc, 'Em análise'))
    conexao.commit()
    conexao.close()
    messagebox.showinfo("Aluno", "Aluno cdastrado com sucesso")

def listar_maiores_18():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunosReview WHERE TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) >= 18")
    alunos = cursor.fetchall()
    cursor.close()
    conexao.close()

    for i in alunos:
        print(i)

def atualizar_status(id_aluno, novo_status):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE alunosReview SET status=%s WHERE id_aluno=%s", (novo_status,id_aluno))
    conexao.commit()
    conexao.close()

def excluir_curso(id_curso):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM cursosReview WHERE id_curso=%s", (id_curso,))
    conexao.commit()
    conexao.close()

tk.Label(janela, text ="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

tk.Label(janela, text="Telefone").pack()
entry_telefone = tk.Entry(janela)
entry_telefone.pack()

tk.Label(janela, text="Data Nascimento(AAAA-MM-DD").pack()
entry_nascimento = tk.Entry(janela)
entry_nascimento.pack()

tk.Button(janela, text = "Adicionar Aluno", command= cadastrar_aluno).pack(pady=10)
tk.Button(janela, text = "Listar maiores 18+", command=listar_maiores_18).pack(pady=10)

janela.mainloop()
