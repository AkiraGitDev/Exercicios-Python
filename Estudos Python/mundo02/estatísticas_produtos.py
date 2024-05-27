"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

print("=" * 20, "LOJA SUPER BARATÃO", "=" * 20)

caixa = 0
contador_1000 = 0

produto = input("Insira o produto: ")
preco = float(input("Insira o preço: R$"))

barato = preco
nome_barato = produto
caixa += preco

if preco > 1000:
    contador_1000 += 1

while True:
    parar = input("Deseja adicionar mais produtos? (s/n): ").strip().lower()

    while parar != "s" and parar != "n":
        print("Valor inválido. Tente novamente.")
        parar = input("Deseja adicionar mais produtos? (s/n): ").strip().lower()

    if parar == "n":
        break
    else:
        produto = input("Insira o produto: ")
        preco = float(input("Insira o preço: R$"))

        caixa += preco

        if preco < barato:
            barato = preco
            nome_barato = produto

        if preco > 1000:
            contador_1000 += 1

print("=" * 20, "LOJA SUPER BARATÃO", "=" * 20)
print("Obrigado por comprar na loja SUPER BARATÃO!")
print("=" * 20, "LOJA SUPER BARATÃO", "=" * 20)
print("O valor total da compra foi R${:.2f}.".format(caixa))
print(f"Ao total, {contador_1000} produtos custam mais que R$1000.")
print("O produto mais barato é {} custando R${:.2f}.".format(nome_barato, barato))
