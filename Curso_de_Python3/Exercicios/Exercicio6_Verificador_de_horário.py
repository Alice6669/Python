# Coletando horário.
print("Digite a hora atual")
numero = input()
# Verificando se é número.
try:
    float(numero)
    # Verificando se é um número inteiro.
    try: 
        numero = int(numero)
        # Verificando se é um numero par.
        if numero >= 0 and numero <= 11:
            print("Bom dia!!!")
        elif numero >= 0 and numero <= 17:
            print("Boa tarde!!!")
        elif numero >= 0 and numero <= 23:
            print("Boa noite!!!")
        else:
            print("Esse horário não faz sentido...")
    except ValueError: 
        print("Digite um número inteiro!")
except ValueError:
    print("Digite um número!")

    

