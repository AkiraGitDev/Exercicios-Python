"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
import time

def fatorial(num, show=False):
    cálculo = 1
    original_num = num

    while num > 0:
        cálculo *= num
        num -= 1
    print(f'Fatorial: {cálculo}')

    if show == "s":
        contador = original_num
        while contador > 1:
            time.sleep(0.3)
            print(f'{contador} x ', end='', flush=True)
            contador -= 1
        print('1 =', cálculo)
    else:
        print("Sem mostrar cálculo.")

numero = int(input("Insira o número para cálculo de fatorial: "))
mostrar = input("Deseja que o cálculo seja impresso? (s/n): ").strip().lower()
fatorial(numero, mostrar)