"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

numeros = (int(input("Insira o primeiro valor: ")), int(input("Insira o segundo valor: ")), int(input("Insira o terceiro valor: ")), int(input("Insira o quarto valor: ")))

print("Você inseriu os valores: {}.".format(numeros))
print("O valor 9 apareceu {} vezes.".format(numeros.count(9)))

if 3 in numeros:
    print("O valor 3 apareceu na {}ª posição.".format(numeros.index(3)+1))
else:
    print("O valor 3 não foi encontrado na tupla.")

for c in numeros:
    if c % 2 == 0:
        print("Os valores pares encontrados foram {}.".format(c), end=" ")