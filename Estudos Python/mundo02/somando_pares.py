"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

print("Iremos somar todos os números pares. Se o valor inserido for ímpar, sera desconsiderado.")

soma = 0
contador = 0
for c in range(1, 7):
    numero = int(input("Insira o {}º número: ".format(c)))
    if numero % 2 == 0:
        soma += numero
        contador += 1

print("{} número(s) inseridos. A soma dos números pares é: {}.".format(contador, soma))
