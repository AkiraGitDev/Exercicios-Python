"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""
r1 = float(input("Insira o primeiro segmento: "))
r2 = float(input("Insira o segundo segmento: "))
r3 = float(input("Insira o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Esses segmentos formam um triângulo!")
    if r1 == r2 == r3:
        print("Esse triângulo é EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("Esse triângulo é ESCALENO!")
    else:
        print("Esse triângulo é ISÓSCELES!")
else:
    print("Impossível formar um triângulo com esses segmentos.")
    