"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
import time

n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))

while True: 
    print("-=-" * 20)
    print("Qual é a sua opção?")
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Qual é maior?")
    print("[ 4 ] Novos valores")
    print("[ 5 ] Sair do programa")
    print("-=-" * 20)

    opcao = int(input(">>>>>Insira uma opção: "))
    if opcao == 1:
        time.sleep(0.5)
        soma = n1 + n2
        print("A soma dos valores {} e {} é igual a: {}.".format(n1, n2, soma))
    elif opcao == 2:
        time.sleep(0.5)
        produto = n1 * n2
        print("A multiplicação dos valores {} e {} é igual a: {}.".format(n1, n2, produto))
    elif opcao == 3:
        time.sleep(0.5)
        if n1 > n2:
            print("O maior valor é {}.".format(n1))
        elif n1 < n2: 
            print("O maior valor é {}.".format(n2))
        else:
            print("Os valores são iguais.")
    elif opcao == 4:
        time.sleep(0.5)
        print("Insira novos valores: ")
        n1 = int(input("Insira o primeiro valor: "))
        n2 = int(input("Insira o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Fim do programa.")
