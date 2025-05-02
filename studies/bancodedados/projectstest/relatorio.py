#importar a base de dados
#vizualizar a base de dados
# -
# faturamento por loja
# quantidade de produtos vendidos por loja
# calcular o ticket medio por produto em cada loja(faturamento/qtd de produtos)
# enviar um email com o relatório
# --

import pandas as pd

#importar a base de dados ----------
tabela_vendas = pd.read_excel("Vendas.xlsx")

# ----------------

#vizualizar a base de dados ---------------
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.set_option("display.max_rows", 10)
# print(tabela_vendas)

# --------------------------

# faturamento por loja -----------
print("-" * 50)
print("Faturamento por Loja:")
print("")

# faturamento = tabela_vendas[['ID Loja','Valor Final']]
# faturamento = (tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').mean())#Média do valor
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# print(tabela_vendas[['ID Loja','Valor Final']])
# print(tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum())


# ---------------------------------

# Qtd de Produtos vendidos por loja ----------
print("-" * 50)
print("Quantidade de produtos por loja:")
print("")

quantidade = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(quantidade)

# print(tabela_vendas[['ID Loja','Valor Final']])
# print(tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum())

# ---------------------------------

# Calcular o ticket médio por produto em cada loja ------------
print("-" * 50)
print("Ticket Médio:")
print("")


ticket_medio = (faturamento['Valor Final']/quantidade['Quantidade']).to_frame()#to_frame: ele pega a divisão e transforma tudo em uma tabela unica(some o dtype)
print(ticket_medio)


# enviando por email com o relatório

import win32com.client as win32
outlook = win32.Dispatch('outlook.application')#seleciona o aplicativo
mail = outlook.CreateItem(0)#cria o email
# mail.To = 'gahespanhol@gmail.com'#destino
mail.To = 'pege15@outlook.com.br'#destino
mail.Subject = 'Eu te amo!'#Titulo
# mail.HTMLBody = '''<html>
#                     <body>
#                     <p>For your eyes only,<br> I show my <strong>HEART!</strong>
#                     </body>
#                     </html>'''


mail.HTMLBody = '''
Prezados,

Faturamento:
{}

Quantidade de produtos vendidos por cada loja:
{}

Ticket Médio:
{}


Qualquer dúvida estou a disposção!

Att.,
Pedro.

'''

mail.Send()



# print(tabela_vendas)


