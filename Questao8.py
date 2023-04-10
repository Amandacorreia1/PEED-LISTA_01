#Crie um programa que leia uma lista de números de usuáros e exiba o maior número dessa lista
maiorNumero = ''

for i in range(1,5):
    numero = str(input('Informe um numero: '))
    if len(numero) < len(maiorNumero):
        numero = maiorNumero
print('O maior numero digitado foi: ', numero)