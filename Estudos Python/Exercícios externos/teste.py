cesta = []

while True:
    fruta = input("Insira uma fruta: ")
    cesta.append(fruta)

    escolha = input("Deseja inserir mais alguma fruta? (s/n): ").strip().lower()

    while escolha != "n" and escolha != "s":
        print("Opção inválida! Tente novamente...")
        escolha = input("Deseja inserir mais alguma fruta? (s/n): ").strip().lower()

    if escolha == "n":
        break

print("A sua cesta contém as seguintes frutas: {}".format(cesta))
    