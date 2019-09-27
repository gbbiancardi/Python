import random

def jogar():
    print("=================================")
    print("Bem vindo ao jogo de Adivinhação!")
    print("=================================")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Normal (3) Difícil")
    nivel = int(input("Digite o nível desejado: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas == 5

    # while (rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Número inválido! O número deve ser entre 1 e 100!")
            continue

        acertou     = chute == numero_secreto
        chute_alto  = chute > numero_secreto
        chute_baixo = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (chute_alto):
                print("Você errou! Seu chute foi muito alto!")
            elif (chute_baixo):
                print("Você errou! Seu chute foi muito baixo!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()
