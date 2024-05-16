"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
import time

numero = int(input("Insira um número inteiro para análise: "))
print("Processando...")
time.sleep(2)

if numero % 2 == 0:
    print("O número {} é PAR.".format(numero))
else:
    print("O número {} é ÍMPAR.".format(numero))
