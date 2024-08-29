"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""

def fatorial(num, show):
    cálculo = 1
    while num > 0:
        cálculo *= num
        num -= 1
    print(cálculo)

    if show == "s":
        contador = 0
        



fatorial(5)