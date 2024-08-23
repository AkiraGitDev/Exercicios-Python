"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

import random
import time
lista = []

def sorteia(num):
    for i in range(0, num):
        sorteio = random.randint(1, 10)
        lista.append(sorteio)
        print(f'{sorteio} ', end="", flush=True)
        time.sleep(0.3)
sorteia(int(input("Insira quantos números deseja sortear: ")))

def somaPar():
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    time.sleep(0.5)
    print(f'A soma dos números pares da lista é: {soma}')
somaPar()