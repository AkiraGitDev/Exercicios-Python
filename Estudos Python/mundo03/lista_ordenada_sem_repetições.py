"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

valores = []

for c in range(0, 5):
    numero = int(input("Insira um valor para ser adicionado à lista: "))

    if c == 0:
        valores.append(numero)
        print("Adicionado o primeiro número.")
    elif numero > valores[-1]:
        valores.append(numero)
        print("Adicionado o na última posição.")
    else:
        posicao = 0
        
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                print(f"Adicionado na posição {posicao} da lista.")
                break
            posicao += 1

print("-=" * 30)
print(f"Os números inseridos na lista em ordem foram: {valores}.")
  