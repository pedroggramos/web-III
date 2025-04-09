#Operadores

# result = (5 + 3) * 2 **3 / 4

# print(f"O resultado = {result:.2f}")

# a,b,c,d = 1,2,3,4

# div = a / b
# resto = a % b
# int = a // b
# potencia = a**b

# Valores externos

# x = int(input("Digite o valor de x: "))
# y = int(input("Digite o valor de y: "))

# print(f"A divisão de {x} / {y} = {x / y}")

# x1 = input('Digite o valor de x1 ')
# x2 = input('Digite o valor de x2 ')

# x1 = int(x1)
# x2 = float(x2)


#Em python nao exite encremento/decremento podemos usar += e -=

# contador = 0
# contador += 1

# print(contador)

# contador -= 2
# print(contador)


#operações relacionadas >,<, <=, <=, ==, !=

# a,b = 10,20

# print(a == b)#false
# print(a != b)#true
# print( a > b)#false

#Comprações encadeadas

# nota = 8

# print(7 <= nota <= 10)#True

#operadores lógicos and, or, not

# idade = 18
# possui_cnh = True

# print(idade >= 18 and possui_cnh)#True

# c = 5
# d = 10

# print (c > 2 and d < 15)#True
# print(c > 2 or d > 15 )#True
# print(c > 5 or d < 10 )#True

# print(not possui_cnh)#False

# operador de associação in, not in

# n1 = [1,2,3,3,4,5,6,7]

# print(4 in n1)
# print(20 in n1)
# print(20 not in n1)


#importar módulos

# import math

#potencia - pow(), raiz quadrada - sqrt()

# n1 = int(input('Digite o valor da base '))
# n2 = int(input('Digite o valor da potencia '))

# n3 = math.pow(n1,n2)
# s = math.sqrt(n1)

#Arrendondar - ceil, floor, round

# print(f"Raiz quadrada {n2} = {round(s,2)}")
# print(f"A raiz quadrada {s} = {math.ceil(s)}")
# print(f"A raiz quadrda {s} = {math.floor(s)}")

#trunc - parte inteira do numero

# x3 = float(input('Digite o valor de x3 '))
# print(f'a parte inteira do numero {x3} = {math.trunc(x3)}')

#random

# import random

#random() - numeros aleatorios entre 0 - 1

# r = random.random()
# print(f'{r:.1f}')

# print(random.random() * 10)

# from random import randint, randrange, uniform, choice, shuffle

# # print(randint(1,10)) #numeros aleatorio inteiro
# # print(uniform(2,10)) #numero flutuante aleatório definindo intervalo
# # print(randrange(0,20,2)) #numero aleatorio flutuante definindo intervalo


# i = int(input('Digite o valor inicial '))
# f = int(input('Digite o valor final '))

# print(randint(i,f))

# l = [1,2,3,4,5,6,7]
# print(choice(l)) #escolhe um elemento da lista de forma aleatoria

# shuffle(l) #embaralha
# print(l)


#len() - qunatidade de carcteres

# nome = input('Digite o seu nome ')

# print(f'O nome da pessoa é {nome} esse nome possui {len(nome)} caracteres.')

# #upper() - lower() - swapcase()

# print(nome.upper())
# print(nome.lower())
# print(nome.swapcase())

# find() - mostra posição de determinado elemento

# v = 'Hoje tá osso!'

# print(f"A posição da palavra osso é: {v.find('á')}")

# replace() - altera a string sem alterar a string principal

# n = 'Maria'
# print(f"O novo nome é {n.replace('Maria', 'Pedro')}")

#count() - mostra a quantidade de vezes que determinado elemento repete

# x = 'Programação'
# print(f'A quantidade de vezes que a letra a repete é {x.count("a")}')

# split() - dividir string

# z = '   Bom dia!   '
# print(z.split())

# join() - concatena uma sequencia escolhendo o separador

# print('-'.join(z.split()))
# print(' '.join(z.split()))
# print('*'.join(z.split()))

# # strip() - remove um espaço inicial e final
# # lstrip - remove o da esquerda
# # rstrip - remove o da direita

