# Coletando variaveis.

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

if not nome or not idade:
    print("Desculpe, você deixou campos vázios")
else:
    print(f"Seu nome é {nome}.")
    print(f"Sua idade é {idade}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome tem espaço")
    else:
        print("Seu nome não tem espaço")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[len(nome)-1]}")