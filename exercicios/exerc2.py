'''
Faça um programa que receba duas notas digitadas pelo usuário e faça a média entre elas.
 Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado
'''

n1= float(input('Digite a Primeira nota:'.replace(',', '.')))
n2= float(input('Digite a Segunda nota:'.replace(',', '.')))
m = (n1+n2)/2

print(f'A média entre a notas {n1} e {n2} é {m} ')

if m >= 6:
    print('Você foi APROVADO.')
else:
    print('Você foi REPROVADO.')