# print(z)
# print(z.strip())
# print(z.lstrip())
# print(z.rstrip())


# -------------------

# if/else/elif

# a = int('Digite o valor de a: ')
# b = int('Digite o valor de b: ')

# if a > b:
#        print(f'O valor {a} é maior que o valor  {b}')
# else:
#     print(f'O valor {a} não é maior que o valor {b}')

# --------------------------

# nome = input('Digite seu nome: ')
# if nome == 'Pedro':
#      print(f'Oi!Seja bem vindo {nome}!')
# print(f'Bom dia {nome}!')

# # -------------

# idade = int(input('Digite sua idade: '))
# if idade >= 18:
#     print(f'A pessoa tem {idade} anos já pode dirigir.')
# else:
#     print(f'A pessoa tem {idade} anos não pode dirigir.')

# # ---------------------------

# c = int(input('Digite o valor de c: '))
# d = int(input('Digite o valor de d: '))

# res = 0
# op = input('Digite a operação: +,-,*,/ ')
# if op == '+':
#     res = c + d
#     print(f'A soma {c} + {d} = {res}')
# elif op == '-':
#     res = c - d
#     print(f'A subtração {c} - {d} = {res}')
# elif op == '*':
#     res = c * d
#     print(f'A multiplicação {c} * {d} = {res}')
# elif op == '/':
#     res = c / d
#     print(f'A divisão {c} / {d} = {res}')
# print('Término do calculo.')

# --------------------

# numero = int(input("digite seu numero: "))
# if numero <= 10 and numero % 2 == 0:
#      print(f'O valor {numero} é menor que 10 e é par')
# else:
#     print('Não atende a condição')

# FOR

# e = 0
# f = 10
# for i in range(e, f):
#     print("Olá!")
        

# ------------

# for j in range(10):
#     print(j)

# --------------

# for numero in range(1,11):
#     if numero % 2 == 0:
#         print(f'O numero {numero} é par.')
#     else:
#         print(f'O numero {numero} é impar.')

# ------------- de 2 em 2

# for num in range(10,40,2):
#     print(f'Numero: {num}')

# break------------

# for n in range(10):
#     if n > 6:
#         break
#     print(f'Numero: {n}')
# print('Fim')


# tabuada-----------

# t = int(input('Digite o valor da tabuada desejada: '))
# for tabuada in range(0,11):
#     print(f'{t} x {tabuada} = {t * tabuada}')

# -------------

# nome = 'Thereza'
# for p,v in enumerate(nome):
#     print(f'{p} {v}')

# while ---------------

# n = 1
# while n != 0:
#     n = int(input(f"Digite o valor: "))
# print("terminou")

# ----------

# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input(f'Digite o valor: '))
#     if n != 0:
#         if n % 2 == 0:
#             par += 1
#         else:
#             impar += 1
# print(f"Você digitou {par} numeros pares e {impar} impares")

# ---------------

# num = 0
# while num < 5:
#     num += 1
#     if num == 3:
#         break
#     print(num)

# -------------

# import random

# from random import randint

# c = randint(1,10)
# print('Tente adivinhar o numro...')

# acerto = False
# while not acerto:
#     j = int(input('Qual o seu palpite?: '))
#     if j == c:
#         acerto = True
#         print('Acertou!😊')
#     else:
#         print('Errou!Tente novamente!🤷')

# -----------------------

# x = int(input('Digite um numero: '))
# y = int(input('Digite outro numero: '))

# op = 0
# while op != '5':
#     print('''
#     [1]Somar
#     [2]Subtrair
#     [3]Multiplicar
#     [4]Dividir
#     [5]Sair''')
#     op = input('Escolha a opção desejada: ')

#     if op == '1':
#         print(f'A soma {x} + {y} = {x + y}')
#     elif op == '2':
#         print(f'A subtração {x} - {y} = {x - y}')
#     elif op == '3':
#         print(f'A multiplicação {x} * {y} = {x * y}')
#     elif op == '4':
#         print(f'A divisão {x} / {y} = {x / y}')
#     elif op == '5':
#         print('Termino do programa!')
#     else:
#         print('Opção invalida!')
#     print('Fim do programa!')

