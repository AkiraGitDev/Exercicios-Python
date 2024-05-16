"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

print("O aumento salarial é de 15% base. Mas para salários maiores que R$1250,00, o aumento é de apenas 10%.")
salario = float(input("Insira o salário atual para aumento: R$"))

aumento_base = (0.15 * salario) + salario
aumento_menor = (0.1 * salario) + salario

if salario <= 1250:
    print("Seu salário de R${} teve um aumento de 15%, indo para R${}.".format(salario, aumento_base))
else:
    print("Seu salário de R${} teve um aumento de 10%, indo para R${}.".format(salario, aumento_menor))
