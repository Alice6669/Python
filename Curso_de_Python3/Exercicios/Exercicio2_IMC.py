nome = "Alice"
alturaMetros = 1.75
pesoKilos = 84

imc = pesoKilos / alturaMetros ** 2

imc = ((imc * 100) // 1) / 100

print(nome, "tem", alturaMetros, "metros", pesoKilos, "kilos e IMC de", imc)