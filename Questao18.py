#Crie um programa que leia uma lista de números do usuário e exiba o produto desses números

numero_produto = []
produto = 1

for i in range(1,6):
    num = int(input('Digite os numeros: '))
    numero_produto.append(num)
    produto = produto * num
print('O produto dos numeros digitados foi: ', produto)
  
