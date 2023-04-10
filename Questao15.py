#  crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5

numeros_menores_cinco = []

for i in range(1,6):
    num = int(input('Informe os numeros: '))
    numeros_menores_cinco.append(num)

print('Os numeros informados menores do que cinco, sao: ')
for num in numeros_menores_cinco:
    if num < 5:
        print(num)
