# Criando lista
import os

while True:
    numerosCPF = []
    # Coletando CPF
    print("Qual CPF você quer validar?")
    CPFBruto = input("")

    # Quebrando CPF em digitos
    CPFTemporario = CPFBruto.split(".")
    CPFTemporario2 = CPFTemporario[-1].split("-")
    if len(CPFTemporario) == 3 and len(CPFTemporario2) == 2:
        CPFTemporario.pop()
        CPFTemporario.append(CPFTemporario2[0])
        CPFTemporario.append(CPFTemporario2[1])
        for grupoNumeros in CPFTemporario:
            for numeros in grupoNumeros:
                numerosCPF.append(numeros)
    elif len(CPFTemporario) == 3:
        print("O formato do CPF deve ser como um desses exemplos:")
        print("111.111.111-11")
        print("11111111111")
        continue
    else:
        numerosCPF = list(CPFBruto)

    # Convertendo o CPF em números, vendo se não há letras e se tem 11 números.
    for indice, numero in enumerate(numerosCPF):
        try:
            numerosCPF[indice] = int(numero)
        except ValueError:
            print("O formato do CPF deve ser como um desses exemplos:")
            print("111.111.111-11")
            print("11111111111")
            continue
    if len(numerosCPF) != 11:
        print("O formato do CPF deve ser como um desses exemplos:")
        print("111.111.111-11")
        print("11111111111")
        continue

    # Validando o penultimo digíto.
    numerosCPFMulti10 = []
    somaTotal = 0
    for indice, numero in enumerate(numerosCPF):
        if indice < 9:
            numerosCPFMulti10.append((10 - indice) * numero )
    for numero in numerosCPFMulti10:
        somaTotal += numero
    somaMult10 = somaTotal * 10
    restoPor7 = somaMult10 % 11
    if restoPor7 <= 9 :
        penultimoDigito = restoPor7
    else:
        penultimoDigito = 0

    # Validando o ultimo digito
    numerosCPFMulti10 = []
    somaTotal = 0
    for indice, numero in enumerate(numerosCPF):
        if indice < 10:
            numerosCPFMulti10.append((11 - indice) * numero )
    for numero in numerosCPFMulti10:
        somaTotal += numero
    somaMult10 = somaTotal * 10
    restoPor7 = somaMult10 % 11
    if restoPor7 <= 9 :
        ultimoDigito = restoPor7
    else:
        ultimoDigito = 0


    # Mostrando resultado.
    if penultimoDigito == numerosCPF[-2] and ultimoDigito == numerosCPF[-1]:
        print("O CPF é válido, o final é: ", str(penultimoDigito), str(ultimoDigito))
    else:
        print("O CPF não é válido, o final de via ser: ", str(penultimoDigito), str(ultimoDigito), \
              "\nMas é: ", numerosCPF[-2:])