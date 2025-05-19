# 1---------------------

import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="sistema_escolar"
# )

# c = conn.cursor()

# c.execute("create database if not exists sistema_escolar")
# c.execute("use sistema_escolar")

# 2---------------

# c.execute('''create table if not exists turmas(
#             id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
#             codigo VARCHAR(10),
#             professor VARCHAR(100),
#             ano_letivo INT)''')
#
# c.execute('''create table if not exists alunos(
#             id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
#             nome VARCHAR(100),
#             idade INT,
#             email VARCHAR(100),
#             turma_id INT,
#             FOREIGN KEY(turma_id) REFERENCES turmas(id))''')
#

# dados_turmas =[
#     ("SINF03NBG4A", "Thereza Godim", 2025),
#     ("SINF03NBG4A", "JP Baptista", 2025),
#     ("SINF03NBG4A", "Marco Antônio", 2025)
# ]
#
# c.executemany("insert into turmas(codigo, professor, ano_letivo) VALUES (%s, %s, %s)", dados_turmas)
# conn.commit()
# print(c.rowcount, "registros cadastrados")
#
# c.execute("SELECT id FROM turmas WHERE professor = 'Thereza Godim'")
# turma_thereza = c.fetchone()[0]
#
#
# c.execute("SELECT id FROM turmas WHERE professor = 'JP Baptista'")
# turma_JP = c.fetchone()[0]
#
#
# c.execute("SELECT id FROM turmas WHERE professor = 'Marco Antônio'")
# turma_marco = c.fetchone()[0]

# #
# dados_alunos =[
#     ("Pedro Gabriel", 19, "pedrogabriel@soulasalle.com.br", turma_thereza),
#     ("Gabriella Hespanhol", 19, "gabriella.hespanhol@soulasalle.com.br", turma_JP),
#     ("Valentina Guimarães", 18, "valentina.guimaraes@soulasalle.com.br", turma_marco),
#     ("Pedro Duarte", 23, "pedro.duarte@soulasalle.com.br", turma_JP),
#     ("Carollina Hespanhol", 22, "carollina.hespanhol@soulasalle.com.br", turma_thereza)
# ]
#
# c.executemany("insert into alunos(nome, idade, email, turma_id) values (%s, %s, %s, %s)", dados_alunos)
# #
# conn.commit()
# print(c.rowcount, "registros cadastrados")

# 4--------------

# c.execute("SELECT nome, turma_id FROM alunos")
# alunos = c.fetchall()
# for i in alunos:
#     print(i)

# c.execute("SELECT * FROM alunos ")
# alunos = c.fetchall()
# for i in alunos:
#     print(i)

# c.execute("SELECT * FROM alunos WHERE turma_id = %s", (turma_thereza,))
# alunos = c.fetchall()
# for i in alunos:
#     print(i)

# c.execute("SELECT * FROM alunos WHERE idade >= 19 and idade <= 21")
# alunos = c.fetchall()
# for i in alunos:
#     print(i)

# c.execute('''SELECT t.professor, COUNT(a.id) AS total_alunos
#             FROM turmas AS t
#             JOIN alunos AS a ON t.id = a.turma_id
#             GROUP BY t.professor;''')
#
# resultado = c.fetchall()
# for i in resultado:
#     print(f"Professor: {i[0]}, Total de Alunos: {i[1]}")

# 5 --------------------

# c.execute("UPDATE alunos SET email = %s WHERE id = %s", ('pedrogabriel@lasallerj.edu.br', 1))
# conn.commit()
# print(c.rowcount, "registros encontrados")

# 6 --------------------------


# c.excute("DELETE FROM alunos WHERE id = %s", (3,))
# c.execute("DELETE FROM alunos WHERE id = 3")
# conn.commit()
# print(c.rowcount, "registros encontrados")



# c.execute("DROP TABLE IF EXISTS alunos")

# c.execute('''
#     CREATE TABLE IF NOT EXISTS alunos (
#         id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
#         nome VARCHAR(100),
#         idade INT,
#         email VARCHAR(100),
#         turma_id INT,
#         FOREIGN KEY(turma_id) REFERENCES turmas(id) ON DELETE CASCADE
#     )
# ''')

# c.execute("DELETE FROM turmas WHERE id = 8")
# conn.commit()
# print(c.rowcount, "registros realizados")

# 7---------------

# c.execute("SELECT * FROM alunos ORDER BY idade DESC")
# alunos = c.fetchall()
# for i in alunos:
#     print(i)

# 8-------------

# c.execute("DROP TABLE IF EXISTS alunos")
# c.execute("DROP TABLE IF EXISTS turmas")
# c.execute("DROP DATABASE IF EXISTS sistema_escolar")
#
# print(c.rowcount, "registros encontrados")
#
# conn.close()




# DESAFIO EXTRA

while True:
    import sys
    try:
        conector = int(input('''Digite 1 para criar a conexão com um banco de dados 
        ou 0 caso deseje cancelar: '''))

        if conector == 1:
            import mysql.connector
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=""
            )
            print("Conectado com sucesso!")

            c = conn.cursor()
            nameDatabase = input('Digite o nome do banco de dados: ')
            c.execute(f"CREATE DATABASE IF NOT EXISTS {nameDatabase}")
            print('Banco de dados criada com sucesso!(ou já existia)')

            c.execute(f"USE {nameDatabase}")
            break

        elif conector == 0:
            print("Programa finalizado com sucesso!")
            sys.exit()

        else:
            print("Digite um valor valido!")

    except ValueError:
        print("Digite um número inteiro válido!")



while True:
    try:
        createTable = int(input("Deseja criar quantas tabelas?: "))
        for i in range(createTable):
            nome_tabela = input(f'\nDigite o nome da tabela {i+1}: ')
            colunas = []
            contador = 1
            print(f"\nAdicione as colunas para essa tabela.")
            print("Quando terminar, deixe o nome da coluna em branco e aperte Enter.")
            while True:
                nome_coluna = input(f'\nDigite o nome da coluna {contador}: ').strip()
                if nome_coluna == '':
                    break

                tipo_coluna = input(f'\nDigite o tipo da coluna {contador}  (ex: INT, VARCHAR(100), DATE): ').strip()
                colunas.append(f"{nome_coluna} {tipo_coluna}")
                contador += 1

            if not colunas:
                print("Nenhuma coluna foi adicionada. A tabela não será criada.")
                continue

            estrutura_colunas = ", ".join(colunas)
            comando = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({estrutura_colunas})"
            c.execute(comando)
            print(f"Tabela '{nome_tabela}' criada com sucesso!")
        break


    except ValueError:
        print("Digite um número inteiro válido!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar tabela: {err}")

conn.close()
print("Conexão fechada com sucesso!")















