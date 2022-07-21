n1 = str(input('Digite o seu primeiro nome:'))
up = n1.upper()
nl = n1.lower()
t1 = n1.replace(' ', '')
pm = n1.split()
print('-'*22)

print(f'O seu nome com todas as letras em maiúsculo fica {up}')
print(f'O seu nome com todas as letras em minúsculo fica {nl}')
print(f'O seu nome sem espaços algum fica {t1}, e ele tem no total {len(t1)} caracteres!!!!!!')
print(f'O seu primeiro nome é {pm[0]} e ele tem no total { len(pm[0])} caracteres!!!!' )


print('-'*22)