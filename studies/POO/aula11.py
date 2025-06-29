# # class Aluno:
# #     def __init__(self, nome, idade, curso):
# #         self.nome = nome
# #         self.idade = idade
# #         self.curso = curso
# #
# #     def apresentar(self):
# #         print(f'Olá! Meu nome é {self.nome} tenho {self.idade} anos e estudo {self.curso}')
# #
# #     def maioridade(self):
# #         if self.idade >= '18':
# #             print(f'{self.nome} é maior de idade')
# #         else:
# #             print(f'{self.nome} é menor de idade')
# #
# # aluno1 = Aluno('Pedro', '19', 'Sistemas de informação')
# # aluno2 = Aluno('Gabriella', '19', 'Arquitetura e Urbanismo')
# #
# # aluno1.apresentar()
# # aluno2.apresentar()
# # aluno1.maioridade()
# # aluno2.maioridade()
#
# # -----------------------------------
#
# # class Aluno:
# #     def __init__(self, nome, idade, curso):
# #         self.nome = nome
# #         self.idade = idade
# #         self.curso = curso
# #         self.notas = []
# #
# #     def apresentar(self):
# #         print(f'Olá! Meu nome é {self.nome} tenho {self.idade} anos e estudo {self.curso}')
# #
# #     def adicionar_nota(self, nota):
# #         if 0 <= nota <= 10:
# #             self.notas.append(nota)
# #         else:
# #             print('Nota inválida.Insira uma nota entre 0 e 10.')
# #
# #     def calcular_media(self):
# #         if len(self.notas) == 0:
# #             return 0
# #         return sum(self.notas) / len(self.notas)
# #
# #     def verificar_aprovacao(self):
# #         media = self.calcular_media()
# #         print(f'A media do {self.nome}: {media:.2f}')
# #         if media >= 7:
# #             print('Aprovado!')
# #         elif 7 > media >= 5:
# #             print('Recuperação!')
# #         else:
# #             print('Reprovado!')
# #
# # aluno1 = Aluno('Pedro', '19', 'Sistemas de informação')
# # aluno2 = Aluno('Gabriella', '19', 'Arquitetura e Urbanismo')
# #
# # aluno1.apresentar()
# # aluno1.adicionar_nota(5)
# # aluno1.adicionar_nota(10)
# # aluno1.adicionar_nota(7)
# # aluno1.verificar_aprovacao()
# # aluno2.apresentar()
# # aluno2.adicionar_nota(5)
# # aluno2.adicionar_nota(6)
# # aluno2.adicionar_nota(5)
# # aluno2.verificar_aprovacao()
#
# # ----------------------------------------
#
# class Aluno:
#     def __init__(self, nome, curso, idade):
#         self.nome = nome
#         self.idade = idade
#         self.curso = curso
#         self.notas = []
#
#     def apresentar(self):
#         print(f'Olá! Meu nome é {self.nome}, tenho {self.idade} anos e estudo {self.curso}')
#
#     def adicionar_nota(self, nota):
#         if 0 <= nota <= 10:
#             self.notas.append(nota)
#             print(f'Nota {nota} adicionada com sucesso.')
#         else:
#             print('Nota inválida. Insira uma nota entre 0 e 10.')
#
#     def calcular_media(self):
#         if not self.notas:
#             return 0
#         return sum(self.notas) / len(self.notas)
#
#     def verificar_aprovacao(self):
#         media = self.calcular_media()
#         if media >= 7:
#             print('Aprovado!')
#         elif 7 > media >= 5:
#             print('Recuperação!')
#         else:
#             print('Reprovado!')
#
# def menu():
#     aluno = None
#
#     while True:
#         print('\n==========MENU=========')
#         print('[1] - Cadastrar Aluno')
#         print('[2] - Adicionar nota')
#         print('[3] - Média/Aprovação')
#         print('[4] - Mostrar Dados do aluno')
#         print('[5] - Sair do programa')
#
#         opcao = input('Escolha a opção(1-5): ').strip()
#         if not opcao in ('1', '2', '3', '4', '5'):
#             print('Entrada inválida! Digite uma opção.')
#             continue
#         if opcao == '1':
#             nome = input('Nome: ')
#             idade = input('Idade: ')
#             curso = input('Curso: ')
#             aluno = Aluno(nome, curso, idade)
#             print('Aluno cadastrado com sucesso!')
#         elif opcao == '2':
#             if aluno:
#                 if 0 > len(aluno.notas) < 3:
#                     try:
#                         restante = 3 - len(aluno.notas) #qtd de notas que faltam
#                         for i in range(restante):
#                             nota = float(input(f'Digite a nota {i + 1}: '))
#                             aluno.adicionar_nota(nota)
#                     except ValueError:
#                         print('Nota inválida')
#                 else:
#                     print("Este aluno já possui 3 notas: ")
#                     for i, nota in enumerate(aluno.notas, 1):
#                         print(f'Nota [{i}] - {nota}')
#                     resp = input("Deseja substituir alguma nota? (s/n): ").strip().lower()
#                     if resp == 's':
#                         try:
#                             pos = int(input("Informe a nota que deseja substituir(1 a 3): "))
#                             if pos in [1, 2, 3]:
#                                 nova = float(input("Digite a nova nota: "))
#                                 aluno.notas[pos - 1] = nova
#                                 print("Nota substituada com sucesso!")
#                             else:
#                                 print("Posição inválida")
#                         except ValueError:
#                             print("Entrada inválida")
#             else:
#                 print("Cadastre um aluno primeiro")
#
#         elif opcao == '3':
#             if aluno:
#                 aluno.verificar_aprovacao()
#             else:
#                 print('Cadastre um aluno primeiro')
#         elif opcao == '4':
#             if aluno:
#                 aluno.apresentar()
#                 print(f'Notas: ', aluno.notas)
#                 print(f'Média Atual: {aluno.calcular_media():.2f}')
#             else:
#                 print('Cadastre um aluno primeiro')
#         elif opcao == '5':
#             print('Encerrando...')
#             break
#
# menu()
#
# # ------------------------------


