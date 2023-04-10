#Crie um programa que leia uma lista de números do usuário e exiba a média desses números
soma = 0

for i in range(1,6): 
    num = int(input('Informe os números: '))
    soma = soma + num
media = soma / 5

print('A media dos numeros digitados foi: ', media)
