verificador = True
verificadorResultado = "N"

while verificador:
    # Coletando números
    if verificadorResultado == "N":
        verificador2 = True
        while verificador2:
            print("Qual o primeiro número?")
            numero1 = input()
            try:
                numero1 = float(numero1)
                verificador2 = False
            except ValueError:
                print("Digite um número!")

    verificador2 = True
    while verificador2:
        print("Qual o segundo número?")
        numero2 = input()
        try:
            numero2 = float(numero2)
            verificador2 = False
        except ValueError:
            print("Digite um número!")

    # Coletando operação.
    verificador2 = True
    while verificador2:
        print("Qual a operação (digite o número correspondente?")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão inteira")
        print("5. Divisão normal")
        print("6. Resto da divisão")
        print("7. Potenciação")
        operacao = input()
        try:
            operacao = int(operacao)
        except ValueError:
            print("Digite um número!")
            continue
        if operacao > 0 and operacao < 8:
            verificador2 = False
        else:
            print("Digite um número válido!")

    # Fazendo operação.
    resultado = 0
    if operacao < 2:
        resultado = numero1 + numero2
    elif operacao < 3:
        resultado = numero1 - numero2
    elif operacao < 4:
        resultado = numero1 * numero2
    elif operacao < 5:
        resultado = numero1 // numero2
    elif operacao < 6:
        resultado = numero1 / numero2
    elif operacao < 7:
        resultado = numero1 % numero2
    else:
        resultado = numero1 ** numero2

    # Mostrando resultado.
    print("Resultado: ", resultado)

    # Vendo próximo passo.

    verificador2 = True
    while verificador2:
        print("Você quer fazer outra operação? (S/N)?")
        verificadorContinuação = input()
        if verificadorContinuação != "S" and verificadorContinuação != "N":
            print ("Digite uma resposta válida!")
        else:
            break 
    if verificadorContinuação == "N":
        break
    
    # Verificando se devo usar o resultado.
    verificador2 = True
    while verificador2:
        print("Você quer usar o resultado como primeiro número? (S/N)?")
        verificadorResultado = input()
        if verificadorResultado != "S" and verificadorResultado != "N":
            print ("Digite uma resposta válida!")
        else:
            break 
    if verificadorContinuação == "S":
        numero1 = resultado


print("Finalizando calculadora")