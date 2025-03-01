# 1 -------------------------------

# dados = (2,0.5,'Pedro',True)

# print(dados[1],dados[3])

# del(dados[1])
# print(dados) #Erro! Pois uma tupla é um conjunto de dados imutável

# 2 -------------------------------

# a = (1,2,2,3,2)

# print(f'O numero 2 aparece {a.count(2)} vezes')

# 3 -------------------------------

# x = [20,40,60,80]

# x.append(100)
# del(x[2])
# del(x[0])
# x.insert(0,500)
# print(x)

# 4 -------------------------------

# notas = [0] * 5

# for i in range(0, len(notas)):
#     notas[i] = float(input("Inserir nota: "))

# soma = sum(notas)
# media = soma / len(notas)

# print(soma)
# print(media)

# 5 -------------------------------

# lista = [0] * 5

# for i in range(0, len(lista)):
#     lista[i] = float(input("Inserir numero: "))

# lista.sort()
# print(lista)
# lista.sort(reverse=True)
# print(lista)

# print([num for num in lista if num > 10])

# 6 -------------------------------

# alunos = ['Pedro', 'Gabi', 'Valentina']
# matriz = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]

# maior_media = 0
# alunoMaior = ''

# print(matriz[1][2])

# for i in range(0, len(matriz)):
#     media = sum(matriz[i]) / len(matriz[i])

#     if media > maior_media:
#         maior_media = media 
#         alunoMaior = alunos[i]

# print(f"O aluno com a maior média é: {alunoMaior} com média {maior_media:.2f}")

# 7 -------------------------------

# lista = [0] * 4

# for i in range(len(lista)):
#     lista[i] = float(input(f"Digite o numero: "))

# print(f'O numero 9 apareceu {lista.count(9)} vezes')
# print(f'O primeiro valor 3 está na posição {lista.index(3)}')
# pares = [num for num in lista if num % 2 == 0]
# print(f'Os numeros pares foram: {pares}')

# 8 -------------------------------

# import random

# lancamentos = []

# for _ in range(50):
#     resultado = random.randint(1,6)
#     lancamentos.append(resultado)

# ocorrenciaSeis = lancamentos.count(6)
# percentualSeis = (ocorrenciaSeis / 50) * 100

# print(f'A face 6 apareceu {ocorrenciaSeis} vezes')
# print(f'O percentual de ocorrencia da face 6 é de {percentualSeis:.2f}%')




