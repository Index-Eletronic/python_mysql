'''
Escreva um programa que ordene uma lista numérica com três elementos.
'''

num = list()
for n in range(0, 3):
   num.append(int(input('Digite um numero: ')))
   num.sort()

print(num)