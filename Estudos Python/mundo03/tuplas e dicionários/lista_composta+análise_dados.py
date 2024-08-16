"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

principal = []
temporario = []
quantidade = 0

while True:
    nome = input("Insira o nome da pessoa: ")
    peso = float(input("Insira o peso da pessoa: "))
    temporario.append(nome)
    temporario.append(peso)
    quantidade += 1

    if quantidade == 1:
        maior_peso = temporario[1]
        menor_peso = temporario[1]
    else:
        if maior_peso < temporario[1]:
            maior_peso = temporario[1]
        elif menor_peso > temporario[1]:
            menor_peso = temporario[1]

    principal.append(temporario[:])
    temporario.clear()

    escolha = input("Deseja continuar? (s/n): ").strip().lower()

    while escolha != "s" and escolha != "n":
        print("Opção inválida. Tente novamente.")
        escolha = input("Deseja continuar? (s/n): ").strip().lower()

    if escolha == "n":
        break

print("-=" * 30)
print(f"Os dados inseridos foram: {principal}")
print(f"Foram cadastradas {quantidade} pessoas ao total.")

print(f"O maior peso foi de {maior_peso}Kg. Peso de ", end="")
for pessoas in principal:
    if pessoas[1] == maior_peso:
        print(f"[{pessoas[0]}] ", end="")
print()

print(f"O menor peso foi de {menor_peso}Kg. Peso de ", end="")
for pessoas in principal:
    if pessoas[1] == menor_peso:
        print(f"[{pessoas[0]}] ", end="")
print()
