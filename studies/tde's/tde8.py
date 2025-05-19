import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = ""
    # database="mydb"
)

cursor = conn.cursor()
c = cursor

# c.execute("CREATE DATABASE IF NOT EXISTS livraria")

c.execute("USE livraria")

# c.execute('''CREATE TABLE IF NOT EXISTS clientes(
#             id_cliente INT NOT NULL PRIMARY KEY,
#             cpf VARCHAR(11) NOT NULL,
#             nome_cliente VARCHAR(30) NOT NULL,
#             endereço VARCHAR(200),
#             telefone VARCHAR(20),
#             listaLivros VARCHAR(200)
#             )''')

# c.execute("ALTER TABLE clientes CHANGE COLUMN cpf cpf_cnpj VARCHAR(14) NOT NULL")
# c.execute("ALTER TABLE clientes CHANGE COLUMN id_cliente id_cliente INT NOT NULL AUTO_INCREMENT")
# c.execute("ALTER TABLE clientes DROP COLUMN listalivros")
# conn.commit()
#
# tabela_clientes=[(17864375607,'Pedro Gabriel', 'Vista Alegre, São Gonçalo', 21997998038),
#                  (10898750617, 'Gabriella Hespanhol', 'Várzea das Moças, Niterói', 21986669879)]
#
# c.executemany('insert into clientes(cpf_cnpj, nome_cliente, endereço, telefone) values(%s,%s,%s,%s)', tabela_clientes)
# conn.commit()

# c.execute('''CREATE TABLE IF NOT EXISTS compras(
#             id_compras INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#             id_cliente INT NOT NULL,
#             data_compra DATETIME,
#             FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente))''')

# tabela_compras=[(1, 31-8-2025),
#                 (2, 21-3-2025)]

# c.executemany('insert into compras(id_cliente, data_compra) values (%s, %s)', tabela_compras)
# conn.commit()
#
# c.execute('''CREATE TABLE IF NOT EXISTS lista_compras(
#             id_lista INT PRIMARY KEY AUTO_INCREMENT,
#             id_compra INT,
#             titulo_livro VARCHAR(50),
#             FOREIGN KEY(id_compra) REFERENCES compras(id_compras))''')

# tabela_listacompras=[(9,'Harry Potter e a Pedra Filosofal'),
#                      (10, 'Harry Potter e a Ordem da Fênix')]

# c.execute("ALTER TABLE lista_compras DROP FOREIGN KEY lista_compras_ibfk_1")
# c.execute("ALTER TABLE lista_compras DROP COLUMN id_livro")



# c.executemany('insert into lista_compras(id_compra, titulo_livro) values (%s, %s)', tabela_listacompras)


# c.execute("ALTER TABLE lista_compras ADD COLUMN id_livro INT")
# c.execute("ALTER TABLE lista_compras ADD FOREIGN KEY (id_livro) REFERENCES livros(id_livro)")


#
# c.execute('''CREATE TABLE IF NOT EXISTS editoras(
#             id_editora INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#             nome_editora VARCHAR(255) NOT NULL,
#             endereco VARCHAR(255),
#             telefone VARCHAR(20),
#             nome_gerente VARCHAR(100))''')

# tabela_editoras = [
#     ("Companhia das Letras", "Rua Oscar Freire, 123, São Paulo, SP", "(11) 1234-5678", "Pedro Albuquerque"),
#     ("Record", "Avenida Paulista, 1000, São Paulo, SP", "(11) 2345-6789", "Ana Costa"),
#     ("Saraiva", "Rua da Consolação, 200, São Paulo, SP", "(11) 3456-7890", "Fernanda Lima")]


# c.executemany("INSERT INTO editoras (nome_editora, endereco, telefone, nome_gerente) VALUES (%s, %s, %s, %s)",tabela_editoras)
#
# c.execute('''CREATE TABLE IF NOT EXISTS livros(
#             id_livro INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#             titulo VARCHAR(100) NOT NULL,
#             autor VARCHAR(100),
#             assunto VARCHAR(100),
#             editora VARCHAR(100),
#             ISBN VARCHAR(20) UNIQUE,
#             quantidade_estoque INT,
#             id_editora INT,
#             FOREIGN KEY(id_editora) REFERENCES editoras(id_editora))''')

# c.execute("ALTER TABLE livros DROP COLUMN editora")
#
# tabela_livros = [("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", "9780544003415", 10, 1),
#     ("Dom Casmurro", "Machado de Assis", "Romance", "9788525411909", 5, 2),
#     ("Python para Iniciantes", "João Silva", "Tecnologia", "9788575222431", 8, 3),]
#
# c.executemany('''INSERT INTO livros (titulo, autor, assunto, ISBN, quantidade_estoque, id_editora)VALUES (%s, %s, %s, %s, %s, %s)''', tabela_livros)
#

# from datetime import datetime
#
# agora = datetime.now()
# data_hora_str = agora.strftime('%Y-%m-%d %H:%M:%S')


# c.execute("UPDATE compras SET data_compra = %s WHERE id_compras IN (%s, %s)", [data_hora_str, 1, 2])


# c.execute("SELECT * FROM clientes")
# clientes = c.fetchall()
# for i in clientes:
#     print(i)

# c.execute("SELECT * FROM compras")
# compras = c.fetchall()
# for i in compras:
#     print(i)

# c.execute("SELECT * FROM lista_compras")
# lista_compras = c.fetchall()
# for i in lista_compras:
#     print(i)
# #

# c.execute("SHOW CREATE TABLE lista_compras")
# tabela = c.fetchall()
# for linha in tabela:
#     print(linha)

# c.execute("SELECT * FROM clientes WHERE id_cliente = 2")
# clientes = c.fetchall()
# for i in clientes:
#     print(i)

# c.execute("SELECT titulo, quantidade_estoque FROM livros")
# livros = c.fetchall()
# for i in livros:
#     print(i)




conn.commit()
print(c.rowcount, "atualizações realizadas")