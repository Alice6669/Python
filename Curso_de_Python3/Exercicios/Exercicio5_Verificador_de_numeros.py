# Coletando número.
print("Digite um número inteiro")
numero = input()
# Verificando se é número.
try:
    float(numero)
    # Verificando se é um número inteiro.
    try: 
        numero = int(numero)
        # Verificando se é um numero par.
        if numero % 2 == 0:
            print("Esse número é par!")
        else:
            print("Esse número é impar!")
    except ValueError: 
        print("Digite um número inteiro!")
except ValueError:
    print("Digite um número!")

    

