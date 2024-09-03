"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)"""

def notas(*num, sit=False):
    dicionario = dict()
    dicionario['total de notas'] = len(num)

    maior = 0
    for n in num:
        if n > maior:
            maior = n
    dicionario['maior nota'] = maior 

    menor = maior
    for n in num:
        if menor > n:
            menor = n
    dicionario['menor nota'] = menor

    soma = 0
    contador = 0
    for n in num:
        soma += n
        contador += 1
    media = soma / contador
    dicionario['média'] = media

    return dicionario



resposta = notas(5.5, 8, 9.5, 4, 7, 10, 2, 3)
print(resposta)