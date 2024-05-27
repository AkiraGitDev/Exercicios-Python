"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol (27/05/2024), na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o Flamengo.
"""

tabela = ("Atlético-PR", "Bahia", "Flamengo", "Botafogo", "São Paulo", "Cruzeiro", "Atlético-MG", "Bragantino", "Palmeiras", "Internacional", "Fortaleza", "Grêmio", "Vasco da Gama", "Criciúma", "Juventude", "Corinthians", "Fluminense", "Vitória", "Atlético-GO", "Cuiabá")

print("-=" * 20)
print(tabela[0:5])
print("-=" * 20)
print(tabela[16:])
print("-=" * 20)
print(sorted(tabela))
print("-=" * 20)
print(f"O Flamengo está na {tabela.index("Flamengo")+1}ª posição.")
print("-=" * 20)