import os
while True:
    # Coletando palavra.
    while True:
        print("Qual a palavra secreta?")
        palavra = input("")
        if palavra == "":
            print("Você não pode deixar a palavra secreta em branco!")
        else:
            break
    os.system("cls" if os.name == "nt" else "clear")
    
    # Criptografando palavra.
    palavraCriptografada = "*" * len(palavra)
    palavraSalva = palavraCriptografada
    contador = 0

    # Jogando.
    while True:
        # Perguntando letra.
        while True:
            print("Qual letra você quer tentar?")
            letraTentada = input("")
            if letraTentada == "" or len(letraTentada) > 1:
                print("Você deve digitar uma letra!")
            else:
                break

        # Procurando letra.
        palavraCriptografada = ""
        palavraTemporaria = ""
        contadorFor = range(len(palavra))
        for letra in palavra:
            if letra != letraTentada:
                palavraCriptografada += "*"
            else:
                palavraCriptografada += letraTentada
        for numero in contadorFor:
            if palavraSalva[numero] != palavraCriptografada[numero] and palavraCriptografada[numero] != "*":
                palavraTemporaria += palavraCriptografada[numero]
            elif palavraSalva[numero] != "*":
                palavraTemporaria += palavraSalva[numero]
            else:
                palavraTemporaria += "*"
        palavraSalva = palavraTemporaria
        contador += 1
        
        # Mostrando como está a palavra após a tentativa.
        if palavraSalva != palavra:
            print('Palavra criptografada: "', palavraSalva, '"')
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print('Você acertou a palavra em ', contador, " tentativas.")
            print('A palavra secreta era: "', palavra, '"')
            break

    # Vendo se o jogador quer jogar de novo
    while True:
        print("Você quer jogar de novo? (S/N)?")
        verificadorContinuação = input()
        if verificadorContinuação != "S" and verificadorContinuação != "N":
            print ("Digite uma resposta válida!")
        else:
            break 
    if verificadorContinuação == "N":
        break

# Finalizando jogo
print("Finalizando jogo")