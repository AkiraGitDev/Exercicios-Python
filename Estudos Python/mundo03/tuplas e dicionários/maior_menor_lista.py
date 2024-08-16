"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

valores = []

maior = 0
menor = 0
posicao_maior = 0
posicao_menor = 0

for c in range(0, 5):
    numero = int(input("Insira um número na posição {}: ".format(c)))
    valores.append(numero)

    if c == 0:
        maior = numero
        menor = numero
        posicao_maior = c
        posicao_menor = c
    else:
        if maior < numero:
            maior = numero          
        elif menor > numero:
            menor = numero          

print("=" * 30)
print("A lista de números inseridos é: {}.".format(valores))

print("O maior número inserido foi: {}.".format(maior), end=" ")
print("Foram inseridos nas posições: ", end="")
for indice, valor in enumerate(valores):
    if valores[indice] == maior:
        print(f"{indice}...", end="")
print()

print("O menor número inserido foi: {}.".format(menor), end=" ")
print("Foram inseridos nas posições: ", end="")
for indice, valor in enumerate(valores):
    if valores[indice] == menor:
        print(f"{indice}...", end="")
print()
