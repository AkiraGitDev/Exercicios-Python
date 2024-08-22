"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
import time

def maior(valores):
    maior_valor = valores[0]
    print("Analisando valores inseridos...")
    time.sleep(0.5)
    for valor in valores:
        print(valor, end=" ", flush=True)
        time.sleep(0.5)
        if valor > maior_valor:
            maior_valor = valor
    print(f'O maior valor da lista é {maior_valor}.')

maior_var = []

while True:
    numero = int(input("Insira um valor à lista (0 = termina): "))
    maior_var.append(numero)

    if numero == 0:
        break

maior(maior_var)