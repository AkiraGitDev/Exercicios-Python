"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media = (n1 + n2) / 2

if media >= 7:
    print("Parabéns, você foi APROVADO com uma média de {:.1f}!".format(media))
elif media <= 6.9 and media >= 5:
    print("Você está de RECUPERAÇÃO. Estude para a prova...")
    print("Sua média é {}.".format(media))
else:
    print("Você está REPROVADO...")
    print("Sua média foi {}...".format(media))