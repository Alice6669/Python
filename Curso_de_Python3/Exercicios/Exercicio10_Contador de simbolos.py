# Coletando a frasse.
print("Diga qual frasse você quer verrificar:")
frasse = input()
frasseLower = frasse.lower()

# Iniciando loop.
contadorDEwhile = 0
contadorDEsimbolosIndependenteUpper = 0
simboloSalvoIndependenteUpper = ""
contadorDEsimbolosNormal = 0
simboloSalvoNormal = ""
while contadorDEwhile < len(frasse):
    
    # Contando independente de uppercase.
    if frasseLower.count(frasseLower[contadorDEwhile]) > contadorDEsimbolosIndependenteUpper:
      simboloSalvoIndependenteUpper = frasseLower[contadorDEwhile]
      contadorDEsimbolosIndependenteUpper = frasseLower.count(frasseLower[contadorDEwhile])
    
    # Contando normal.
    if frasse.count(frasse[contadorDEwhile]) > contadorDEsimbolosNormal:
        simboloSalvoNormal = frasse[contadorDEwhile]
        contadorDEsimbolosNormal = frasse.count(frasse[contadorDEwhile])

    # Finalizando loop
    contadorDEwhile += 1

# Mostrando resultado
print('Se considerar letras maisculas e minusculas o simbolo' \
      ' que aparece mais vezes é o "', simboloSalvoNormal,'"')
print('Se desconsiderar letras maisculas e minusculas o simbolo' \
      ' que aparece mais vezes é o "', simboloSalvoIndependenteUpper,'"')
