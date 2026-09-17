# Jogo da velha em que o jogador pode jogar contra uma pessoa ou contra o computador.

# importações
import os
import random

# Velha (função que decide onde o computador írá jogar).
def velha(gradeVelha: list[list[str]], simbolo: str):
    lugaresPosiveis = []
    for indice, linha in enumerate(gradeVelha):
        for indiceInterno, posicao in enumerate(linha):
            if (posicao == " "):
                lugaresPosiveis.append(str(indice) + str(indiceInterno))
    posicao = random.randint(0, len(lugaresPosiveis))
    if (lugaresPosiveis[posicao - 1][0] == "0"):
        gradeVelha[0][int(lugaresPosiveis[posicao - 1][1])] = simbolo
    elif (lugaresPosiveis[posicao - 1][0] == "1"):
        gradeVelha[1][int(lugaresPosiveis[posicao - 1][1])] = simbolo
    else:
        gradeVelha[2][int(lugaresPosiveis[posicao - 1][1])] = simbolo
    return gradeVelha

# Jogador (Salvando jogada do jogador.)
def jogador(gradeVelha: list[list[str]], simbolo: str):
    while True:
        coluna = coletorNumero("Você quer jogar em qual linha? (0 a 2) ", [0, 1, 2])
        linha = coletorNumero("Você quer jogar em qual coluna? (0 a 2) ", [0, 1, 2])
        if jogadaPossivel(gradeVelha, coluna, linha) == True:
            break
        print("Local ocupado!")     
    gradeVelha[coluna][linha] = simbolo
    return gradeVelha

# Verificador de jogada possível.
def jogadaPossivel(gradeVelha: list[list[str]], coluna: int, linha: int):
    if gradeVelha[coluna][linha] == " ":
        return True
    return False

# Verificador de ganhador.
# Pega o símbolo de quem ganhou.
def simbologanhou(gradeVelha: list[list[str]]):
    for linha in gradeVelha:
        posicao1 = linha[0]
        for indice, posicaoAtual in enumerate(linha[1:]):
            if posicaoAtual == posicao1:
                if indice == 1 and posicao1 != " ":
                    return ganhou(posicao1)
            else :
                break

    if ((gradeVelha[0][0] == gradeVelha[1][1] and gradeVelha[2][2] == gradeVelha[1][1]) or \
        (gradeVelha[0][2] == gradeVelha[1][1] and gradeVelha[2][0] == gradeVelha[1][1])) and \
        gradeVelha[1][1] != " ":
        return ganhou(gradeVelha[1][1])
    
    if gradeVelha[0][0] == gradeVelha[1][0] and gradeVelha[2][0] == gradeVelha[1][0] and \
            gradeVelha[1][0] != " ":
        return ganhou(gradeVelha[0][0])

    if gradeVelha[0][1] == gradeVelha[1][1] and gradeVelha[2][1] == gradeVelha[1][1] and \
                gradeVelha[1][1] != " ":
            return ganhou(gradeVelha[0][1])

    if gradeVelha[0][2] == gradeVelha[1][2] and gradeVelha[2][2] == gradeVelha[1][2] and \
                gradeVelha[1][2] != " ":
            return ganhou(gradeVelha[0][2])

    posicaoVazia = False
    for linha in gradeVelha:
        for posicao in linha:
            if (posicao == " "):
                posicaoVazia = True
                break
        if posicaoVazia:
            break
    if posicaoVazia == False:
        return ganhou("E")
    return ganhou(" ")

# Ver de quem é o símbolo ganhador.
def ganhou(simbolo: str):
    if simbolo == "E":
        return -1
    elif simbolo == " ":
        return 0
    elif simbolo == simboloJogador:
        return 1
    return 2


# Coletor de números.
def coletorNumero (mensagem: str, numerosPosiveis: list[int] ):
    while True:
        try:
            resposta = int(input(mensagem))
        except (ValueError):
            print("VALOR INVÁLIDO!")
            continue
        if resposta not in numerosPosiveis:
            print("VALOR INVÁLIDO!")
            continue
        return resposta

