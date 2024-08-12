"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""

aluno = {}
aluno['nome'] = input("Nome: ")
aluno['média'] = float(input("Média de {}: ".format(aluno["nome"])))

if aluno["média"] >= 7:
    aluno['situação'] = "Aprovado"
elif aluno["média"] < 7 and aluno["média"] >= 5:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado..."

print("-=" * 10)
for k, v in aluno.items():
    print("{} é igual a {}.".format(k, v))