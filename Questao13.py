# crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a"

letra = []

for i in range(1,6):
    palavra = str(input('Digite a palavra: '))
    letra.append(palavra)
        
print('A palavra digitada iniciada com "a ou A" letra a foi: ')
for palavra in letra:
    if palavra[0] == 'a' or palavra[0] == 'A':
        print(palavra)