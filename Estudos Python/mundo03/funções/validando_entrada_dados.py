"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)"""

def leiaInt(numero):
    ok = False
    valor = 0
    while True:
        n = str(input(numero))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Insira um número inteiro válido!")
        
        if ok:
            break
    return valor

    

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
        