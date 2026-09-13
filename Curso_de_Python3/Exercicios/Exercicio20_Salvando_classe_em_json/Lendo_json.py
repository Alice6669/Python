import json
import Criando_json
# Lendo json
caminho = "json.json"
with open(caminho, "r") as arquivo:
    dados = json.load(arquivo)

p = []
for number, value in enumerate(dados):
    p.append(Criando_json.Pessoa(**dados[number]))


for number, value in enumerate(p):
    print(p[number].__dict__)