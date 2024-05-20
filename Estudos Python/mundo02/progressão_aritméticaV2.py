"""
Refaça o DESAFIO PROGRESSÃO ARITMÉTICA, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print("=" * 30)
print("10 TERMOS DE UMA PA (COM WHILE)")
print("=" * 30)

primeiro = int(input("Insira o primeiro termo da PA: "))
razao = int(input("Insira a razão da PA: "))
termo = primeiro
contador = 1

while contador <= 10:
    print(termo)
    termo += razao
    contador += 1
print("FIM!")
