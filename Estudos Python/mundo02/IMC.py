"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""

print("--------------------------------------------------------")
print("Vamos calcular o seu IMC (Índice de Massa Corporal).")
print("Tabela de IMC:")
print("– IMC abaixo de 18,5: Abaixo do Peso")
print("– Entre 18,5 e 25: Peso Ideal")
print("– 25 até 30: Sobrepeso")
print("– 30 até 40: Obesidade")
print("– Acima de 40: Obesidade Mórbida")
print("--------------------------------------------------------")

peso = float(input("Insira o seu peso corporal em Kg: "))
altura = float(input("Insira a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
    print("Seu IMC é: {:.2f}.".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Você está no peso ideal.")
    print("Seu IMC é: {:.2f}.".format(imc))
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
    print("Seu IMC é: {:.2f}.".format(imc))
elif imc >= 30 and imc < 40:
    print("Seu IMC é: {:.2f}.".format(imc))
    print("Você está obeso.")
else:
    print("Você está com obesidade mórbida.")
    print("Seu IMC é: {:.2f}.".format(imc))
