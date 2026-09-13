# Criando lista.
import os
compras = []
while True:
    
    # Coletando o que devo fazer.
    while True:
        print("O que você quer fazer com a lista de compras?")
        print("(i)Inserir item  (m)Mudar quantidade de um item (a)Apagar item (c)Marcar comprado em um item (l)Ler lista")
        opcaoParaAcao = input("")
        if opcaoParaAcao != "i" and opcaoParaAcao != "a" and opcaoParaAcao != "l" and opcaoParaAcao != "m" and opcaoParaAcao != "c":
            print("Ação inreconhecivel!")
        else:
            break
    
    # Identificando 
    os.system("cls" if os.name == "nt" else "clear")
    if opcaoParaAcao == "i":

        # Selecionando o que devo inserir na lista.
        while True:
            print("O que devo inseir na lista?")
            novoItem = input("")
            if novoItem == "":
                print("Adicione um item válido!")
            else:
                break
        while True:
            print("Qual a quantidade do produto?")
            novaQuantidade = input("")
            if novaQuantidade == "":
                print("Adicione um valor válido!")
            else:
                break

        # Adicionando item à lista.
        listaTemporaria = [novoItem, novaQuantidade, "Não"]
        compras.append(listaTemporaria)
    elif opcaoParaAcao == "m":

        # Coletando dados para altera na lista
        while True:
            print("Qual o indice do item que quer alterar a quantidade?")
            indice = input("")
            try:
                indice = int(indice)
            except ValueError:
                print("Digite um número inteiro!")
                continue
            if indice < 0 or indice >= len(compras):
                print("Diga um indice válido!")
            else:
                break
        while True:
            print("Qual a quantidade do produto?")
            novaQuantidade = input("")
            if novaQuantidade == "":
                print("Adicione um valor válido!")
            else:
                break

        # Mudando quantidade na lista.
        compras[indice][1] = novaQuantidade
    elif opcaoParaAcao == "a":
    
        # Coletando dado para apagar na lista.
        while True:
            print("Qual o indice do item que quer apagar?")
            indice = input("")
            try:
                indice = int(indice)
            except ValueError:
                print("Digite um número inteiro!")
                continue
            if indice < 0 or indice >= len(compras):
                print("Diga um indice válido!")
            else:
                break
                
        # Apagando item.
        compras.pop(indice)
    elif opcaoParaAcao == "c":
    
        # Coletando dado para marcar como comprado na lista.
        while True:
            print("Qual o indice do item que quer marcar?")
            indice = input("")
            try:
                indice = int(indice)
            except ValueError:
                print("Digite um número inteiro!")
                continue
            if indice < 0 or indice >= len(compras):
                print("Diga um indice válido!")
            else:
                break

        # Marcando item como comprado na lista.
        compras[indice][2] = "Sim"
    else:
    
        # Mostrando Lista
        os.system("cls" if os.name == "nt" else "clear")
        print("Lista de compras:")
        if compras == []:
            print("Lista vazia")
        else:
            print("Indice |      Item      |     Quantidade    | Comprado?")
            for indice, item in enumerate(compras):
                print(indice, "     ", item[0], " --- ", item[1], " --- ", item[2])

    # Vendo o que fazer agora.
    while True:
        
        print("Você quer fechar a lista? (S/N)?")
        verificadorContinuação = input()
        if verificadorContinuação != "S" and verificadorContinuação != "N":
            print ("Digite uma resposta válida!")
        else:
            break 
    if verificadorContinuação == "S":
        break

# Finalizando jogo
print("Finalizando lista")