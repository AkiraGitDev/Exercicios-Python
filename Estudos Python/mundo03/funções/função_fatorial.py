"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""

def fatorial(num):
    cálculo = 0
    contador = num
    while num > 0:
        contador -= 1
        cálculo *= num * (num - contador)
    print(cálculo)




fatorial(5)