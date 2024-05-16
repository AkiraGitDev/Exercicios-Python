"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

distancia = float(input("Insira a distância em Km da viagem: "))
preco_promo = distancia * 0.45
preco = distancia * 0.5

if distancia >= 200:
    print("A viagem é mais longa. Você conseguiu promoção e pagará R${:.2f}!".format(preco_promo))
else:
    print("Viagem mais curta. Você pagará RS{:.2f}.".format(preco))
