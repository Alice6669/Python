# Jogo da forca tradicional com palavras de uma lista fixa.

# Importes.
import random
import os

# Fonte dos dados.
palavrasStr = "abacaxi montanha velocidade azul computador "\
    "janela elefante melancia livro sapato caneta telefone "\
    "cadeira garrafa nuvem tempestade foguete bicicleta "\
    "planeta oceano teclado guitarra formiga estrela papel "\
    "gravata barco trem espelho cachorro gato cidade pintura "\
    "chocolate sorriso porta vidro vento lua sol estrada areia "\
    "peixe tigre macaco folha pedra luz sombra fogo gelo copo "\
    "prato garfo faca colher parede teto tapete quadro foto "\
    "festa amigo carro ponte rio lago mar ilha praia concha "\
    "navio farol mapa tesouro caverna parque escorregador bola "\
    "boneca carrinho urso travesseiro cobertor cama sonho noite "\
    "dia tarde madrugada chuva neve nevasca terremoto tsunami "\
    "deserto cacto camelo escaravelho templo castelo rei rainha "\
    "princesa cavaleiro espada escudo armadura flecha arco magia "\
    "bruxa mago varinha vassoura fada duende gnomo gigante floresta "\
    "bosque selva vale colina desfiladeiro abismo universo cometa "\
    "meteoro asteroide astronauta nave laser ciborgue futuro "\
    "passado presente tempo ampulheta ano semana hora minuto "\
    "segundo instante momento eternidade vida morte nascimento "\
    "crescimento movimento energia tecido corpo mente alma "\
    "pensamento sentimento alegria tristeza raiva medo amor "\
    "desejo vontade coragem covardia desespero certeza verdade "\
    "mentira segredo enigma resposta pergunta problema desafio "\
    "derrota sucesso fracasso honra vergonha orgulho humildade "\
    "paz guerra conflito harmonia liberdade lei regra ordem caos "\
    "anarquia borracha tesoura cola caderno mochila lousa giz "\
    "apagador professor aluno escola universidade diploma formatura "\
    "trabalho emprego dinheiro moeda nota banco cofre economia "\
    "mercado loja supermercado feira padaria hospital enfermeiro "\
    "vacina cura tratamento cirurgia lente contato olfato paladar "\
    "tato sentido pele osso sangue intestino rim veia nervo"
letrasStr = "abcdefghijklmnopqrstuvwxyz"

letrasLista = list(letrasStr)
palavrasLista = palavrasStr.split(" ")

# Criptografando palavra.
contador = 0
while True:
    indiceResposta = random.randint(0, (len(palavrasLista) -1))
    resposta = palavrasLista[indiceResposta]
    respostaCripto = len(resposta) * "_"

    # Interface do jogo.
    contadorErros = 0
    letrasListaTentadas = []
    while True:
        if contadorErros == 0:
            print("------\n|    |\n|\n|\n|\n|\n 7 vidas")
        elif contadorErros == 1:
            print("------\n|    |\n|    º\n|\n|\n|\n 6 vidas")
        elif contadorErros == 2:
            print("------\n|    |\n|    º\n|    |\n|\n|\n 5 vidas")
        elif contadorErros == 3:
            print("------\n|    |\n|    º\n|   /|\n|\n|\n 4 vidas")
        elif contadorErros == 4:
            print("------\n|    |\n|    º\n|   /|\ \n|\n|\n 3 vidas")
        elif contadorErros == 5:
            print("------\n|    |\n|    º\n|   /|\ \n|   /\n|\n 2 vidas")
        elif contadorErros == 6:
            print("------\n|    |\n|    º\n|   /|\ \n|   / \ \n|\n 1 vida")
        else :
            print("Você perdeu!")

        print(f"\n\n      {letrasListaTentadas}\n      {respostaCripto}")

        if contadorErros == 7:
            break

        # Pegando letra.
        letraTentada = ""
        while True:
            letraTentada = input("Qual letra você quer tentar?   ").lower()
            if letraTentada in letrasLista:
                break
            print("\nVALOR INVÁLIDO!\n")
            continue

        # Procurando letra
        respostaCriptoTemp = ""
        for indice, letra in enumerate(resposta):
            if letra == letraTentada:
                respostaCriptoTemp += letra
                continue
            respostaCriptoTemp += respostaCripto[indice]

        # Conferindo resposta
        if respostaCriptoTemp == respostaCripto:
            contadorErros += 1
            if contadorErros == 7:
                respostaCripto = resposta
        elif respostaCriptoTemp == resposta:
            print (f"Você acertou! A resposta é: {resposta}")
            break
        else:
            respostaCripto = respostaCriptoTemp
        letrasListaTentadas.append(letraTentada)

    # Conferindo se o usuário quer jogar de novo.
    contador += 1
    jogar = -1
    while True:
        try:
            jogar = int(input("Você quer Jogar de novo? (0->Não/1->Sim)"))
        except ValueError:
            continue
        if jogar not in [0, 1]:
            continue
        break
    if jogar == 0:
        break
    palavrasLista.remove(resposta)
    os.system("cls" if os.name == 'nt' else 'clear')

# Fechando programa.
print(f"Fechando programa, número de jogos: {contador}.")
    