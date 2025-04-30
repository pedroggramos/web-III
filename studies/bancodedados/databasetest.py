import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

x = conexao.cursor()

x.execute('create database if not exists test')

# x.execute('show databases')
# for i in x:
#     print(i)