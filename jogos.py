import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("Bem vindo Escolha seu Jogo       ")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual Jogo?: "))

    if (jogo == 1):
        print("Jogo Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo Adivinhação")
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()