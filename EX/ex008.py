meters = float(input('Digite a quantidade me metros: '))
centimeters = meters * 100
milimeter =  meters * 1000
km = meters / 1000
hm = meters / 100
dam = meters / 10
dm = meters * 10
print(f'E a conversão de {meters}m para km é = {km}km \nE a conversão de {meters}m para hm é = {hm}hm  \nE a conversão de {meters}m para dam é = {dam}dam ')
print(f'E a conversão de {meters}m em dm é = {dm :.0f}dm \nE a conversão de {meters }m em cm é = {centimeters :.0f}cm \nE a conversão de {meters}m para mm é = {milimeter :.0f}mm')
