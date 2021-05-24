'''
Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.
'''


arq = 'exerc.txt'
arquivo = open(arq)
linhas = arquivo.readlines()
for i in linhas:
    print(i)





