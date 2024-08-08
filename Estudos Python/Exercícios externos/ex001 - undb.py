"""Escreva um programa que leia números positivos e os armazene numa lista (até que um número não positivo seja fornecido). Por fim, seu programa receberá um número inteiro x e deve verificar se x pertence ou não à lista."""

positivos = []

while True:
    numero = int(input("Insira um número: "))

    if numero < 0:
        break

    positivos.append(numero)

    escolha = input("Deseja adicionar um número a mais? (s/n): ").strip().lower()


    while escolha != "s" and escolha != "n":
        print("Opção inválida. Tente novamente...")
        escolha = input("Deseja adicionar um número a mais? (s/n): ").strip().lower()
    
    if escolha == "n":
        break

print("A lista de números é essa: {}.".format(positivos))

verificar = int(input("Qual número deseja verificar na lista?: "))

if verificar in positivos:
    print("O número {} está na lista!".format(verificar))
else:
    print("O número {} NÃO está na lista...".format(verificar))