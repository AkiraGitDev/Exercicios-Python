"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

import random
import time
import operator

print("-=" * 5, "JOGANDO DADOS!", "-=" * 5)
print("Valores sorteados:")
resultado = {}
resultado['jogador1'] = random.randint(1, 6)
resultado['jogador2'] = random.randint(1, 6)
resultado['jogador3'] = random.randint(1, 6)
resultado['jogador4'] = random.randint(1, 6)

for k, v in resultado.items():
    print("{} sorteou o número {}".format(k, v))
    time.sleep(1)

print("-=" * 5, "RANKING DE JOGADORES", "-=" * 5)
ranking = list()
ranking = sorted(resultado.items(), key=operator.itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(1)