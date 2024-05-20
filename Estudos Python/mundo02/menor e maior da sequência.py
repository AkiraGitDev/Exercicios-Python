"""
Faça um programa que leia o peso de CINCO pessoas. No final, mostre qual foi o MAIOR e o MENOR peso lidos.
"""

maior_peso = 0
menor_peso = 0

for c in range(1, 6):
    peso = float(input("Insira o peso da {}ª pessoa em Kg: ".format(c)))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print("O MAIOR peso inserido foi {}Kg.".format(maior_peso))
print("O MENOR peso inserido foi {}Kg.".format(menor_peso))