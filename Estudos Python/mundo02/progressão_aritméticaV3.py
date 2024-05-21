"""
Melhore o DESAFIO Progressão Aritmética V2, perguntando para o usuário se ele quer mostrar mais alguns termos. Adicione opções para o usuário escolher se quer adicionar mais termos ou não.
"""

print("=" * 30)
print("10 TERMOS DE UMA PA (COM WHILE)")
print("=" * 30)

primeiro = int(input("Insira o primeiro termo da PA: "))
razao = int(input("Insira a razão da PA: "))
termo = primeiro
contador = 1

# Inicializando a contagem total de termos exibidos
total_termos_exibidos = 0

# Exibindo os 10 primeiros termos
while contador <= 10:
    print(termo)
    termo += razao
    contador += 1

# Atualizando a contagem total de termos exibidos
total_termos_exibidos += 10

while True:
    opcao = input("Gostaria de mostrar mais termos? (s/n): ").strip().lower()

    if opcao == "n":
        break
    elif opcao == "s":
        termos = int(input("Quantos termos a mais você gostaria?: "))
        contador = 1

        while contador <= termos:
            print(termo)
            termo += razao
            contador += 1

        # Atualizando a contagem total de termos exibidos
        total_termos_exibidos += termos
    else:
        print("Opção inválida. Insira novamente.")

print("Programa finalizado com {} termos.".format(total_termos_exibidos))
print("FIM DO PROGRAMA")
