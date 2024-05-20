"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

print("Analisaremos se o número inserido é primo (divisível apenas por 1 e ele mesmo).")
numero = int(input("Insira um número: "))

total = 0

for c in range(1, numero + 1):
    print(c)
    if numero % c == 0:
        print("Divisível!")
        total += 1
    else: 
        print("Não divisível...")

if total == 2:
    print("{} é um número primo!".format(numero))
else:
    print("{} não é um número primo...".format(numero))
    