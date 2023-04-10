#Crie um programa que leia uma lista de números do usuário e exiba a soma desses números
soma = 0
for i in range(1,10):
    numero = int(input('Digite os numeros: '))
    soma = soma + numero

print('A soma dos numeros digitados eh: ', soma)
