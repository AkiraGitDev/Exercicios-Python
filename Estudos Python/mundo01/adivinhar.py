"""
1 - Desenvolva um jogo de "acerte o número", onde o computador escolhe um número inteiro aleatório de 0 a 10, e o usuário tem 5 tentativas para adivinhar o número.

2 - Implemente um sistema de pontuação com o seguinte comportamento: se o usuário adivinhar o número na primeira tentativa, receberá a pontuação máxima (100 pontos); se o usuário acertar o número em nas tentativas 4 a 2, receberá metade dos pontos (50 pontos); e se acertar na última tentativa receberá a pontuação mínima (10 pontos). Se o usuário não acertar o número, não recebe pontos.

3 - Implemente um controle de erros. Caso o jogador digite um número fora da faixa permitida ou caracteres não numéricos, o sistema deve notificar o jogador e solicitar o input correto.

4 - Implemente a opção de o usuário iniciar uma nova partida. Ao finalizar uma rodada, após o resultado final, o jogo deve perguntar se o jogador quer iniciar uma nova partida e, em caso negativo, encerrar a aplicação.
"""
import random

tentativas_maximas = 5
pontuacao_maxima = 100
pontuacao_minima = 10

def obter_palpite(tentativa_atual):
    while True:
        try:
            palpite = int(input("Tentativa {}: Qual é o número escolhido? (entre 0 e 10): ".format(tentativa_atual + 1)))
            if palpite < 0 or palpite > 10:
                print("Por favor, insira um número entre 0 e 10.")
            else:
                return palpite
        except ValueError:
            print("Por favor, insira um número válido.")

def jogar_jogo():
    numero_aleatorio = random.randint(1, 10)
    pontuacao = 0
    
    for tentativa_atual in range(tentativas_maximas):
        palpite = obter_palpite(tentativa_atual)
    
        if palpite == numero_aleatorio:
            if tentativa_atual == 0:
                pontuacao += pontuacao_maxima
            elif tentativa_atual >= 1 and tentativa_atual <= 3:
                pontuacao += pontuacao_maxima // 2
            else:
                pontuacao += pontuacao_minima
                
            print("Parabéns! Você acertou o número.")
            print("Pontuação desta rodada: {}".format(pontuacao))
            return pontuacao
        else:
            print("Ops! Tente novamente.")

            if palpite > numero_aleatorio:
                print("Está mais para baixo...")
            else:
                print("Está mais para cima...")

    print("Suas {} tentativas acabaram. O número correto era {}.".format(tentativas_maximas, numero_aleatorio))
    return pontuacao

pontuacao_total = 0
while True:
    pontuacao_total += jogar_jogo()
    continuar = input("Deseja jogar novamente? (s/n): ")
    if continuar.lower() != "s":
        break

print("Pontuação total: {}".format(pontuacao_total))
