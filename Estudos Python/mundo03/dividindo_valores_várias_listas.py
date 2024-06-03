"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

valores = []
pares = []
impares = []

while True:
    numero = int(input("Insira um número à lista: "))
    valores.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    escolha = input("Deseja adicionar mais um número? (s/n): ").strip().lower()
    while escolha != "s" and escolha != "n":
        print("Opção inválida. Tente novamente.")
        escolha = input("Deseja adicionar mais um número? (s/n): ").strip().lower()

    if escolha == "n":
        break

print("-=" * 30)
print("As três listas geradas foram:")
print(f"Total: {valores}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")