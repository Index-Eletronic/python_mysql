'''
Crie um menu com 3 opções.
1 para Abrir Arquiv
2 para Ler Arquivo
3 para sair do sistemna
'''

menu = 0

def openArquivo():
    nome = str(input('Digite o nome do arquivo:'))
    arquivo = open(nome)
    return arquivo

def lerArquivo(arquivo):

    linhas = arquivo.readlines()
    for linha in linhas():
        print(linha)

while menu != 3:
    print('''
            [1] - Abrir Arquivo
            [2] - Ler Arquivo
            [3] - Sai do Sistema.
          ''')
    menu = int(input('Digite a opção desejada: '))

    if menu == 1:
        arquivo = openArquivo()
    elif menu == 2:
        lerArquivo(arquivo)
    else:
        print('Saindo do Sistema')
        break
