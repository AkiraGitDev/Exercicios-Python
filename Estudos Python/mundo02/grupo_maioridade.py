"""
Crie um programa que leia o ano de nascimento de SETE pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
import datetime

print("Iremos analisar as idades inseridas: ")
ano_atual = datetime.datetime.today().year
contador_maior = 0
contador_menor = 0

for c in range(1, 8):
    ano = int(input("Insira o {}º ano de nascimento: ".format(c)))
    idade = ano_atual - ano
    if idade >= 18:
        print("Essa pessoa é maior de idade ({} anos).".format(idade))
        contador_maior += 1
    else:
        print("Essa pessoa é menor de idade ({} anos).".format(idade))
        contador_menor += 1

print("Ao total foram {} pessoas MAIORES.".format(contador_maior))
print("Ao total foram {} pessoas MENORES.".format(contador_menor))
