import math
import random
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
random.shuffle(lista)
print(f'O aluno escolhido foi {lista}')
print('o aluno escolhido foi {}'.format(escolhido))

