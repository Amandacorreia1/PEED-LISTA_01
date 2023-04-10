#  crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10

numeros_maiores_dez = []

for i in range(1,6):
    num = int(input('Informe os numeros: '))
    numeros_maiores_dez.append(num)

print('Os numeros informados maiores do que dez, sao: ')
for num in numeros_maiores_dez:
    if num > 10:
        print(num)
