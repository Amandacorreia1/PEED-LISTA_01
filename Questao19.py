#Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem crescente

ordem_crescente = []

for i in range(1,6):
    num = int(input('Informe os numeros: '))
    ordem_crescente.append(num)

ordem_crescente.sort()
print('Os numeros em ordem crescente eh: ', ordem_crescente)