import random
import os

def jogar():

    palavra_secreta = carrega_palavra_secreta()

    enforcou = False
    acertou = False
    chute_repetido = True
    chutes = []
    acertos = []
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    max_tentativas = 6
    erros = 0
    tentativas = 1
    boneco = [" ", " ", " ", " ", " ", " "]

    while (not enforcou and not acertou):

        #Testa se a letra á foi usada
        while (chute_repetido):

            imprime_mensagem_abertura()

            print("Letra(s) usada(s) {}". format(chutes))
            print("{}".format(letras_acertadas))
            chute = input("Digite uma Letra: ").upper()
            os.system("cls") or None
            chute = chute.strip()
            chute = chute[0]
            if (chute not in chutes) :
                chutes.append(chute)
                chute_repetido = False
            else :
                print("A letra {} já foi usada !!! ".format(chute))
        chute_repetido = True
        if (chute in palavra_secreta) :
            index = 0
            print("A letra digitada foi", chute)
            for letra in palavra_secreta:
                if (chute == letra) :
                    print("Encontrei a letra {} na posição {}.".format(letra, index+1))
                    letras_acertadas[index] = chute
                    acertos.append(letra)
                else :
                    tentativas += 1

                if "_" not in letras_acertadas :
                    acertou = True
                index = index + 1
        else :
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(max_tentativas - erros))

        if erros == 1 :
            boneco[0] = ' O '
        elif erros == 2 :
            boneco[1] = '/| '
        elif erros == 3 :
            boneco[1] = "/|\\"
        elif erros == 4 :
            boneco[2] = ' | '
        elif erros == 5:
            boneco[3] = '/  '
        elif erros == 6:
            boneco[3] = '/ \\'
        enforcou = max_tentativas == erros

        print("  ------------ ")
        print("  |           |")
        for linha in range(0, 6):
            print("  |          {}".format(boneco[linha]))
        print("  |            ")
        print("----------")

    if acertou :
        print("Você ganhou !!!")
    else :
        print("Você perdeu !!!")

    print("Fim de Jogo!")

def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Forca !     ")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()
    palavra_selecionada = random.randrange(0, len(palavras))
    palavra_secreta = palavras[palavra_selecionada]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if (__name__ == '__main__'):
    jogar()

