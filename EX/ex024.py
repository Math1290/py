city = input('Digite o nome da cidade aonde vc mora:')
a = city.split()
play = 'Santo' in a[0]
print(f'A sua cidade se chama = {city} \nE ela começa com santo? = {play}')