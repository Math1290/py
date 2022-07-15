days = int(input('Quantos dias alugados?'))
km = float(input('Quantos KM rodados?'))
money = (days * 60) + (km * 0.15)
print(f'O total a pagar é de R${money:.2f}')