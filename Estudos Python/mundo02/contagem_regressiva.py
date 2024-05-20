"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 1, com uma pausa de 1 segundo entre eles.
"""
import time

print("Começando contagem regressiva!")
time.sleep(1)
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print("BOOM! BOOM! POW!")