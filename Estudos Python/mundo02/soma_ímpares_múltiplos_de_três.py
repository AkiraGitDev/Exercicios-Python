"""
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
import time

print("Contando apenas números que são múltiplos de 3 e que se encontram no intervalo de 1 a 500: ")

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        time.sleep(0.05)
        contador += 1
        soma += c

print("Fim da contagem!")
print("A soma de todos os valores solicitados é: {}!".format(soma))
print("A quantidade de números somados é: {}!".format(contador))
