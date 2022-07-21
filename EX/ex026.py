frase = input('Digite uma frase pequena:').upper().strip()
t = frase.count('O')
f = frase.find('O') + 1
u = frase.rfind('O') + 1
print(f'a letra = o, aparece  na frase {t} vezes \n'
      f'a primeira letra o está localizada a partir da {f} posição \n'
      f' a ultima letra o está localizada a partir da {u} posição')
