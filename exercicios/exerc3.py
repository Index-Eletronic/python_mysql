'''
Escreva um programa que resolva uma equação de segundo grau.
'''
import math
#ax^2+bx+c=0
#a =5 / b = 3 / c = 2
# x = b^2-4*a*c

a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))

print(f'Sua equação é:{a}x²+{b}x+{c} = 0 ')
x = b**2 - 4*a*c
print(f'O delta para essa equação é: {x}')
raiz = math.sqrt(x)
d1 = (-b+raiz)/2*a
d2 = (-b-raiz)/2*a

print(f'Encontrado os 2 valores para x = {d1:.0f} e {d2:.0f}')