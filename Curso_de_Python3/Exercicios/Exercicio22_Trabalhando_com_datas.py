# calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

# Importações.
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Configurando datas.
date_inicio = datetime(2020, 12, 20)
date_fim = date_inicio + relativedelta(years = 5)

# Salvando datas.
dates_parcelas = []
date_atual = date_inicio
while date_fim >= date_atual:
    dates_parcelas.append(date_atual)
    date_atual = date_atual + relativedelta(months = 1)

# Calculando parcela.
valor_parcela = 1000000 / len(dates_parcelas)

# Mostrando resultado.
print(f"\nO valor das parcelas é: {valor_parcela:.2f} \nO total de parcelas são: " \
      f"{len(dates_parcelas)} \nData das parcelas:\n")
for indice, date in enumerate(dates_parcelas):
    print(f"{indice + 1}ª - {date.strftime('%d,%m,%Y')}")
