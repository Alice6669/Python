# Coletando nome.
print("Qual nome você quer enfeitar?")
nome = input()
# Coletando simbolo.
print ("Com qual símbolo você quer enfeitá-lo?")
simbolo = input()
# Iniciando contador.
contador = 0
# Efeitando nome.
nomeEnfeitado = ""
while contador < len(nome):
    nomeEnfeitado += simbolo + nome[contador]
    contador += 1
    
    if contador == len(nome):
        nomeEnfeitado += simbolo

# Mostrando nome enfeitado
print(nomeEnfeitado)