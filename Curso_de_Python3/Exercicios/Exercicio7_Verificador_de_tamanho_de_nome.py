# Coletando nome.
print("Qual o seu nome?")
nome = input("")

if nome != "":
    if len(nome) < 5:
        print("Seu nome é curto")
    elif len(nome) < 7: 
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")