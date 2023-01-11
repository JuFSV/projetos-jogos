import random

def jogar():

    print("-------------------------------------")
    print("| Bem vindo ao jogo de Adivinhação! |")
    print("| Tente adivinhar o número secreto! |")
    print("-------------------------------------")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Temos os seguintes níveis de dificuldade:")
    print("(1) Fácil - 20 tentativas\n(2) Médio - 10 tentativas\n(3) Difícil - 5 tentativas")
    nivel = int(input("Qual nível deseja? "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas +1):
        print("\nRodada {} de {} tentativas".format(rodada, tentativas))
        chute = int(input("Digite um número de 1 a 100: "))
        print("Você digitou ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("E adivinhou! Parabéns!")
            break

        else:
            if(maior):
                print("E errou... Seu número é maior!")
            elif(menor):
                print("E errou... Seu número é menor!")
            pontos = pontos - 50

    print("\nO número secreto era {} e você fez {} pontos.".format(numero_secreto, pontos))

if(__name__ == "__main__"):
    jogar()