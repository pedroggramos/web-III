# Teste pra gabi cmainhões -----------------------

# import win32com.client as win32
# outlook = win32.Dispatch('outlook.application')#seleciona o aplicativo
# mail = outlook.CreateItem(0)#cria o email
# mail.To = 'gahespanholl@gmail.com'#destino
# # mail.To = 'pege15@outlook.com.br'#destino
# mail.Subject = 'Eu te amo, minha bibizoca!'#Titulo
# mail.HTMLBody = '''<html>
#                     <body>
#                     <p style="color:#FFB6C1;font-size: 20pt">For your eyes only,<br> I'll show you my <strong style = "color:red!important;">HEART!</strong>
#                     <br>
#                     For when you're lonely and forget who you are.
#                     </p>
#                     <br>
#                     <h1 style="color:red">Eu te amo!</h1>
#                     <br>
#                     <br>
#                     <p style = "color:blue;">E-mail enviado via código Python by Pedro Ramos.</p>
#                     </body>
#                     </html>'''


# Juntando PDFs e depois mandando email

#
from PyPDF2 import PdfMerger #biblioteca
#
merger = PdfMerger() #nomear
#
# merger.append("Pedro Gabriel Guimarães Ramos - Curriculo.pdf")
# merger.append("Histórico Escolar.pdf")
# merger.append("declaracaomatricula.pdf")
# merger.write("documentos.pdf")#escrever em um novo pdf
# merger.close()

#Criar o pdf com o código----------------

from reportlab.pdfgen import canvas

def criarPaginaCodigo(nome_arquivo):
    c = canvas.Canvas(nome_arquivo)
    c.setFont("Helvetica", 12)
    texto = """
Este PDF foi montado via código Python.

Código usado:
from PyPDF2 import PdfMerger  # biblioteca

merger = PdfMerger()  # nomear

merger.append("Pedro Gabriel Guimarães Ramos - Curriculo.pdf")
merger.append("Histórico Escolar.pdf")
merger.append("declaracaomatricula.pdf")

merger.write("documentos.pdf")  # escrever em um novo pdf
merger.close()


#Criar o pdf com o código----------------

from reportlab.pdfgen import canvas

def criarPaginaCodigo(nome_arquivo):
    c = canvas.Canvas(nome_arquivo)
    c.setFont("Helvetica", 12)
    texto = ....
    
    
     y = 800
    for linha in texto.strip().splitlines():
        c.drawString(50, y, linha)
        y -= 20
    c.save()

# Cria o pdf
criarPaginaCodigo("paginaDeCodigo.pdf")

#Juntando novamente

merger.append("documentos.pdf")
merger.append("paginaDeCodigo.pdf")
merger.write("documentosProcessoSeletivo.pdf")
merger.close()
    

"""

    y = 800
    for linha in texto.strip().splitlines():
        c.drawString(50, y, linha)
        y -= 20
    c.save()

# Cria o pdf
criarPaginaCodigo("paginaDeCodigo.pdf")

#Juntando novamente

merger.append("documentos.pdf")
merger.append("paginaDeCodigo.pdf")
merger.write("documentosProcessoSeletivo.pdf")
merger.close()


#Enviando via Outlook-------------

# import win32com.client as win32
# import os
#
# outlook = win32.Dispatch("Outlook.application")
# email = outlook.CreateItem(0)
#
# email.To =""
# email.Subject = ""
# email.BodyHTML='''
# '''
#
# email.Attachments.Add("documentos.pdf")
#
# email.send()

