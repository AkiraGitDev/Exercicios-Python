"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

ficha = []

while True:
    nome = input("Insira o nome do aluno: ")
    n1 = float(input("Insira a 1ª nota: "))
    n2 = float(input("Insira a 2ª nota: "))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])

    escolha = input("Deseja adicionar mais um aluno? (s/n): ").strip().lower()
    while escolha != "s" and escolha != "n":
        print("Opção inválida. Tente novamente.")
        escolha = input("Deseja adicionar mais um aluno? (s/n): ").strip().lower()
    
    if escolha == "n":
        break

print("-=" * 10, "SISTEMA DE NOTAS", "-=" * 10)
for indice, a in enumerate(ficha):
    print(f"Aluno(a) {a[0]} com as notas {a[1]} ficou com média {a[2]}.")
print("-=" * 30)