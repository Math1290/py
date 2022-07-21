city = input('Digite o nome da cidade aonde vc mora:').strip()
a = city[:5].upper()
play = a == 'SANTO'
print(f'A sua cidade se chama = {city} \nE ela começa com santo? = {play}')