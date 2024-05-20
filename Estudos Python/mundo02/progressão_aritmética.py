"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" * 20)

primeiro = int(input("Insira o primeiro termo da PA: "))
razao = int(input("Insira a razão dessa PA: "))
decimo = primeiro + (10-1) * razao #Fórmula da PA para 10 termos.

for c in range(primeiro, decimo, razao):
    print(c)
print("FIM!")