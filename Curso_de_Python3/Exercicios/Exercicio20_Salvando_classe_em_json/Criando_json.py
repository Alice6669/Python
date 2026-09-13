import json

# Criando classe pessoa.
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

# Criando objeto pessoa
p = []
p.append(Pessoa("João", 56, 1.78))
p.append(Pessoa("Maria", 37, 1.87))
p.append(Pessoa("Aline", 13, 1.55))

dados = []
for number, value in enumerate(p):
    dados.append(p[number].__dict__) 

# Escrevendo Json
caminho = "json.json"
with open(caminho, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)