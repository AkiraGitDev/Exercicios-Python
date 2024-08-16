"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

valores = []

while True:
    numero = int(input("Insira um número na lista: "))

    if numero in valores:
        print("Número já inserido na lista. Insira outro...")
    else:
        valores.append(numero)
        print("Número inserido com sucesso!")

    escolha = input("Deseja adicionar mais um número? (s/n): ").strip().lower()

    while escolha != "n" and escolha != "s":
        print("Valor inválido. Tente novamente.")
        escolha = input("Deseja adicionar mais um número? (s/n): ").strip().lower()

    if escolha == "n":
        break
    elif escolha == "s":
        print("Um novo número será adicionado!")

print("=" * 50)
print("Essa foi a lista inserida em formato crescente:")
valores.sort()
print(valores)
