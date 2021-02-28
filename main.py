def computador_escolhe_jogada(fn, fm):
    repetir = True
    pecas_tirar_pc = 1
    aux = fn
    while pecas_tirar_pc <= fm and repetir:
        fn = aux - pecas_tirar_pc
        if fn % (fm + 1) == 0:
            repetir = False
        else:
            pecas_tirar_pc = pecas_tirar_pc + 1
    if pecas_tirar_pc == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", pecas_tirar_pc, "peças.")

    return pecas_tirar_pc


def usuario_escolhe_jogada(fn, fm):
    repetir = True
    while repetir == True:
        pecas_tirar = int(input("Quantas peças você vai tirar? "))
        print("")
        if pecas_tirar <= fm and pecas_tirar > 0:
            repetir = False
        else:
            print("Oops! Jogada inválida! Tente de novo.")
            print("")

    if pecas_tirar == 1:
        print("Você tirou uma peça.")
    else:
        print("Voce tirou", pecas_tirar, "peças.")

    return pecas_tirar


def sobra(fn):
    if fn == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
        print("")
    elif fn > 1:
        print("Agora restam", fn, "peças no tabuleiro.")
        print("")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    if n % (m + 1) == 0:
        print("Voce começa!")
        print("")
        while n > 0:
            tiradas = usuario_escolhe_jogada(n, m)
            n = n - tiradas
            sobra(n)
            if n == 0:
                print("Você ganhou!")
                print("")
            else:
                tiradas_pc = computador_escolhe_jogada(n, m)
                n = n - tiradas_pc
                sobra(n)

                if n == 0:
                    sobra(n)
                    print("Fim do jogo! O computador ganhou!")
                    print("")

    else:
        print("Computador começa!")
        print("")
        while n > 0:
            tiradas_pc = computador_escolhe_jogada(n, m)
            n = n - tiradas_pc
            sobra(n)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                print("")
            else:
                tiradas = usuario_escolhe_jogada(n, m)
                n = n - tiradas
                sobra(n)
                if n == 0:
                    print("Você ganhou!")
                    print("")


def campeonato():
    rodada = 1
    while rodada <= 3:
        print("**** Rodada", rodada, "****")
        print("")
        partida()
        rodada = rodada + 1


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    print("")
    tipo_game = int(input())
    print("")

    if tipo_game == 1:
        print("Voce escolheu uma partida isolada!")
        print("")
        partida()

    else:
        print("Voce escolheu um campeonato!")
        print("")
        campeonato()
        print("")
        print("**** Final do campeonato! *****")
        print("")
        print("Placar: Você 0 x 3 Computador")


main()