# Main do jogo.
contadorJogos = 0
jogador1Pontos = 0
jogador2Pontos = 0
empates = 0
velhaPontos = 0
simboloJogador = ""
simboloOutro = ""
while True:

    # Pegando dados gerais do jogo.
    seguirPadrão = -1
    if contadorJogos > 0:
        seguirPadrão = coletorNumero("Você quer mudar os dados?\n(Não -> 0/Sim -> 1) ", [0, 1])
    if seguirPadrão != 0:
        contadorJogos = 0
        empates = 0

        # Coletando simbolo a ser jogado
        simboloJogador = "X"
        simboloOutro = "O"
        selecionarSimbolo = coletorNumero("Com qual símbolo você quer jogar?\n(O -> 0/X -> 1) ", [0, 1])
        if selecionarSimbolo == 0:
            simboloJogador = "O"
            simboloOutro = "X"

        # Vendo contra quem irá jogar.
        selecionarJogador = coletorNumero("Contra quem você quer jogar?\n(Velha -> 0/Jogador 2 -> 1) ", [0, 1])

        # Pegando nome(s) do(s) jogadore(s).
        jogador1Nome = input("Qual o nome do Jogador 1? ").capitalize()
        jogador1Pontos = 0
        if selecionarJogador == 1:
            jogador2Nome = input("Qual o nome do Jogador 2? ").capitalize()
            jogador2Pontos = 0
        else:
            jogador2Nome = "Velha"
            velhaPontos == 0
    else:
        contadorJogos += 1

    # Criando tabuleiro
    gradeVelha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Vendo quem joga primeiro.
    jogadorVezes = [1, 2]
    print("Sorteando quem joga primeiro\n\n")
    jogadorVezes[0] = random.randint(1, 2)
    if jogadorVezes[0] == 2:
        jogadorVezes[1] = 1

    # Interface do jogo
    while True:
        venceu = 0
        for vezJogar in jogadorVezes:
            # Mostrando jogo.
            for linha in gradeVelha:
                print(f" {linha[0]} | {linha[1]} | {linha[2]}\n")

            # Coletando posição para jogar.
            if vezJogar == 2 and jogador2Nome == "Velha":
                print(f"Vez de {jogador2Nome}.")
                gradeVelha = velha(gradeVelha, simboloOutro)
            elif vezJogar == 2 and jogador2Nome != "Velha":
                print(f"Vez de {jogador2Nome}.")
                gradeVelha = jogador(gradeVelha, simboloOutro)
            else:
                print(f"Vez de {jogador1Nome}.")
                gradeVelha = jogador(gradeVelha, simboloJogador)

            # Verificando se alguem ganhou.
            venceu = simbologanhou(gradeVelha)
            if  venceu == 1:
                jogador1Pontos += 1
                print(f"{jogador1Nome} ganhou a partida {contadorJogos + 1}\n Placar: {jogador1Nome} " \
                    f"{jogador1Pontos} pontos | {jogador2Nome} {jogador2Pontos} pontos "\
                    f"| {empates} empates")
                break
            elif venceu == 2:
                jogador2Pontos += 1
                print(f"{jogador2Nome} ganhou a partida {contadorJogos + 1}\n Placar: {jogador1Nome} " \
                f"{jogador1Pontos} pontos | {jogador2Nome} {jogador2Pontos} pontos"\
                f"| {empates} empates")
                break
            elif venceu == -1:
                empates += 1
                print(f"Deu empate!\n Placar: {jogador1Nome} " \
                    f"{jogador1Pontos} pontos | {jogador2Nome} {jogador2Pontos} pontos"\
                    f"| {empates} empates")
                break

        if venceu != 0:
            break
        
    # Vendo se que jogar de novo.
    jogarDeNovo = coletorNumero("Você quer Jogar de novo? (0->Não/1->Sim)", [0, 1])
    if jogarDeNovo == 1:
        os.system("cls" if os.name == 'nt' else 'clear')
        contadorJogos += 1
        continue
    break

# Finalizando jogo.
print(f"Fechando programa, número de jogos: {contadorJogos + 1}.")
    
    