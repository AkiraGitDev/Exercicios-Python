"""
Refaça o TABUADA V1, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

numero = int(input("Insira um número inteiro para verificar sua tabuada: "))

print("-" * 20)
for c in range(1,11):
    tabuada = numero * c
    print("{} x {} = {}".format(numero, c, tabuada))
print("-" * 20)