"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

import time
print("=" * 20 + " ANALISADOR COMPLETO " + "=" * 20)

contador_idade = 0
contador_homens = 0
contador_mulheres = 0

while True:
    nome = input("NOME: ")
    idade = int(input("IDADE: "))
    genero = input("GÊNERO (M/F): ").strip().upper()

    if idade > 18:
        contador_idade += 1

    while genero != "M" and genero != "F":
        print("Gênero inválido. Tente novamente.")
        genero = input("GÊNERO (M/F): ").strip().upper()

    if genero == "M":
        contador_homens += 1
    elif genero == "F" and idade < 20:
        contador_mulheres += 1

    escolha = input("Deseja adicionar mais pessoas? (s/n): ").strip().lower()

    while escolha != "s" and escolha != "n":
        print("Escolha inválida. Tente novamente.")
        escolha = input("Deseja adicionar mais pessoas? (s/n): ").strip().lower()

    if escolha == "n":
        break

print("Análise finalizada!")
print("Carregando...")
time.sleep(3)

print("=" * 20 + " ANALISADOR COMPLETO " + "=" * 20)

print(f"Foram inseridas ao total {contador_idade} pessoas maiores de 18 anos.")
print(f"Ao total foram {contador_homens} homens cadastrados.")
print(f"Ao total foram {contador_mulheres} mulheres mais novas que 20 anos.")

print("=" * 20 + " ANALISADOR COMPLETO " + "=" * 20)
