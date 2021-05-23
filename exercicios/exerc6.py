'''
Escreva um programa que compare se duas sequências digitadas pelo usuário são iguais.
'''

lista = []
lista1 = []
lista2 = []

def sequenia(lista):
    for n in range(0, 4):
        usuario = int(input('Digite uma segencia de 4 numeros:'))
        lista.append(usuario)

#Principal

sequenia(lista1)
sequenia(lista2)

print(f'A primeira seguecia digitada{lista1}.')
print(f'A segunda seguecia digitada{lista2}.')

if lista1 == lista2:
    print('As seguencias são iguais')
else:
    print('As seguencias são diferentes')

