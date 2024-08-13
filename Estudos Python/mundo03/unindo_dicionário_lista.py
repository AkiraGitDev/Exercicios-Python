"""Crie um programa que leia nome, gênero e idade de várias individuo, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média"""

individuo = {}
pessoas = []

while True:
    individuo.clear()
    individuo['nome'] = input("Insira o nome: ")
    individuo['idade'] = int(input("Qual a idade?: "))
    individuo['gênero'] =  input("Selecione gênero (M/F): ").strip().upper()[0]

    while individuo['gênero'] != "M" and individuo['gênero'] != "F":
        print("Opção inválida. Tente novamente...")
        individuo['gênero'] =  input("Selecione gênero (M/F): ").strip().upper()[0]
    
    pessoas.append(individuo.copy())

    opção = input("Deseja adicionar outra pessoa? (s/n): ").strip().lower()[0]
    while opção != "s" and opção != "n":
        print("Opção inválida. Tente novamente...")
        opção = input("Deseja adicionar outra pessoa? (s/n): ").strip().lower()[0]
    
    if opção == "n":
        break

print("-=" * 30)
for i in range 
print(pessoas)