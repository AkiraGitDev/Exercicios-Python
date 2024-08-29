"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

# Função do Programa
def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} marcou {gols} gol(s) no campeonato.')



# Programa Principal
print("-=" * 15)
nome = str(input("Insira o nome do jogador: "))
gol = str(input("Quantos gols ele fez?: "))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)