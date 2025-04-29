import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="aula8"
)

x = conexao.cursor()

#x.execute('create database if not exists aula8')
'''x.execute('show databases')
for i in x:
    print(i)

x.execute('use aula8')

x.execute(create table if not exists aluno(
          matricula int auto_increment primary key,
          nome varchar(30) not null,
          idade int,
          email varchar(50)))

x.execute('show tables')
for i in x:
    print(i)

x.execute('describe aluno')
for i in x:
    print(i)

y = "insert into aluno(nome, idade, email) values ('Thereza',34,'teste@gmail.com')"
x.execute(y)
conexao.commit()
print(x.rowcount, 'registro(s) inserido(s)')

v = [
    ('Thereza',34,'teste@gmail.com'),
    ('Tatiana',12,'teste1@gmail.com'),
    ('Tales',20,'teste2@gmail.com'),
    ('Maria',14,'teste3@gmail.com'),
    ('Paulo',4,'teste4@gmail.com'),
    ('Joana',40,'teste5@gmail.com'),
 ]
x.executemany("insert into aluno(nome, idade, email) values (%s,%s,%s)",v)
conexao.commit()
print(x.rowcount, 'registro(s) inserido(s)')

x.execute('select * from aluno')
resultado = x.fetchall()
print('Todos os dados dos alunos:')
for i in resultado:
    print(i)

x.execute('select nome,idade from aluno')
resultado = x.fetchall()
print('Todos os dados dos alunos:')
for i in resultado:
    print(i)

x.execute('select nome,idade from aluno')
resultado = x.fetchone()
print('Primeiro nome e idade do aluno:')
for i in resultado:
    print(i)

x.execute('select nome,idade from aluno where idade>20')
resultado = x.fetchall()
print('Alunos com idade maior que 20:')
for i in resultado:
    print(i)

x.execute('select * from aluno order by nome')
resultado = x.fetchall()
print('Ordenado por nome(A-Z)')
for i in resultado:
    print(i)'''

x.execute('select * from aluno order by nome DESC ')
resultado = x.fetchall()
print('Ordenado por nome(Z-A)')
for i in resultado:
    print(i)
