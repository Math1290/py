from math import cos, sin, radians, tan

num = float(input('Digite o valor do ângulo:'))
res = cos(radians(num))
ress = sin(radians(num))
restan = tan(radians(num))
print(f'O valor de {num} tem o COSSENO de {res :.2f} \nO valor de {num} tem o SENO de {ress :.2f} ')
print(f'O valor de {num} tem o tangente de {restan :.2f}')
