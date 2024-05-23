"""
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""

numero = 0
soma = 0
contador = 0

while True:
    numero = int(input("Insira um número inteiro: "))

    if numero == 999:
        break
    
    soma += numero
    contador += 1

    
print(f"Foram inseridos ao total {contador} números.")
print(f"A soma total de todos os valores é {soma}.")