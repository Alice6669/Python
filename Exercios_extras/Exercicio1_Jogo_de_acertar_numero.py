# Criar um jogo que o usuário irá tentar acertar um número dentro de um intervalo.

# Importações.
import os
import random

# Método para tentar a sorte.
def sorte():
    return random.randint(0, 1)

# Inicio do jogo.
print("\nBem vindo(a) ao Adivinhe o Número!")
print(f"Nesse jogo você terá que tentar adivinhar um número dentro de\n"\
      f"um intervalo que escolher. (0 para não e 1 para sim)\n\n")
contadorPartidas = 0
mesmoIntervalo = 0
inicio = 0
fim = 100
while True:

    # Coletando dados para gerar o número.
    contadorPartidas += 1
    if contadorPartidas != 1:
        while True:
            try:
                mesmoIntervalo = int(input("Você quer usar o mesmo intervalo? "))
            except ValueError:
                continue
            if mesmoIntervalo not in [0, 1]:
                continue
            break
    if mesmoIntervalo == 0:
        while True:
            try:
                inicio = int(input("Qual o menor valor do intervalo? "))
            except ValueError:
                continue
            break
        while True:
            try:
                fim = int(input("Qual o maior valor do intervalo? "))
            except ValueError:
                continue
            break

    # Gerando numero.
    numeroSorteado = random.randint(inicio, fim)

    # Menu para tentar acertar o número.
    numeroTentado = 0
    contadorTentativas = 1
    parImparTentativas = 3
    sinalTentativas = 3
    maiorMenorTentativas = 20
    opcao = 0
    numerosTentados = []
    while True:
        while True:
            try:
                numeroTentado = int(input("\nQual valor quer tentar? "))
            except ValueError:
                continue
            break
        if numeroTentado == numeroSorteado:
            print(f"\nVocê acertou na tentativa numero {contadorTentativas}!\n"\
                  f"O número era {numeroSorteado}")
            break
        else:
            numerosTentados.append(numeroTentado)
            print(f"Numeros errados: {numerosTentados}")
            while True:
                try:
                    opcao = int(input("O que você quer tentar?(A tentaiva pode" \
                        f" falhar 50%)\n"\
                        f"0 - Ver se o número é maior ou menor (tentativas "\
                        f"{maiorMenorTentativas})\n"\
                        f"1 - Ver se o número é impar ou par (tentativas "\
                        f"{parImparTentativas})\n"\
                        f"2 - Ver o sinal do número (tentativas "\
                        f"{sinalTentativas})\n"\
                        f"3 - Seguir para proxima parte\n"))
                except ValueError:
                    continue
                if opcao not in [0, 1, 2, 3]:
                    continue
                break

        # Processando o que falar do número.
        if opcao == 0:
            if maiorMenorTentativas > 0:
                maiorMenorTentativas -= 1
                print(f"O {numeroTentado} é maior que o sorteado" \
                    f"? {numeroTentado > numeroSorteado}")
            else: 
                print("Falhou")
        elif opcao == 1:
            if parImparTentativas > 0:
                parImparTentativas -= 1
                if sorte():
                    print(f"O número sorteado é par" \
                        f"? {bool(numeroSorteado % 2 == 0)}")
                else: 
                    print("Falhou")
            else: 
                print("Falhou")
        elif opcao == 2:
            if sinalTentativas > 0:
                sinalTentativas -= 1
                if sorte():
                    print(f"O numero sorteado é negativo" \
                        f"? {numeroSorteado < 0}")
                else: 
                    print("Falhou")
            else: 
                print("Falhou")

        # Vendo se o usuário quer tentar outro valor ou desistir.
        while True:
            try:
                tentarNumero = int(input("Você quer tentar outro número? "))
            except ValueError:
                continue
            if tentarNumero not in [0, 1]:
                continue
            break
        if not tentarNumero:
            print(f"Você desistiu na tentativa número {contadorTentativas}")
            break
        contadorTentativas += 1

    # Vendo se o usuário quer jogar outro vez fechar o jogo.
    while True:
        try:
            tentarNumero = int(input("Você quer jogar de novo? "))
        except ValueError:
            continue
        if tentarNumero not in [0, 1]:
            continue
        break
    if not tentarNumero:
        print(f"Você jogou {contadorPartidas} partidas \n" \
              f"Fechando jogo")
        break
    os.system('cls' if os.name == 'nt' else 'clear')