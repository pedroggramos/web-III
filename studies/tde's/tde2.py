# 1)

# n = int(input("Digite um numero: "))

# if n > 0:
#     print(f'{n} é um numero Positivo')
# elif n < 0:
#     print(f'{n} é um numero negativo')
# else:
#     print(f'Numero zero!')

# --------------------------------

# 2)


# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# n3 = float(input("Nota 3: "))

# media = (n1 + n2 + n3) / 3

# if media >= 7:
#     print(f'Aprovado')
# elif media < 5:
#     print(f'reprovado')
# else:
#     print(f'recuperação')


# ------------------------------------------

# 3)

# n1 = float(input("N1: "))
# n2 = float(input("N2: "))

# if n1 % n2 == 0:
#     print(f"Sim")
# else:
#     print(f"Não")


# ----------------------------

# 4)

# n1 = int(input("n1: "))
# n2 = int(input("n2: "))
# n3 = int(input("n3: "))

# if n1 < n2 < n3:
#     print(f'Ordem decrescente')
# else:
#     print(f'Não está em ordem decrescente')

# ---------------------------------------

# 5)

# num = int(input("Numero: "))

# if num > 0:
#     cont = 0
#     for i in range(1, num + 1, 2):
#         cont += 1
#     print(f'Quantidade de numeros ímpares é de 1 até {num} é de {cont}')
# else:
#     print(f'Inválido')

# ---------------------------------

# 6)

# num = int(input("Numero: "))

# if num < 0:
#     print(f"Inválido")
# else:
#     fatorial = 1
#     for i in range(1,num + 1):
#         fatorial *= i
#     print(f"O fatorial de {num} é: {fatorial}")

# ---------------------------------------------

# 7)

# num = input("Numero: ")

# qtdDigitos = len(num)

# print(f"O numero {num} tem {qtdDigitos} dígitos")

# ----------------------

# 8)
# num = int (input("Numero: "))

# soma_divisores = 0
# for i in range(1, num):
#     if num % i == 0:
#         soma_divisores += i

# if soma_divisores == num:
#     print(f"{num} é um numero perfeito")
# else:
#     print(f"{num} não é um numero perfeito")

# ---------------------

# 9)

# n = int(input("numero de sequencias: "))

# t1 = 0
# t2 = 1

# for i in range(n):
#     print(t1)
#     t1,t2 = t2, t1 + t2

# ---------------------------


# 10)

# base = int(input("base: "))
# limite = int(input("limite: "))

# print(f"TABUADA DE {base}")
# print(f"")


# for i in range(1,limite):
#     print(f"{base} x {i} = {base * i}")





