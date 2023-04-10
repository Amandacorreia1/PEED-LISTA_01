#Crie um programa que leia uma lista de números do usuário e exiba somente os números ímpares

impares = []

for i in range(1,6):
   num = int(input('Informe os numeros: '))
   if num % 2 != 0:
    impares.append(num)

print('Os numeros pares digitados sao: ')
for num in impares:
    print(num)
      
