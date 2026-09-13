# Coletando váriaveis.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite mais um número: "))

# Condicionais para sinal da variavel

if numero1 < 0:
    if numero2 < 0:
        print("Ambos os números são negativos")
    elif numero2 == 0:
        print("O 1º número é negativo e o 2º número é nulo")
    else: 
        print("O 1º número é negativo e o 2º número é positivo")
elif numero2 < 0:
    if numero1 == 0:
        print("O 2º número é negativo e o 1º número é nulo")
    else:
        print("O 2º numero é negativo e o 1º número é positivo")
elif numero1 == 0:
    if numero2 == 0:
        print("Ambos os número são nulos")
    else:
        print(("O 2º número é positivo e o 1º é nulo"))
elif numero2 == 0:
    if numero1 == 0:
        print("Ambos os número são nulos")
    else:
        print(("O 1º número é positivo e o 2º é nulo"))
else:
    print("Ambos os números são positivos")
    