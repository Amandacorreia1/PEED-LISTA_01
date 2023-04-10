#Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente

ordem_decrescente = []

for i in range(1,6):
    num = int(input('Informe os numeros: '))
    ordem_decrescente.append(num)

ordem_decrescente.sort(reverse=True)
print('Os numeros em ordem decrescente eh: ', ordem_decrescente)