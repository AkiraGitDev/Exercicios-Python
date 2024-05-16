"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime

print("Análise de alistamento militar.")
nascimento = int(input("Insira o seu ano de nascimento: "))
ano_atual = datetime.datetime.today().year
idade = ano_atual - nascimento

print("Quem nasceu em {} tem {} anos no ano atual, {}.".format(nascimento, idade, ano_atual))
genero = input("Insira seu gênero. Masculino ou Feminino (m/f): ")

if genero == "f":
    print("Mulheres não precisam se alistar obrigatoriamente.")
    escolha = input("Quer se alistar de forma voluntária? (s/n): ")
    if escolha == "s":
        if idade == 18:
            print("Seu alistamento é este ano!".format(idade))
        elif idade > 18:
            saldo = idade - 18
            ano = ano_atual - saldo
            print("Seu alistamento passou há {} ano(s).".format(saldo))
            print("Seu alistamento foi em {}.".format(ano))
        else:
            saldo = 18 - idade
            ano = ano_atual + saldo
            print("Seu alistamento será daqui há {} ano(s).".format(saldo))
            print("Seu alistamento será em {}.".format(ano))
    elif escolha == "n":
        print("Você está liberada do alisamento.")

elif genero == "m":
    print("Homens tem alisamento militar obrigatório.")
    if idade == 18:
        print("Seu alistamento é este ano!".format(idade))
    elif idade > 18:
        saldo = idade - 18
        ano = ano_atual - saldo
        print("Seu alistamento passou há {} ano(s).".format(saldo))
        print("Seu alistamento foi em {}.".format(ano))
        print("Obrigado por se alistar!")
    else:
        saldo = 18 - idade
        ano = ano_atual + saldo
        print("Seu alistamento será daqui há {} ano(s).".format(saldo))
        print("Seu alistamento será em {}.".format(ano))
        print("Não esqueça de realizar seu alistamento!")
