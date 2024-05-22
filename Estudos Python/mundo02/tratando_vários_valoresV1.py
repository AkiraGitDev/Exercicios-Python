"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

print("Vamos somar todos os números inseridos.")
print("=" * 40)

numero = int(input("Insira um número (999 para parar): "))
soma = 0
contador = 0

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input("Insira um número (999 para parar): "))

print("Foram inseridos um total de {} números.".format(contador))
print("A soma de todos os números foi: {}!".format(soma))
