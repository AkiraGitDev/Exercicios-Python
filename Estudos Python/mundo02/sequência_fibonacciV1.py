"""
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
"""
print("=" * 30)
print("Sequência de Fibonacci")
print("=" * 30)
numero = int(input("Insira o número de termos da sequência para exibição: "))

print("~" * 30)

t1 = 0
t2 = 1

print("{}".format(t1))
print("{}".format(t2))
contador = 3

while contador <= numero:
    t3 = t1 + t2
    print("{}".format(t3))
    t1 = t2
    t2 = t3
    contador += 1

print("Fim da sequência.")
print("~" * 30)
