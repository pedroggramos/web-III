import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    # database="sistema_escolar"
)

c = conn.cursor()



