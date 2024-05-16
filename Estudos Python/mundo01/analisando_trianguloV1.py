"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

reta1 = float("Insira o primeiro segmento: ")
reta2 = float("Insira o segundo segmento: ")
reta3 = float("Insira o terceiro segmento: ")

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos acima PODEM FORMAR TRIÂNGULO.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO.")