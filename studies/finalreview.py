# aula 3 ----

#Estrutura condicional if/else/elif

# a = int(input('Digite o valor de a: '))
# b = int(input('Digite o  valor b: '))

# if a == b:
#     print(f'O valor de {a} é igual a {b} ?')
# else:
#     print(f'O valor de {a} não é igual de {b}')


# -------------------

# c = int(input('Digite o valor de c: '))
# d = int(input('Digite o  valor d: '))

# if d > c:
#     print(f'o valor de {d} é maior que o valor de {c}')
# elif d == c:
#     print(f'o valor de {d} é igual o valor de {c}')
# elif d + 20 != c:
#     print(f'o valor de {d} é diferente o valor de {c}')
# else:
#     print('Todas as verificações foram falsas!')

# --------------

# c = int(input('Digite o valor de c: '))
# d = int(input('Digite o  valor d: '))

# res = 0
# op = input('Digite o valor de op: +,-,*,/: ')

# if op == '+':
#     res = c + d
#     print(f' A soma de {c} + {d} = {res}')
# elif op == '-':
#     res = c - d
#     print(f' A subtração de {c} - {d} = {res}')
# elif op == '*':
#     res = c * d
#     print(f' A multiplicação de {c} * {d} = {res}')
# elif op == '/':
#     res = c / d
#     print(f' A divisão de {c} / {d} = {res}')
# print('Término do programa!')

#--------------------------------

# a = int(input("Digite um numero: "))
# b = int(input("Digite um numero: "))


# if b > a:
#     c = a
#     a = b
#     b = c

# print(a,b)


# - Ternário ---------------------

# idade = int(input("Qual a sua idade?: "))
# print('A idade é menor que 17' if idade < 17 else 'A idade é maior que 17')

# nota = float(input('Qual a sua nota?: '))
# print('Aprovado' if nota >= 6 else 'Reprovado')

# -----------------------

# numero = int(input("Digite um número: "))
# if numero <= 10 and numero % 2 == 0:
#     print(f'O valor do {numero} é menor ou igual a 10 e é um numero par')
# else:
#     print(f'O valor é {numero} não é válido')

# For --------------

# e = 0
# f = 10
# for i in range(f):
#     print('Oi!')

#-----------------------------

# for z in range(1,10):
#     print(z)

# --------------------

# for numero in range(1,8):
#    if numero % 2 == 0:
#       print(f'O numero {numero} é par')
#    else:
#       print(f'O numero {numero} é impar')

# -----------------

# for numero in range(10,30,2): #start, stop and step
#     print(f'Numero : {numero}')

# -----------------

# for numero in range(10):
#     if numero > 5:
#         break #encerra o loop do for
#     print(numero)
# print('Fim')

# ----------

# for numero in range(20,30):
#     if numero == 25:
#         continue #pulou o 25 mas continua o loop
#     print(numero)

#tabuada -------------------------------------------------------------

# num = int(input('Digite o valor da tabuada: '))

# for t in range (0,11):
#     print(f'{num} x {t} = {num * t}')

# -------------------------------

# nome = 'Thereza'
# for n,l in enumerate(nome): #enumera cada caracterer
#     print(n,l)

#while -------------------------------------------------------------------

# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('Terminou')

# -----------------

# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input('Digite um valor: '))
#     if n!= 0 :
#         if n % 2 == 0:
#             par += 1
#         else:
#             impar += 1
# print(f'você digitou {par} numeros pares e {impar} numeros impares')

# --------------------

# sexo = input('Digite o sexo [M/F/O]: ').strip().upper()[0]
# while sexo not in 'MFO':
#     sexo = input('Digite o sexo [M/F/O]: ').strip().upper()[0]
# print(f'Sexo {sexo} registrado com sucesso')

# -------------------

# import random

# from random import randint

# c = randint(1,10)
# print("Tente adivinhar...")
# acerto = False
# while not acerto:
#     j = int(input('Qual o seu palpite?: '))
#     if j == c:
#         acerto = True
#         print('Acertou')
#     else:
#         print('Errou, tente novamente!')

# ---------=-=-=--=-=-=-=--=---

# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))

# op = 0
# while op != 5:
#     print('''
#     [1]Somar
#     [2]Subtrair
#     [3]Multiplicar
#     [4]Dividir
#     [5]Sair''')

#     op = input('escolha a opção')
#     if op == '1':
#         print(f'A soma de {n1} + {n2} = {n1 + n2}')
#     elif op == '2':
#         print(f'A subtração de {n1} - {n2} = {n1 - n2}')
#     elif op == '3':
#         print(f'A multiplicação de {n1} * {n2} = {n1 * n2}')
#     elif op == '4':
#         print(f'A divisão de {n1} / {n2} = {n1 / n2}')
#     elif op == '5':
#         print(f'saindo do programa')
#     else:
#         print('Opção inválida 🤡')
# print('Fim')

# --=-=-=-=-=-=-=--=-=-=-=-==-=-==-=-=-==-=-=-==-=-==-=-=-==-=-=-==-=-=--==-=-=-=-=-==-=-=-=-=-==-=-

import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host = 'localhost',
    psswd = "",
    user = "root"
)

cursor = conexao.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS g3")
cursor.execute("USE g3")


cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
                id_aluno INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                email VARCHAR(100),
                telefone VARCHAR(20),
                data_nascimento DATE,
                status VARCHAR(20)
                )'''
            )

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursos (
        id_curso INT AUTO_INCREMENT PRIMARY KEY,
        nome_curso VARCHAR(100),
        descricao TEXT
    )
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS matriculas(
                id_matricula INT AUTO_INCRMENT PRIMARY KEY,
                id_aluno INT,
                id_curso INT,
                data_matricula DATE
                FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
                FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
                )"""
            )

def cadastrar_alunos():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_tel.get()
    nascimento = entry_nascimento.get()
    
    try:
        nascimento_formatado = datetime.strptime(nascimento, "%d/%m/%Y").date()
        cursor.execute("INSERT INTO alunos (nome, email, telefone, data_nascimento) VALUES (%s, %s, %s, %s)",
                       (nome, email, telefone, nascimento_formatado))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
        
janela = tk.Tk()
janela.title("Cadastro de Alunos")

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

tk.Label(janela, text="Email").pack()
entry_telefone = tk.Entry(janela)
entry_telefone.pack()

tk.Label(janela, text="Nascimento (dd/mm/aaaa)").pack()
entry_nascimento = tk.Entry(janela)
entry_nascimento.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar_alunos).pack()

janela.maimloop()