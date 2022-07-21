import random

n1 = input('Digite o primeiro nome:')
n2 = input('Digite o segundo nome:')
n3 = input('Digite o terceiro nome:')
n4 = input('Digite o quarto nome:')
l1 = [n1, n2, n3, n4]
e1 = random.shuffle(l1)
print(f'A ordem de apresentação será')
print(l1)

