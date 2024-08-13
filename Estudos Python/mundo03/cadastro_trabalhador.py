"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

import datetime

dados = {}
dados['nome'] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
dados['ctps'] = int(input("Carteira (0 = não possui): "))
dados['idade'] = datetime.datetime.now().year - nascimento

if dados['ctps'] != 0:
    dados['contrato'] = int(input("Ano de contratação: "))
    dados['salário'] = float(input("Salário: R$"))
    dados['aposentadoria'] = (dados['contrato'] + 35) - datetime.datetime.now().year

print("-=" * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}.')