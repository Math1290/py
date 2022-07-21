name = input('Digite o seu nome completo:').strip()
play = name.split()
print('-' * 30)
print(f'Muito prazer em te conhecer {play[0]}!!!!! \n'
      f'Você se chama = {name} \n'
      f'O seu preimeiro nome é = {play[0]} \n'
      f'O seu último nome é = {play[-1]}')
print('-' * 30)