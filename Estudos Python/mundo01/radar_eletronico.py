"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mansagem que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade_limite = 80
print("A velocidade máxima permitida é 80Km/h.")
velocidade = int(input("Insira a velocidade registrada pelo veículo: "))

if velocidade > velocidade_limite:
    print("Acima do limite de velocidade! MULTADO!")
    diferenca_velocidade = velocidade - velocidade_limite
    multa = diferenca_velocidade * 7
    print("A sua multa foi de R${} por ultrapassar {}Km/h do limite!".format(multa, diferenca_velocidade))
else:
    print("Dentro da velocidade permitida. Diriga com responsabilidade!")
