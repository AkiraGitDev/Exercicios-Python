"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
A) Quantos números foram.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []

while True:
    numero = int(input("Insira um número: "))
    valores.append(numero)
    escolha = input("Deseja continuar? (s/n): ").strip().lower()

    while escolha != "s" and escolha != "n":
        print("Opção inválida. Tente novamente.")
        escolha = input("Deseja continuar? (s/n): ").strip().lower()
    
    if escolha == "n":
        break

print("-=" * 30)
print(f"Foram inseridos {len(valores)} números ao total.")

valores.sort(reverse=True)

print(f"Aqui está a lista ordenada: {valores}.")

if 5 in valores:
    print("O número 5 está presente na lista.")
else:
    print("O número 5 não está na lista.")