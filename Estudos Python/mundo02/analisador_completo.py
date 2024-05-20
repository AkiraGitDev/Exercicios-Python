"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
soma = 0
contador = 0
maior_idade = 0
homem_velho = ""

for c in range(1, 5):
    print("===== {}ª PESSOA =====".format(c))
    nome = input("Insira o nome: ")
    idade = int(input("Insira a idade: "))
    genero = input("Qual o gênero? (M/F): ").strip().upper()
    soma += idade

    if genero == "M":
        if idade > maior_idade:
            maior_idade = idade
            homem_velho = nome
    elif genero == "F" and idade < 20:
            contador += 1

media = soma / 4
print("A idade média do grupo é: {:.1f} anos.".format(media))

if homem_velho:
    print("O homem mais velho é {} com {} anos.".format(homem_velho, maior_idade))
else:
     print("Não há homens no grupo.")
print("Foram inseridas {} mulhere(s) com idade menor que 20 anos.".format(contador))