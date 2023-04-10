#Crie um programa que leia uma lista de números do usuário e exiba o menor número dessa lista
numeroMenor = ''

for i in range(1,5):
    numero = input('Informe os numeros: ')
    if len(numeroMenor) < len(numero):
        numeroMenor = numero 
print('O menor numero digitado foi: ', numeroMenor)