# --------------------

# --------------------

# tuplas()

# a = (1,2,3,4,5,'Thereza', True)
# print(a)
# print(a[4])
# print(a[-3])
# print(a[1:4])
# print(a[3:])
# print(a[:3])

# concatenação de tupla - +

# b = (1,2,3,4,5)
# c = (6,7,8,9,10)

# d = b + c

# print(d)
# print (b + c)

# len() - mostra a quantidade elementos de uma tupla ou lista

# nome = ('Thereza', 'Pedro', 'Gabi', 'Valentina')
# t = len(nome)
# print(f"A quantidade de elementos da tupla é {t}")
# print(f"A quantidade de elementos da tupla é {len(nome)}")

# -- FOR -----------------------


# for i in range(0,len(nome)):
#     print(f'Olá! {nome[i]}.Bom dia!')

# for i in range(len(nome)):
#     print(f'Olá! {nome[i]}.Bom dia!')


# # del()------------

# e = (1,2,3,4,5)
# print(e)

# del(e)
# print(e)

# e = (1,2,3,4,5)
# del(e[1][3])
# print(e) #TUPLAS SÃO IMUTAVEIS

# ----------------------------

#count() - mostra a quantidade de vezes que um determinado elemento repete

# f = (1,4,5,2,3,4,8,9,4)
# print(f'O numero 4 repete {f.count(4)} vezes')
# print(f'O numero 1 repete {f.count(1)} vezes')


#index() - mostra a posição de um determinado elemento
# e quando houver repetição ele mostra primeira posição do valor
# repetido ----------


# print(f'O indice da primeira posição é {f.index(4)}')
# print(f'O indice da primeira posição é {f.index(9)}')

#Lista() - conjunto de dados, mutavel, sua representação é [] ----

# a = [1,2,3,4,5,'Thereza',True]
# print(a)
# print(a[4])
# print(a[-3])
# print(a[1:4])
# print(a[3:])
# print(a[:3])

# a[-2] = 'Paulo'
# print(a)

# i = [1,[1,2,3],4,5,6,[7,8,9],False]
# print(i)
# print(i[5][0])
# print(i[1][-1])


# 
#concatenar lista ----------------------------------------------

# b = [1,2,3,4,5]
# c = [6,7,8,9,10]

# print(b + c)

#append() - inserir novos elementos no final da lista ---------

# b.append('Marcelo') #nome inteiro
# print(b)

# b.extend('Marcelo') #um por um
# print(b)

#recebendo valores externos ------------------------------------

# aluno = [] #ou list()

# nome1 = input('Digite o nome do aluno: ')
# nome2 = input('Digite o nome do aluno: ')
# nome3 = input('Digite o nome do aluno: ')
# nome4 = input('Digite o nome do aluno: ')
# aluno.append(nome1)
# aluno.append(nome2)
# aluno.append(nome3)
# aluno.append(nome4)
# print(aluno)


# aluno = []
# nome1 = input("Digite o nome do aluno: ")
# nome2 = input("Digite o nome do aluno: ")
# nome3 = input("Digite o nome do aluno: ")
# nome4 = input("Digite o nome do aluno: ")
# aluno.append(nome1)
# aluno.append(nome2)
# aluno.append(nome3)
# aluno.append(nome4)
# print(aluno)



# -----------------

# numero = list()
# for i in range(10,30,2):
#     numero.append(i)
# print(numero)

# --------------

#insert() - inserir novos elementos na lista escolhendo a posição desejada

# k = [1,2,3,4,5]
# print(k)
# k.insert(3,'A')
# print(k)

# remove() - remover um determinado elemento da lista 

# k.remove('A')
# print(k)
# del(k[3])
# print(k)

#max() - mostra o maior valor da lista ------------------------

# m = [100,20,30,40,1,12]
# print(f'O maior valor da lista é {max(m)}')

# #min() - mostra o menor valor da lista ------------------------

