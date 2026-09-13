# Perguntas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

quant_acertos = 0
for indice in perguntas:
    # Questões.
    print("Pergunta: " + indice["Pergunta"])
    for index, value in enumerate(indice["Opções"]):
        print(str(index) + ") " + str(value))
     
    # Verificando resultado.
    resposta = input(print("Escolha uma opção: "))
    if indice['Opções'][int(resposta)] == indice['Resposta']:
        print("Você acertou!!!")
        quant_acertos += 1
    else:
        print("Você errou... a resposta certa era " + indice["Resposta"] + ".")

# Resultado final.
print("Você acertou " + str(quant_acertos) + " de " + str(len(perguntas)) + " perguntas.")