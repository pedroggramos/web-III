#tuplas() - conjunto de dados,é imutavel, é representado pelo ()

# a = (1,2,3,4,5,'Thereza',True)
# print(a)
# print(a[4])
# print(a[-3])
# print(a[1:4])
# print(a[3:])
# print(a[:3])

# b = (1,2,3,4,5,'Gabi', 'Pedro', True)

# print(b[5:7])

# concatenação de tupla - + -------------------------------------

# b = (1,2,3,4,5)
# c = (6,7,8,9,10)
# d = b + c
# print(d)
# print(b + c)

# b = (1,2,3,4,5,6,7,8,9,10)
# c = (11,12,13,14,15,16,17)

# d = b + c
# print(d)

# print(c + b)


#len() - mostra a quantidade de elementos de uma tupla ou lista -----

# nome = ('Thereza','Julia','Paulo','Marcelo')
# t = len(nome)
# print(f'A quantidade de elementos da tupla é {t}')
# print(f'A quantidade de elementos da tupla é {len(nome)}')


# # ----------------
# for i in range(2, len(nome)):
#     print(f'Olá! {nome[i]}. Bom dia!')

# for i in range (len(nome)):
#     print(f'Olá! {nome[i]}. Bom dia!')


# del()---------------------

# e = (1,2,3,4,5)
# print(e)

# e = (1,2,3,4,5)
# del(e[1][3])
# print(e) #resposta erro

# count() - mostra a quantidade de vezes que um determinado elemento repete


# f = (1,4,5,2,3,4,8,9,4)
# # print(f'O numero 4 repete {f.count(4)} vezes')
# # print(f'O numero 1 repete {f.count(1)} vezes')

# # index() - mostra a posição de um determinado elemento e quando houver repetição ele mostra primeira posição do valor

# print(f"O indice da primeira posição é {f.index(4)}")
# print(f'O indice da primeira posição é {f.index(9)}')

# ------------------

# Lista - conjunto de dados, mutavel, sua representação é [] ---

# a = [1,2,3,4,5,'Gabi', True]

# print(a)
# # print(a[4])
# # print(a[-3])
# # print(a[1:4])
# # print(a[3:])
# # print(a[:3])

# a[-2] = 'Pedro'
# print(a)

# i = [1,[1,2,3],4,5,6,[7,8,9],False]

# print(i)
# print(i[5][0])
# print(i[5][0:3])
# print(i[1][-1])

# Concatenar Lista ---------------------

# b = [1,2,3,4,5]
# c = [6,7,8,9,10]

# print(b + c)

# append() - inserir novos elementos no final da lista ---------

# b.append('Pedro')
# print(b)

# b.extend('123456789')
# print(b)

# recebendo valores externos -----


# aluno = [] #ou list()

# nome1 = input("Digite um nome: ")
# nome2 = input("Digite um nome: ")
# nome3 = input("Digite um nome: ")
# nome4 = input("Digite um nome: ")
# aluno.append(nome1)
# aluno.append(nome2)
# aluno.append(nome3)
# aluno.append(nome4)

# ----

# aluno = []

# for i in range(0,5):
#     nome = input("Digite seu nome: ")
#     aluno.append(nome)

# print(aluno)


# -----


# numero = list()
# for i in range(10,21,2):
#     numero.append(i)
# print(numero)


# insert() - inserir novos elementos da lista --------

# k = [1,2,3,4,5]
# print(k)
# k.insert(3,'A')
# print(k)

# remove() - remover determinado elemento da lista --------

# k.remove('A')
# print(k)

# max() - mostra o maior valor da lista ----------

# m = [100,20,30,40,1,12]
# print(f"O maior valor da lista é{max(m)}")

# min() - mostra o menor valor da lista -------

# print(f"O menor valor da lista é{min(m)}")

# --------------------------

nota = [0] * 3
for a in range(0,len(nota)):
    nota[a] = float(input(f"Digite as notas: "))
media = ((nota[0] + nota[1] + nota[2]) / 3)
print(f'A media de aluno é {media:.1f}')









