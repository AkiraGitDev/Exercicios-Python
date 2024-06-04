"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

valores = [[], []]

for numeros in range(1, 8):
    numero = int(input(f"Insira o {numeros}º valor: "))

    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)

valores[0].sort()
valores[1].sort()

print("-=" * 30)
print(f"Os números pares inseridos foram: {valores[0]}")
print(f"Os números ímpares inseridos foram: {valores[1]}")
