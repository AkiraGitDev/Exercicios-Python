"""Crie um programa que leia nome, gênero e idade de vários individuos, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média"""

individuo = {}
pessoas = []
mulheres = []

while True:
    individuo.clear()
    individuo['nome'] = input("Insira o nome: ")
    individuo['idade'] = int(input("Qual a idade?: "))
    individuo['gênero'] =  input("Selecione gênero (M/F): ").strip().upper()[0]

    while individuo['gênero'] != "M" and individuo['gênero'] != "F":
        print("Opção inválida. Tente novamente...")
        individuo['gênero'] =  input("Selecione gênero (M/F): ").strip().upper()[0]

    if individuo["gênero"] == "F":
        mulheres.append(individuo.copy())
    
    pessoas.append(individuo.copy())

    opção = input("Deseja adicionar outra pessoa? (s/n): ").strip().lower()[0]
    while opção != "s" and opção != "n":
        print("Opção inválida. Tente novamente...")
        opção = input("Deseja adicionar outra pessoa? (s/n): ").strip().lower()[0]
    
    if opção == "n":
        break
print("-=" * 30)

# Loop para contar número de pessoas na lista.
contador = 0
for i in range(len(pessoas)):
    contador += 1
print("Foram cadastradas {} pessoas.".format(contador))

# Loop para somar idades e calcular média.
soma_total = 0
for individuo in pessoas:
    soma_total += individuo['idade']
media = soma_total / contador
print("A média de todas as idades é: {} anos.".format(media))

# Loop para contar todas as mulheres.
contador_mulheres = 0
for individuo in mulheres:
    contador_mulheres += 1
print("Foram cadastradas {} mulheres.".format(contador_mulheres))

# Loop para contar as idades acima da média.
acima_média = []
for individuo in pessoas:
    if individuo['idade'] > media:  # Geralmente ">" é usado para evitar incluir a média
        acima_média.append(individuo.copy())  # Adiciona a pessoa individualmente
print("Pessoas com idade acima da média:")
for pessoa in acima_média:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
print("<<ENCERRADO>>")