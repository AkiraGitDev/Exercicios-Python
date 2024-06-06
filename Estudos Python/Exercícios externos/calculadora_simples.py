"""
Desenvolva uma calculadora que possa realizar as operações básicas (adição, subtração, multiplicação, divisão). O usuário deve ser capaz de escolher a operação e fornecer os números de entrada.
"""
print("-=" * 10, "CALCULADORA SIMPLES", "-=" * 10)
print("OPÇÕES: 1) Soma, 2)Diferença, 3)Multiplicação e 4)Divisão.")
operacao = input("Insira a opção de operação: ")
n1 = float(input("Insira o 1º valor: "))
n2 = float(input("Insira o 2º valor: "))

if operacao == 1:
    soma = n1 + n2
    print(f"A soma dos valores {n1} e {n2} é {soma}.")
elif operacao == 2:
    diferenca = n1 - n2
    print(f"A diferença dos valores {n1} e {n2} é {diferenca}.")
elif operacao == 3:
    multiplicacao = n1 * n2
    print(f"Os valores {n1} e {n2} multiplicados resulta {multiplicacao}.")
elif operacao == 4:
    divisao = n1 / n2
    print(f"Os valores {n1} e {n2} dividos resultam {divisao}.")
else:
    while True:
        print("Opção inválida. Tente novamente.")
        operacao = input("Insira a opção de operação: ")
