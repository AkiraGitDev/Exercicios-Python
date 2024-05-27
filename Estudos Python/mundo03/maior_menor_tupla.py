"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

import random

numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

print("Números gerados:", numeros)

menor = min(numeros)
maior = max(numeros)

print(f"O maior valor sorteado foi {maior}.")
print(f"O menor valor sorteado foi {menor}.")
