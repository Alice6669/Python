while True:
    # Coletando número
    while True:
        print("Qual valor você quer verificar?")
        numero = input("")

        try:
            numero = int(numero)
            break
        except ValueError:
            print("O valor deve ser um número inteiro!")

    # Criando função para ver se é par ou impar
    def parORimpar (numero):
        if numero % 2 == 0:
            print(numero, "é par")
        else:
            print(numero, "é impar")

    # Usando a função
    parORimpar(numero)
    
    # Vendo se quer verificar outro número.
    while True:
        print("Você quer estar outro número? (S/N)?")
        verificadorContinuação = input()
        if verificadorContinuação != "S" and verificadorContinuação != "N":
            print ("Digite uma resposta válida!")
        else:
            break 
    if verificadorContinuação == "N":
        break

print("Finalizando verificador de par ou impar.")