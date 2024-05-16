"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
n1 = int(input("Insira o número 1: "))
n2 = int(input("Insira o número 2: "))
n3 = int(input("Insira o número 3: "))

if n1 > n2 and n1 > n3:
    print("O maior valor é {}.".format(n1))
elif n2 > n1 and n2 > n3:
    print("O maior número é {}.".format(n2))
else:
    print("O maior número é {}.".format(n3))

if n1 < n2 and n1 < n3:
    print("O menor valor é {}.".format(n1))
elif n2 > n1 and n2 > n3:
    print("O menor número é {}.".format(n2))
else:
    print("O menor número é {}.".format(n3))