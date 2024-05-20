"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""

print("Vamos ler o número e calcular seu fatorial.")
numero = int(input("Insira um número inteiro: "))
contador = numero
fatorial = 1

while contador > 0:
    fatorial *= contador
    contador -= 1
    
print("O fatorial de {} é {}.".format(numero, fatorial))
