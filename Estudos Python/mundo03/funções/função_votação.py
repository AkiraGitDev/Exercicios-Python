"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
import datetime

def voto(ano):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano
    if 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: OPCIONAL.'
    elif idade < 16:
        return f'Com {idade} anos: NEGADO.'
    elif idade >= 18:
        return f'Com {idade} anos: OBRIGATÓRIO.'
    
nascimento = int(input("Em que ano você nasceu?: "))
print(voto(nascimento))