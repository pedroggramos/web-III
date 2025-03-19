# # Questão 1
# numeros_por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
# n = int(input("Digite um número entre 0 e 20: "))
# print(f"Você digitou {numeros_por_extenso[n]}")

# # Questão 2
# valores = [int(input(f"Digite um valor para a posição {i}: ")) for i in range(10)]
# unicos = len(set(valores))
# print(f"Quantidade de valores diferentes: {unicos}")

# # Questão 3
# valores = [int(input(f"Digite o {i+1}º valor: ")) for i in range(4)]
# print(f"O valor 9 apareceu {valores.count(9)} vezes.")
# print(f"O primeiro 3 apareceu na posição {valores.index(3) + 1}" if 3 in valores else "O valor 3 não foi digitado.")
# print(f"Números pares: {[num for num in valores if num % 2 == 0]}")

# # Questão 4
# from random import randint
# dados = [randint(1, 6) for _ in range(50)]
# percentual = (dados.count(6) / 50) * 100
# print(f"Percentual de ocorrência da face 6: {percentual:.2f}%")

# # Questão 5
# tradutor = {"hello": "olá", "world": "mundo", "dog": "cachorro", "cat": "gato"}
# entrada = input("Digite uma palavra em inglês: ").lower()
# print(f"Tradução: {tradutor.get(entrada, 'Palavra não encontrada')}")

# # Questão 6
# estoque = {}
# while True:
#     produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
#     if produto.lower() == "sair":
#         break
#     quantidade = int(input("Digite a quantidade: "))
#     estoque[produto] = estoque.get(produto, 0) + quantidade
# print("Estoque atualizado:", estoque)

# # Questão 7
# idades = [int(input("Digite a idade: ")) for _ in range(5)]
# alturas = [float(input("Digite a altura: ")) for _ in range(5)]
# print("Idades na ordem inversa:", idades[::-1])
# print("Alturas na ordem inversa:", alturas[::-1])

# # Questão 8
# texto = input("Digite um texto: ").lower()
# frequencia = {letra: texto.count(letra) for letra in set(texto) if letra.isalpha()}
# print("Frequência das letras:", frequencia)

# # Questão 9
# def media_notas(alunos):
#     media = sum(alunos.values()) / len(alunos)
#     return {"média": media}
# alunos = {"Pedro": 8, "Ana": 7.5, "Carlos": 9}
# print(media_notas(alunos))

# # Questão 10
# texto = input("Digite um texto: ").lower().split()
# contagem = {palavra: texto.count(palavra) for palavra in set(texto)}
# print("Contagem de palavras:", contagem)

# # Questão 11
# def verifica_sinal(n):
#     print("Positivo" if n > 0 else "Negativo")

# # Questão 12
# def valor_absoluto(n):
#     print(abs(n))

# # Questão 13
# def soma_maior_que_limite(a, b, limite):
#     return (a + b) > limite

# # Questão 14
# def somaImposto(taxaImposto, custo):
#     return custo + (custo * taxaImposto / 100)

# # Questão 15
# def quantidade_digitos(n):
#     print(len(str(abs(n))))
