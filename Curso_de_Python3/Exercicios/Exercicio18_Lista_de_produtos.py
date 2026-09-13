# Criar uma lista de produtos com nome e preço, dar possibilidade do usuário alterá-lo
# e ordenar a lista.

produtos = []

while(True):
    # Tela de opções do que o usuário pode fazer.
    print()
    print("O Que você quer fazer com os produtos(digite o que há no parenteses)? ")
    acao = input("Criar(C)-----Ler(L)-----Alterar(A)-----Excluir(E)-----Sair(S) ").upper()
    print()

    #Ação de criar
    if acao == "C":
        nome = input("Qual o nome do produto? ")
        while(True):
            preco = input("Qual o preço desse produto? ")
            try:
                preco = float(preco)
            except:
                print("O preço deve ser um número.")
                continue
            if preco <= 0:
                print("O preço deve ser maior que zero.")
            else:
                break
        produtos.append({'nome': nome, 'preco': preco})
        #Ação de ler.
    elif acao == "L":
        if len(produtos) == 0:
            print("Lista vazia.")
            continue
        print("Você que ordenar a lista de acordo o que? ")
        ordem = input("Nome(N)-----Preço(P) ").upper()
        direcao = input("Crescente(C)-----Decrescente(D) ").upper()
        if ordem == "N":
            if direcao == "C":
                produtos.sort(key=lambda x: x['nome'])
            else:
                produtos.sort(key=lambda x: x['nome'], reverse=True)
        else:
            if direcao == "C":
                produtos.sort(key=lambda x: x['preco'])
            else:
                produtos.sort(key=lambda x: x['preco'], reverse=True)
        for indice, dicionario in enumerate(produtos):
            print(str(indice + 1) + "-Nome: " + dicionario['nome'] + "-----Preço: " + str(dicionario['preco']))
            print()
    # Ação de alterar os dados.
    elif acao == "A":
        print("O que você quer alterar? ")
        tipo_alteracao = input("Nome(N)-----Preço(P) ").upper()
        nome_atual = input("Qual o nome atual? ")
        if tipo_alteracao == "N":
            nome_novo = input("Qual o nome novo? ")
        else:
            while(True):
                preco_novo = input("Qual o preço desse produto? ")
                try:
                    preco_novo = float(preco_novo)
                except:
                    print("O preço deve ser um número.")
                    continue
                if preco_novo <= 0:
                    print("O preço deve ser maior que zero.")
                else:
                    break
        for indice, dicionario in enumerate(produtos):
            if dicionario['nome'] == nome_atual:
                if tipo_alteracao == "N":
                    dicionario['nome'] = nome_novo
                    break
                else:
                    dicionario['preco'] = preco_novo
                    break
            if indice == len(produtos) - 1:
                print("Não existe esse produto.")
                print()
    # Ação de excluir.
    elif acao == "E":
        nome_excluir = input("Qual o nome do produto que será excluido? ")
        verificacao = input("Tem certeza(S/N)? ").upper()
        if verificacao == "S":
            for indice, dicionario in enumerate(produtos):
                if dicionario['nome'] == nome_excluir:
                    del(produtos[indice])
                    break
                if indice == len(produtos) - 1:
                    print("Não existe esse produto.")
                    print()
    # Acão de sair
    elif acao == "S":
        break

print("Finalizando programa.")