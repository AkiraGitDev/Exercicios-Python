"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor válido.
"""

genero = input("Insira seu gênero (M/F): ").strip().upper()

while genero != "M" and genero != "F":
    print("Insira um gênero válido!")
    genero = input("Insira seu gênero (M/F): ").strip().upper()

if genero == "M":
    print("Você selecionou o gênero MASCULINO.")
elif genero == "F":
    print("Você selecionou o gênero FEMININO.")