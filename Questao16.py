# Crie um programa que leia uma lista de números do usuário e exiba a soma dos números pares.

soma_pares = []
soma = 0

for i in range(1,6):
    num = int(input('Digite os numeros: '))
    if num % 2 == 0:
        soma_pares.append(num)
        soma = soma + num

print('Os numeros pares digitados')
for num in soma_pares:
    print(num)
print('A Soma dos numeros pares eh: ', soma)

    
