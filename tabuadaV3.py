"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

print(f"{"=" * 20} TABUADA V3 {"=" * 20}")

while True:
    numero = int(input("Será exibido a tabuada de qual número?: "))
    
    if numero < 0:
        break

    for c in range (1, 11):
        print(f"{numero} x {c} = {numero * c}")
    print("Insira um número negativo para sair do programa.")

print(f"{"=" * 20} TABUADA V3 {"=" * 20}")