"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""

print("CONTROLE DE TERRENOS")
print("-=" * 12)

def cálculo_área(a, b):
    área = a * b
    print(f'A área de largura {a} e comprimento {b} é de {área}m².')

# Programa Principal
largura = float(input("Insira a largura do terreno (em metros): "))
comprimento = float(input("Insira o comprimento do terreno (em metros): "))
cálculo_área(largura, comprimento)