"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

nome = input("Insira o seu nome completo: ").strip()
sobrenome = input("Insira sobrenome para procura: ").strip().lower()

print("Seu nome tem {}? {}".format(sobrenome, sobrenome in nome.lower()))



