"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
import random
import time

print("=========== JOKENPÔ GAME ==========")

print("Vamos jogar PEDRA, PAPEL e TESOURA!")
print("""Escolha uma opção:
1) PEDRA
2) PAPEL
3) TESOURA""")

escolha = int(input("Insira a sua escolha: "))
pc = random.randint(1, 3)

print("===================================")
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PÔ!")
print("===================================")

if escolha == 1:
    print("Você escolheu PEDRA!")
elif escolha == 2:
    print("Você escolheu PAPEL!")
elif escolha == 3:
    print("Você escolheu TESOURA!")
else:
    print("Insira uma opção válida.")

if pc == 1:
    print("Computador escolheu PEDRA!")
elif pc == 2:
    print("Computador escolheu PAPEL!")
elif pc == 3:
    print("Computador escolheu TESOURA!")

if escolha == pc:
    print("EMPATE!")
elif escolha == 1 and pc == 2:
    print("COMPUTADOR VENCEU!")
elif escolha == 2 and pc == 3:
    print("COMPUTADOR VENCEU!")
elif escolha == 3 and pc == 1:
    print("COMPUTADOR VENCEU!")
elif escolha == 1 and pc == 3:
    print("VOCÊ VENCEU!")
elif escolha == 2 and pc == 1:
    print("VOCÊ VENCEU!")
elif escolha == 3 and pc == 2:
    print("VOCÊ VENCEU!")
