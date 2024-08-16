"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
import random

lista = []
jogos = []
contador = 0
total = 1

print("-=" * 5, "MEGA SENA DO AKIRÃO", "-=" * 5)
quantidade = int(input("Quantos jogos serão gerados?: "))
print("-=" * 30)

while total <= quantidade:
    contador = 0
    while True:
        numero = random.randint(1, 60)
        
        if numero not in lista:
            lista.append(numero)
            contador += 1
        
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f"{i+1}º jogo: {l}")
