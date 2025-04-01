import pandas as pd  
import numpy as np 

# Buscar planilha no Google Sheets  
sheet_id = "1khkuQT4BuLlgugOlp-FKkHp1Ep9GG6eYCyjgjWI3l7U"  
sheet_name = "Empresas"  

# Criar a URL para importar os dados como CSV  
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"  

print(url)  # Verifique se a URL está correta  
# Carregar os dados no Vs Code
data = pd.read_csv(url)  

# Mostrar as primeiras linhas da planilha  
print(data.head())

#a. Construa uma tabulação cruzada com Taxa de crescimento (%) como a variável linha e Tamanho como a variável coluna.
# Use classes começando em −10 e terminando em 70 em gradações de 10 para a Taxa de crescimento (%).
#Definir as faixas de Taxa de Crescimento (%)
# Exemplo de dados

import pandas as pd
import numpy as np

# Exemplo de dados (com a coluna 'Tamanho' como exemplo)
data = pd.DataFrame({
    'Taxa de crescimento (%)': [5, -3, 15, 45, 67, 10, 25, -7, 55, 72, 0],
    'Tamanho': ['Large', 'Midsized', 'Small', 'Large', 'Small', 'Midsized', 'Large', 'Small', 'Large', 'Midsized', 'Small']
})

# Verifique as colunas do DataFrame para identificar possíveis problemas
print([coluna for coluna in data.columns])

# Se houver espaços extras nos nomes das colunas, remova-os
data.columns = data.columns.str.strip()

# Definir os intervalos personalizados
bins = [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 100]

# Definir os rótulos para os intervalos
labels = ["-10 a 0", "0 a 10", "10 a 20", "20 a 30", "30 a 40", "40 a 50", "50 a 60", "60 a 70", "70 a 80", "80 a 100"]

# Classificar os dados dentro dos intervalos
data["Faixa_Crescimento"] = pd.cut(data["Taxa de crescimento (%)"], bins=bins, labels=labels, include_lowest=True)

# Exibir o DataFrame com a nova coluna
print(data)

# Criar uma tabulação cruzada (cross-tab) entre Faixa de Crescimento e Tamanho
tab_cros = pd.crosstab(data["Faixa_Crescimento"], data["Tamanho"])

# Exibir a tabulação cruzada
print(tab_cros)

