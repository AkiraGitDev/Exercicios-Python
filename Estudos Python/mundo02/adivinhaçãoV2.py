"""
Melhore o jogo AdivinhaçãoV1 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
import random
numero = random.randint(1, 10)
tentativas = 1

print("==================== JOGO DA ADIVINHAÇÃO V2 ====================")
print("Tente adivinhar o número de 1 a 10.")
adivinhar = int(input("Tente adivinhar o número: "))

if numero == adivinhar:
    print("VITÓRIA! Você adivinhou em {} tentativa(s)!".format(tentativas))

while numero != adivinhar:
    print("Você errou, tente novamente...")
    if numero > adivinhar:
        print("Está mais para cima!")
        adivinhar = int(input("Tente adivinhar o número: "))
        tentativas += 1
    else:
        print("Está mais para baixo!")
        adivinhar = int(input("Tente adivinhar o número: "))
        tentativas += 1

if numero == adivinhar:
    print("VITÓRIA! Você adivinhou em {} tentativa(s)!".format(tentativas))

print("==================== JOGO DA ADIVINHAÇÃO V2 ====================")