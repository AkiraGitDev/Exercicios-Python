"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

soma = 0
contador = 0

print("=" * 50)
numero = float(input("Insira um número inteiro: "))
soma += numero
contador += 1

maior_valor = numero
menor_valor = numero

opcao = input("Quer continuar adicionando valores? (s/n): ").strip().lower()
while opcao != "s" and opcao != "n":
        print("Opção inválida! Tente novamente.")
        opcao = input("Quer continuar adicionando valores? (s/n): ").strip().lower()

while opcao == "s":
    numero = int(input("Insira um número inteiro: "))
    soma += numero
    contador += 1

    if maior_valor < numero:
        maior_valor = numero

    if menor_valor > numero:
        menor_valor = numero

    opcao = input("Quer continuar adicionando valores? (s/n): ").strip().lower()
    while opcao != "s" and opcao != "n":
        print("Opção inválida! Tente novamente.")
        opcao = input("Quer continuar adicionando valores? (s/n): ").strip().lower()

media = soma / contador

print("=" * 50)
print("A soma total foi: {:.1f}.".format(soma))
print("A média de todos os termos inseridos é: {:.1f}.".format(media))
print("O menor valor inserido foi: {:.1f}.".format(menor_valor))
print("O maior valor inserido foi: {:.1f}.".format(maior_valor))
print("=" * 50)