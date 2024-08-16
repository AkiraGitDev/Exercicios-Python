"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada"""

import time

print("CONTAGEM COM FUNÇÃO")
print("-=" * 30)

def contador(a, b, c):
    if c < 0:
        c *= -1
    
    if c == 0:
        c = 1
        
    print(f'Contagem de {a} até {b} de {c} em {c}.')
    time.sleep(1)

    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont += c
        time.sleep(0.5)
        print('FIM!')
        print("-=" * 30)
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont -= c
        time.sleep(0.5)
        print("FIM!")
        print("-=" * 30)

contador(1, 10, 1)
contador(10, 0, 2)
print("Agora escolha a sua contagem personalizada!")
time.sleep(0.5)
início = int(input("Insira o início da contagem: "))
final = int(input("Insira o final da contagem: "))
passo = int(input("Insira o passo da contagem: "))
contador(início, final, passo)