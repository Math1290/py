import random

studentone = input('Digite o primeiro aluno:')
studenttwo = input('Segundo aluno:')
studenttree = input('Terceiro aluno:')
studentfor = input('Quarto aluno:')
list = [studentone, studenttwo, studenttree, studentfor]
escolhido = random.choice(list)
print(f'O escolhido foi {escolhido}')