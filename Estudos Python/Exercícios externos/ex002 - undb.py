"""Escreva um programa que recebe como entrada um número inteiro positivo n. Em seguida, seu programa deve ler n números inteiros e adicioná-los numa lista. Por fim, seu programa receberá um número inteiro x e deve verificar se x pertence ou não à lista."""

lista = []

while True:
    numero = int(input("Adicione um número à lista: "))
    lista.append(numero)

    escolha = input("Deseja adicionar outro número? (s/n): ").strip().lower()

    while escolha != "s" and escolha != "n":
        print("Escolha inválida. Tente novamente...")
        escolha = input("Deseja adicionar outro número? (s/n): ").strip().lower()
    
    if escolha == "n":
        break

verificar = int(input("Insira o número que deseja verificar na lista: "))

if verificar in lista:
    print("O número {} está na lista!".format(verificar))
else:
    print("O número {} não está na lista...".format(verificar))

print("A lista completa é: {}".format(lista))