frase = input('Digite uma frase pequena:')
t = frase.count('o')
f = frase.find('o')
u = frase.rfind('o')
print(f'a letra = o, está na frase {t} vezes \n'
      f'a primeira letra o está localizada a partir da {f} posição \n'
      f' a ultima letra o está localizada a partir da {u} posição')
