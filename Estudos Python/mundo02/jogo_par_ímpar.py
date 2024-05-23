"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
import random

vitorias = 0

while True:
    print(f"{"=" * 20} PAR OU ÍMPAR {"=" * 20}")

    computador = random.randint(0, 10)
    jogador = int(input("Insira seu número (de 0 a 10): "))

    escolha = input("PAR ou ÍMPAR? (P/I): ").upper()

    while escolha != "P" and escolha != "I":
        print("Escolha inválida. Tente novamente.")
        escolha = input("PAR ou ÍMPAR? (P/I): ").upper()

    print(f"O computador jogou {computador}!")

    if (jogador + computador) % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"

    print(f"O resultado foi {jogador + computador}.")

    if escolha == resultado:
        print("VITÓRIA!")
        vitorias += 1
    else:
        print("Você perdeu...")
        break

print(f"{"=" * 20} PAR OU ÍMPAR {"=" * 20}")
print(f"Você ganhou {vitorias}x seguida(s)!")
print("Fim de jogo...")
