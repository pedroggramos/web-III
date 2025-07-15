# aula 1 ------

# Tipos de dados e prints

# int
idade = 15

# float
altura = 1.61

# string

nome = "Pedro"

# Booleano

aprovado = True

# print(nome, idade, altura, aprovado)
# print(nome + idade + altura + aprovado) #erro

# print(2 + 2) #soma
# print(2,2) #printa
#print('5'+ 5) #erro
# print('Olá'+'5')#printa
#print('Olá'+ 5) #erro
# print('Olá'+''+ '5')#printa
# print('Olá','5')#printa

# print('Olá!\nBoa Noite!\nSejam Bem vindos!')
#
# nome = "Pedro"
# sobrenome = "Ramos"
#
# # print(nome,sobrenome)
# # print(nome + " " + sobrenome)
# # print(f'O nome dele é {nome + " " + sobrenome}')
#
# a = 10
# b = 20
# c = 2.454355
# print(a,b,c)

# .format-------------

# print('O valor de a = {}'.format(a))#usando o .format
# print('O valor de b = {}'.format(b), 'O valor de c = {:.2f}'.format(c))
# print('O valor de b = {}, o valor de c = {}'.format(b,c))
#
# print(f'O valor de b = {b}, o valor de c = {c:.2f}')

# aula 2 ----------------

# OPERADORES ARITMÉTICOS

# n1, n2, n3, n4 =  2,4,6,8.5
# s = n1 + n2 + n3 + n4
# sub = n4 - n1
# div = n2 / n4
# resto = n1 % n2 #resto da divisao
# i = n2 // n4#inteiro da divisao #result = 0 pois o resultado é 0.5 e o inteiro é o 0
# p = n1 ** n2#potencia

# print('A soma dos valores = ',s)
# print('A soma dos valores = {}'.format(s))
# print(f'A soma dos valores = {s}')
#
# print('A subtração dos valores = ', n3 -4)
# print('A subtração dos valores = {}'.format(n3-n4))
# print(f'O inteiro da divisão = {i}')
#
# print(f'O valor de {n2} elevado a {n4} potencia = {n2**n4}')

# OPERAÇÕES COMBINADOS -------------

# resultado = (5+3) * 2 ** 3/4
# print(f'Operação combinada = {resultado}')


#CONVERTER INPUT--------------

# x1 = input("Digite o valor de x: ")
# y2 = input("Digite o valor de y: ")
#
# x1 = int(x1)
# y2 = float(y2)
#
# print(f'A multiplicação de {x1} * {y2} = {x1 * y2}')

#no python não temos incremento nem decremento, podemos usar += ou -=

# contador = 0
# contador += 1
#
# print(f'Incremento: {contador}')
#
# contador -= 2
# print(f'Decrmento: {contador}')

# OPERADORES RELACIONAIS >, <, >=, <=, ==, != ----------------------

# a,b = 10, '10'
# print(a == b)
# print(a != b)

#OPERADORES ENCADEADOS ------------

# nota = 6.9
# print(7 <= nota <= 10)

# OPERADORES LÓGICOS and, or, not ------------------------

# idade = 10
# possui_cnh = True
#
# print(idade > 18 and possui_cnh)
#
a,b = 5,10
# print(a > 2 and b < 15)

# ------------------------

# tem_cartao = False
# tem_dinheiro = False
#
# print(tem_cartao or tem_dinheiro)
#
# print(a > 5 or b < 15)
#
# ativo = True
# print(not ativo)

# OPERADOR IN E NOT IN -------------------

# numero = [1,2,3,4]
#
# # verifica se existe o numero na lista
# print(2 in numero) #true
# print(20 not in numero) #true

# Math -----------------

import math

# pow() - potencia --------------

# x1 = int(input("Digite o valor base: "))
# y1 = int(input("Digite o valor da potencia: "))

# print(f'O numero {x1} elevado a {y1} = {math.pow(x1,y1):.0f}')
#
# m = math.pow(x1, y1)
# print(f'O numero {x1} elevado a {y1} = {m:.0f}')

# sqrt() ---------------

