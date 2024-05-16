import random

def calcular_pontuacao(tentativas_restantes):
    if tentativas_restantes == 5:
        return 5
    elif tentativas_restantes == 4:
        return 4
    elif tentativas_restantes == 3:
        return 3
    elif tentativas_restantes == 2:
        return 2
    else:
        return 1

def jogar_jogo():
    numero_correto = random.randint(1, 10)
    tentativas = 5
    
    print("Bem-vindo ao jogo de adivinhação! Você tem 5 tentativas para adivinhar o número de 1 a 10.")
    
    while tentativas > 0:
        print("\nTentativas restantes:", tentativas)
        palpite = int(input("Digite seu palpite: "))
        
        if palpite == numero_correto:
            pontuacao = calcular_pontuacao(tentativas)
            print("Parabéns! Você acertou o número!")
            print("Sua pontuação é:", pontuacao)
            break
        else:
            if palpite > numero_correto:
                print("Tente um número menor.")
            else:
                print("Tente um número maior.")
            
            tentativas -= 1

    if tentativas == 0:
        print("\nVocê não conseguiu adivinhar o número. O número correto era:", numero_correto)

if __name__ == "__main__":
    while True:
        jogar_jogo()
        continuar = input("Deseja jogar novamente? (s/n): ")
        if continuar.lower() != 's':
            break