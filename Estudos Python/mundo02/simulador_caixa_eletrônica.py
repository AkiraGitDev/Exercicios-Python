"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print("=" * 20, "CAIXA BANCO AKIRA", "=" *20)
saque = int(input("Insira um valor para saque (inteiro): R$"))
total = saque

cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0

while True:
    if saque >= 50:
        saque -= 50
        cedula_50 += 1
    elif saque >= 20 and saque < 50:
        saque -= 20
        cedula_20 += 1
    elif saque >= 10 and saque < 20:
        saque -= 10
        cedula_10 += 1
    elif saque >= 1 and saque < 10:
        saque -= 1
        cedula_1 += 1
    else:
        break

print("=" * 20, "CAIXA BANCO AKIRA", "=" *20)
print("Você sacou um total de R${}.".format(total))

if cedula_50 != 0:
    print(f"Total de {cedula_50} cédulas de R$50.")
if cedula_20 != 0:
    print(f"Total de {cedula_20} cédulas de R$20.")
if cedula_10 != 0:
    print(f"Total de {cedula_10} cédulas de R$10.")
if cedula_1 != 0:
    print(f"Total de {cedula_1} cédulas de R$1.")
    
print("=" * 20, "CAIXA BANCO AKIRA", "=" *20)
print("Obrigado por usar o BANCO AKIRA, volte sempre!")
