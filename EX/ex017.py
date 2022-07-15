import math
catetoa = float(input('Digite o comprimento de um cateto:'))
catetob = float(input('Digite o comprimeto do segundo cateto: '))
hp = math.hypot(catetoa, catetob)
print(f'A hipotenusa vai medir {hp :.2f}')