import tkinter as tk
from tkinter import ttk, messagebox

class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return True
        return False

    def calcula_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcula_media()
        return media >= 7, media

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Aluno")
        self.aluno = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Nome: ").grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Idade: ").grid(row=1, column=0)
        self.idade_entry = tk.Entry(self.root)
        self.idade_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Curso: ").grid(row=2, column=0)
        self.curso_entry = tk.Entry(self.root)
        self.curso_entry.grid(row=2, column=1)

        tk.Button(self.root, text="Cadastrar Aluno", command=self.cadastrar_aluno).grid(row=3, columnspan=2, pady=10)

        tk.Label(self.root, text="Nota: ").grid(row=4, column=0)
        self.nota_entry = tk.Entry(self.root)
        self.nota_entry.grid(row=4, column=1)

        tk.Button(self.root, text="Adicionar Nota", command=self.adicionar_nota).grid(row=5, columnspan=2, pady=10)
        tk.Button(self.root, text="Ver Média e Situação", command=self.mostrar_media).grid(row=6, columnspan=2, pady=5)
        tk.Button(self.root, text="Mostrar Dados", command=self.mostrar_dados).grid(row=7, columnspan=2, pady=5)

    def cadastrar_aluno(self):
        nome = self.nome_entry.get().strip()
        idade = self.idade_entry.get().strip()
        curso = self.curso_entry.get().strip()

        if nome and idade.isdigit() and curso:
            self.aluno = Aluno(nome, int(idade), curso)
            messagebox.showinfo("Cadastro", f"Aluno {nome} cadastrado com sucesso.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente")

    def adicionar_nota(self):
        if not self.aluno:
            messagebox.showwarning("Erro", "Cadastre um aluno primeiro")
            return

        nota_str = self.nota_entry.get().strip()
        try:
            nota = float(nota_str)
            if self.aluno.adicionar_nota(nota):
                messagebox.showinfo("Nota", f'Nota {nota} adicionada.')
                self.nota_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Erro", "Nota deve estar entre 0 e 10")
        except ValueError:
            messagebox.showwarning("Erro", "Digite um número válido")

    def mostrar_media(self):
        if not self.aluno:
            messagebox.showwarning("Erro", "Cadastre um aluno primeiro")
            return

        aprovado, media = self.aluno.verificar_aprovacao()
        status = "Aprovado" if aprovado else "Reprovado"
        messagebox.showinfo("Resultado", f'Média: {media:.2f}\nSituação: {status}')

    def mostrar_dados(self):
        if not self.aluno:
            messagebox.showwarning("Erro", "Cadastre um aluno primeiro")
            return

        dados = (
            f"Nome: {self.aluno.nome}\n"
            f"Idade: {self.aluno.idade}\n"
            f"Curso: {self.aluno.curso}\n"
            f"Notas: {self.aluno.notas}\n"
            f"Média: {self.aluno.calcula_media():.2f}\n"
        )
        messagebox.showinfo("DADOS DO ALUNO", dados)

root = tk.Tk()
app = App(root)
root.mainloop()
