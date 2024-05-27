"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numero = int(input("Insira um número de 0 a 20: "))

while numero < 0 or numero > 20:
    print("Valor inválido. Tente novamente.")
    numero = int(input("Insira um número de 0 a 20: "))

extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

print(extenso[numero])

while True:
    continuar = input("Deseja que seja mostrado outro número? (s/n): ").strip().lower()

    if continuar == "s":
        numero = int(input("Insira um número de 0 a 20: "))
        while numero < 0 or numero > 20:
            print("Valor inválido. Tente novamente.")
            numero = int(input("Insira um número de 0 a 20: "))
        
        print(extenso[numero])
    elif continuar == "n":
        break
    elif continuar != "s" and continuar != "n":
            print("Valor inválido. Tente novamente")
            