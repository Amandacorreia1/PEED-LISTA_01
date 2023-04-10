#Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa
palavraLonga = ''

for i in range(1,5):
    palavra = str(input('Informe uma palavra: '))
    if len(palavra) > len(palavraLonga):
        palavraLonga = palavra
print('A maior palavra digitada foi: ', palavraLonga)
