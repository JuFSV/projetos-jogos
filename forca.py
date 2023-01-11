import random

def jogar():

    print("---------------------------------------")
    print("|     Bem vindo ao jogo de Forca!     |")
    print("| Tente descobrir a palavra secreta!  |")
    print("---------------------------------------")
    print("|         DICA: É uma fruta!          |")
    print("---------------------------------------")

    arquivo = open("lista_de_palavras.txt")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_corretas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_corretas)
    
    while(not enforcou and not acertou):

        chute = input("\nDigite uma letra: ")
        chute = chute.strip().upper()
        print("Você digitou {}.\n".format(chute))

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_corretas[index] = letra
                index += 1
        else:
            erros +=1
            desenha_forca(erros)
                
        enforcou = erros == 7
        acertou = "_" not in letras_corretas
        print(letras_corretas)
            
    if (acertou):
        print("Parabéns, você ganhou!")
    else:
        print("Que pena, você morreu enforcado!\nA palavra era {}.".format(palavra_secreta))

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
            
if(__name__ == "__main__"):
    jogar()