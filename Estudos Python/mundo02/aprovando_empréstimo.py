"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input("Insira o valor do imóvel para compra: R$"))
salario = float(input("Insira o salário do comprador: R$"))
tempo = int(input("Insira em quanto tempo (em anos) será financiado: "))

prestacao = casa / (tempo * 12)

if prestacao > (salario * 0.3):
    print("A prestação da casa é igual a R${:.2f}, e seu salário é R${:.2f}. Empréstimo NEGADO...".format(prestacao, salario))
else:
    print("A prestação da casa é igual a R${:.2f}, e seu salário é R${:.2f}. Empréstimo CONCEDIDO!".format(prestacao, salario))
    print("O imóvel custo R${:.2f} e você pagará prestações de R${:.2f} durante {} anos.".format(casa, prestacao, tempo))

