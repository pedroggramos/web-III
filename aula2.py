#import random

# from random import randint

# c = randint( a: 1, b:10)
# print('Tente adivi1nhar o erro')

# acerto = False
# while not acerto:
#     j = int(input('Qual o seu palpite?: '))
#     if j == c:
#         acerto = True
#         print('Acertou!')
#     else:
#         print('Errou! Tente novamente')

# ---------------------------------

x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))

op = 0
while op != 5:
    print('''
          [1]Somar
          [2]Subtrair
          [3]Multiplicar
          [4]Dividir''')
    op = input('Escolha a opção desejada: ')
    
    if op == '1':
        print(f'A soma {x} + {y} = {x + y}')
    elif op == '2':
        print(f'A subtração {x} - {y} = {x - y}')
    elif op == '3':
        print(f'A multiplicação {x} * {y} = {x * y}')
    elif op == '4':
        print(f'A multiplicação {x} / {y} = {x / y}')
    elif op == '5':
        print('Termino do programa!')
        break
    else:
        print('Opção Inválida!')
    
print('Fim do programa!')
        
        
        