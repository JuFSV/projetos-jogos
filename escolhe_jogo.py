import forca
import adivinhacao

def escolhe_jogo():

    print("--------------------------------")
    print("|     Escolha qual jogo:       |")
    print("| (1) Adivinhação ou (2) Forca |")
    print("--------------------------------")

    escolha = int(input("\nDigite 1 ou 2: "))

    if(escolha == 1):
        adivinhacao.jogar()
    else:
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()