# r = math.sqrt(x1)
# print(f'A raiz quadrada de {x1} = {r:.2f}')
#
# r1 = math.sqrt(math.pow(x1,y1))
# print(f'A raiz quadrada de {x1} elelevado a {y2} = {r1:.2f}')

# ARREDONDAMENTO - round, ceil, floor -----------------------

# print(f'A raiz quadrada de {r} = {round(r,0)}')
# print(f'A raiz quadrada de {r} = {math.ceil(r)}')
# print(f'A raiz quadrada de {r} = {math.floor(r)}')

# OUTRA FORMA DE IMPORTA

from math import pow,sqrt, trunc

# x2 = float(input('Digite o valor base: '))
# y2 = int(input('Digite o valor da potencia: '))
#
# print(f'O numero {x2} elevado {y2} = {pow(x2,y2)}')

# TRUNC - traz a parte inteira do número
#
# print(f'A parte inteira do numero {x2} = {trunc(x2)}')

# NUMEROS RANDOMICOS --------

import random

# numeros aleatorios entre 0 e 1 --------------

# r1 = random.random()
# print(round(r1, 2))
# print(f'O numero aleatorio é {r1}')
# print(f'O numero aleatorio é {r1:.2f}')

#numeros aleatorios entre 0 e 10 --------------------
#
# r2 = (random.random() * 10)
# # print(round(r2))
# print(f'O numero aleatorio é {round(r2)}')

# radint() - inteiro entre dois numeros----------

# print(random.randint(10,40))

from random import randrange,uniform, choice, shuffle

# r3 = randrange(5,25)
# print(r3)
# r4 = randrange(5,25, 2)#de 2 em dois entre 5 e 25
# print(r4)
#
# r5 = uniform(0,15) #inclui os decimais
# print(r5)
# print(f'{r5:.2f}')
#
# x1 = float(input('Digite o valor inicial: '))
# x2 = float(input('Digite o valor final: '))
#
# x3 = uniform(x1, x2)
# print(f'{x3:.2f}')
#
t = [1,2,3,4,5,6]
# print(choice(t)) #escolhe um da lista

# random.shuffle(t) #bagunça a lista
# print(t)

# ANALISAR STRING ----------------------

#len(var) - quantidade de caracteres --------------------------------

# nome = input('Digite o seu nome')
# print(f'O nome do usuario é {nome} e a quantidade de caracteres = {len(nome)}')

#.upper() - maiusculo --------------------------------------------

# print(nome.upper())

#lower() - minusculo ---------------------------------------------

# print(nome.lower())

#.find('') - mostra a posição de uma determinada string ---------------

# m = ('Hoje tá osso')
# print(f'A posição da palavra osso {m.find('osso')}')

#.replace() - altera o valor da string sem alterar a string principal ---

# print(f'A nova palavra é {m.replace('Hoje','Amanhã')}')

#count() - quantidade de vezes que um determinado elemento repete -----

# print(f'A quantidade de vezs que o caracter repete: {m.count('o')}')

#split() - divide a string transformando em uma lista --------------

# v = 'Boa noite!'
# print(v.split())

#.join(v) - alterar o separador -----------------------------------------

# print('-'.join(v))

#.swapcase() - inverte a string maiusculo para minusculo e vice versa --------

# print(nome.swapcase())

#strip() - remove os espaços inicial e final -----------------------

# s = ('     Boa noite!       ' )
# print(s.strip())
#
# print(nome.strip())

#lstrip() - remove o espaço da esquerda

# print(nome.lstrip())

#rstrip() - - remove o espaço da direita ------------

# print(nome.rstrip())


# AULA 3 -------------------

#Estrutura condicional if/else/elif

# a = input('Digite o valor de a: '))
# b = int(input('Digite o  valor b: '))
#
# if a == b:
#     print(f'O valor de {a} é igual a {b} ?')
# else:
#     print(f'O valor de {a} não é igual a {b} ?')

#--------------------------------------------------

M# if nome == 'Gustavo':
#     print(f'Oi!!Esse nome {nome} é maravilhoso!')
# print(f'Boa noite {nome}!')

#---------------------------------------------------