"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""
import datetime

ano_atual = datetime.datetime.today().year
nascimento = int(input("Insira o ano de nascimento do atleta: "))
idade = ano_atual - nascimento

if idade <= 9:
    print("Com {} anos de idade, a classificação do atleta é MIRIM.".format(idade))
elif idade >= 10 and idade <= 14:
    print("Com {} anos de idade, a classificação do atleta é INFANTIL.".format(idade))
elif idade >= 15 and idade <= 19:
    print("Com {} anos de idade, a classificação do atleta é JÚNIOR.".format(idade))
elif idade >= 20 and idade <= 25:
    print("Com {} anos de idade, a classificação do atleta é SÊNIOR.".format(idade))
else:
    print("Com {} anos de idade, a classificação do atleta é MASTER.".format(idade))
