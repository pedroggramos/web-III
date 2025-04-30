import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test"
)

x = conexao.cursor()
#
# x.execute('create database if not exists test')

# x.execute('show databases')
# for i in x:
#     print(i)

# x.execute("use test")
#
# x.execute('''create table if not exists produtos(
#             codProduto int auto_increment primary key,
#             nome varchar(50) not null,
#             quantidade int)''')
#
# x.execute('show tables')
# for i in x:
#     print(i)

# x.execute('describe produtos')
# for i in x:
#     print(i)
#

#Primeiro inserir, depois executar e depois dar o commit

# y = ("insert into produtos(nome, quantidade) values ('Arroz', 20)")
# x.execute(y)
# conexao.commit()
# print(x.rowcount, 'registros inseridos')

# v = [
#     ('Feijão', 50),
#     ('Batata', 35),
#     ('Carne', 10),
# ]

# Primeiro inserir, depois executar e depois dar o commit
#
# x.executemany("insert into produtos(nome, quantidade) values (%s, %s)", v)
# conexao.commit()
# print(x.rowcount, 'registros inseridos')

# SELECIONAR TODOS OS PRODUTOS(SELECT)

# x.execute("select * from produtos")
# resultado = x.fetchall()
# print('Todos os resultados: ')
# for i in resultado:
#     print(i)

# x.execute("select nome from produtos")
# resultado = x.fetchall()
# print("Todos os resultados")
# for i in resultado:
#     print(i)

#MOSTRAR PRIMEIRO RESULTADO

# x.execute("select nome,quantidade from produtos")
# resultado = x.fetchone()
# print("Primeiro resultado")
# for i in resultado:
#     print(i)

# WHERE PARA ESPECIFICAR (>,<,>=,<=,=)

# x.execute("select * from produtos WHERE quantidade > 34")
# resultado = x.fetchall()
#
# for i in resultado:
#     print(i)

# ORDEM ALFABÉTICA (ORDER BY) ou (ORDER BY **** DESC)

# x.execute("select * from produtos ORDER BY nome")
# resultado = x.fetchall()
# for i in resultado:
#     print(i)
#

# Decrescente

# x.execute("select * from produtos ORDER BY nome DESC")
# resultado = x.fetchall()
# for i in resultado:
#     print(i)






