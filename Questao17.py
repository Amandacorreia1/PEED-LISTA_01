# Crie um programa que leia uma lista de números do usuário e exiba a soma dos números impares.

soma_impares = []
soma = 0

for i in range(1,6):
    num = int(input('Digite os numeros: '))
    if num % 2 != 0:
        soma_impares.append(num)
        soma = soma + num

print('Os numeros impares digitados')
for num in soma_impares:
    print(num)
print('A Soma dos numeros impares eh: ', soma)

    
