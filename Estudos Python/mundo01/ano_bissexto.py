"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
import datetime

ano = int(input("Insira um ano para análise: "))
if ano == 0:
    ano = datetime.datetime.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO!".format(ano))
else:
    print("O ano {} não é BISSEXTO...".format(ano))