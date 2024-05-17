"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
"""

print("========== MERCADO AKIRÃO ==========")

preco = float(input("Insira o valor do produto: R$"))
print("1) à vista pix: 10% de desconto.")
print("2) à vista cartão: 5% de desconto.")
print("3) até 2x no cartão: preço formal.")
print("4) 3x ou mais no cartão: 20% de juros.")

escolha = int(input("Qual será o método de pagamento? Escolha uma opção: "))

if escolha == 1:
    valor = preco - (preco * 0.1)
    print("Pagando à vista no pix o valor de R${:.2f} ficará R${:.2f}.".format(preco, valor))
elif escolha == 2:
    valor = preco - (preco * 0.05)
    print("Pagando à vista no cartão o valor de R${:.2f} ficará R${:.2f}.".format(preco, valor))
elif escolha == 3:
    parcelamento = preco / 2
    print("Pagamento parcelado não possui desconto. As parcelas serão de R${:.2f} por mês.".format(parcelamento))
elif escolha == 4:
    meses = int(input("Insira em quantas vezes será o parcelamento: "))
    juros = (preco + (preco * 0.2))
    parcelamento = juros / meses
    print("Pagamento terá juros de 20%. As parcelas serão de R${:.2f} durante {} meses, com um valor total de R${:.2f}.".format(parcelamento, meses, juros))
else:
    print("Opção inválida. Escolha uma opção válida.")