# m = [100,20,30,40,1,1]
# print(f'O menor valor da lista é {min(m)}')

# ----------------

# nota = [] * 3
# for a in range(0, len(nota)):
#     nota[a] = float(input('Digite as notas: '))
# media = ((nota[0] + nota[1] + nota[2]) / 3)
# print(f'A media do aluno é {media:.1f}')

#reverse() - inverte a lista

# n = [1,2,3,4,5,6]
# n.reverse()
# print(f"A lista invertida é{n}")

# ----------------------------

# d = []

# for i in range(5):
#     num = float(input("Digite um numero: "))
#     d.append(num)

# d.reverse()
# print(f"A lista invertida é: {d}")

#sum() - soma todos os valores da lista ---------------

# print(f"a soma dos valores da lista é de {sum(d)}")

#pop() apagar o ultimo elemento da lista ------------------

# x= [1,2,3,4,5]
# x.pop()
# print(x)

# x.pop(2)
# print(x)

#del() - apagar elementos da lista, podendo ainda de finir o intervalo

#del(x)
# del(x[1:3])
# print(x)

# l = ['b','l','c','a']
# l.sort()
# print(l)
# l.sort(reverse=True) #ordem decrescente
# print(l)
# l.reverse()
# print(l)

# #exemplo mostrando o indice e o valor ----------------------

# lista = [10,20,30,40,50]
# for i,v in enumerate(lista):
#     print(f'Indice = {i} Valor = {v}')


# DICIONARIO E FUNÇÕES

#dicionario - nome do diciconario = {'chave:'valor}

d = {}
# e = dict()
# print(d)
# print(e)
# f = []
# g = ()
# print(type(d))
# print(type(f))
# print(type(g))

# ------------------

# if not d:#conjuntos vazios são False
#     print("O dicionário está vazio")
# else:
#     print("O dicionário não está vazio")

# ----------------

# aluno = {
#     'nome': 'Thereza',
#     'idade': 27,
#     'sexo': 'F',
#     'email':'teste2@gmail.com'
# }

# print(aluno)
# print('Nome: ', aluno['nome'])
# print('Idade: ',aluno['idade'])

# aluno['nome'] = "Pedro Gabriel"
# print("Nome: ", aluno['nome'])
# aluno['nacionalidade'] = 'Brasileira'
# print(aluno)
# del aluno['sexo']
# print(aluno)

# -------------------------

#keys() - mostra a chave
#values() - mostra os valores
#items() - mostra a chave e os valores

# filme = {'titulo':'Moana','ano':2017,'diretor':'Jonh Musker'}
# print(filme)
# print(filme.keys())
# print(filme.values())
# print(filme.items())

# ------------------

# d1 = {'a':1,'b':2,'c':3}
# for c in d1.values():
#     print(f'Valor: {c}')


# ------------------------

# notas ={
#     "G1": float(input("Nota 1: ")),
#     "G2": float(input("Nota 2: ")),
#     "G3": float(input("Nota 3: "))
# }
# for c, v in notas.items():
#     print(f"{c} Nota: {v}")

# -------------------

# pessoa = {}
# pessoa['nome'] = str(input("Digite seu nome: "))
# pessoa['idade'] = str(input("Digite sua idade: "))
# pessoa['sexo'] = str(input("Digite o seu sexo[F/M]: "))

# for c,v in pessoa.items():
#     print(f"{c} = {v}")

#update() ----------------------------------------------------------

# d2 = {'nome':'Paulo'}
# print(d2)

# d2.update({'nome':'Paulo Milhomem'}) #atualiza os dados
# print(d2)

# d2.update({'idade':22})#inserir nova chave no dicionario
# print(d2)

# d2.pop('idade') #deleta o ultimo elemento do dicionário
# print(d2)

# d3 = {'a':10,'b':20,'c':30}
# d4 = {'d':40,'e':50,'f':60}

# d3.update(d4) #concatena dicionarios
# print(d3)

# copy() - para fazer uma copia do dicionario

# aula 5 continuar!!!!!!!!!!!!!!!!!!