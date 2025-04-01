#O site VirtualTourist fornece classificação para hoteis em todo o mundo. As classificações fornecidas por 649 hóspedes no Sheraton Anaheim Hotel, l
# localizado perto da Disneyland Resort, em Anaheim, Califórnia, podem ser encontradas no DATAfile chamado HotelRatings (site VirtualTourist, 25 de fevereiro de 2013). 
# As respostas possíveis foram Excelente, Muito Bom, Regular, Ruim e Péssima. 

#a. Construa uma distribuição de frequência. 
#b. Construa uma distribuição de frequência percentual. 
#c. Construa um gráfico de barras para a distribuição de frequência percentual.
#d. Comente sobre como os hóspedes avaliam sua estadia no Sheraton Anaheim Hotel. 
#e. Os resultados para 1.679 convidados que ficaram no Disney’s Grand Californian forneceram as seguintes distribuições de frequência##

#a # Construa uma distribuição de frequencia##
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Adicione as categorias entre aspas para que sejam interpretadas como strings
x = ['Excelente', 'Muito Bom', 'Regular', 'Ruim', 'Péssima']
y = [187, 252, 107, 61, 41]

# Gerando o gráfico de barras
plt.bar(x, y)

# Adicionando a grade ao gráfico
plt.grid()

# Exibindo o gráfico
plt.show()


#Construa uma frequencia em percentual####

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Categorias e frequências absolutas
x = ['Excelente', 'Muito Bom', 'Regular', 'Ruim', 'Péssima']
y = [187, 252, 107, 61, 41]

# Calculando o total de elementos
total = sum(y)

# Calculando a frequência percentual
percentual = [(i / total) * 100 for i in y]

# Gerando o gráfico de barras
plt.bar(x, percentual)

# Adicionando título e rótulos aos eixos
plt.title('Frequência Percentual')
plt.xlabel('Categorias')
plt.ylabel('Percentual (%)')

# Adicionando a grade ao gráfico
plt.grid(True)

# Exibindo o gráfico
plt.show()

# Imprimindo a frequência percentual
for categoria, perc in zip(x, percentual):
    print(f'{categoria}: {perc:.2f}%')

import pandas as pd
import numpy as np

# Categorias e frequências absolutas
x = ['Excelente', 'Muito Bom', 'Regular', 'Ruim', 'Péssima']
y = [187, 252, 107, 61, 41]

# Calculando o total de elementos
total = sum(y)

# Calculando a frequência percentual
percentual = [(i / total) * 100 for i in y]

# Criando a tabela com pandas
tabela = pd.DataFrame({
    'Categoria': x,
    'Frequência Absoluta': y,
    'Frequência Percentual (%)': percentual
})

# Exibindo a tabela
print(tabela)

#Compare as classificações para o Disney’s Grand Californian com os resultados obtidos para o Sheraton Anaheim Hotel. 
#Dados do Hotel Disney’s Grand Californian 

import pandas as pd
import numpy as np

# Dados
x = ['Excelente', 'Muito Bom', 'Regular', 'Ruim', 'Péssima']
y = [807, 521, 200, 107, 44]

# Calculando o total de elementos
total = sum(y)

# Calculando a frequência percentual
percentual = [(i / total) * 100 for i in y]

# Imprimindo a frequência percentual
for categoria, perc in zip(x, percentual):
    print(f'{categoria}: {perc:.2f}%')

# Criando a tabela com pandas
tabela = pd.DataFrame({
    'Categoria': x,
    'Frequência Absoluta': y,
    'Frequência Percentual (%)': percentual
})

# Exibindo a tabela
print(tabela)


#Exercício 18# 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

#Dados do exercicio 18 cap. 2### Pontos por jogo ##

ppj= [27.0, 21.1, 23.3, 15.7, 17.0, 28.8, 19.2, 16.4, 17.2, 17.3, 
      26.4, 21.2, 18.9, 18.2, 17.5, 27.1, 15.5, 16.5, 17.5, 14.0, 
      22.9, 17.2, 17.0, 13.6, 16.9, 28.4, 16.7, 11.7, 16.3, 16.3, 
      19.2, 17.6, 15.7, 16.2, 15.1, 21.0, 18.5, 18.0, 13.6, 12.3, 
      20.8, 18.3, 17.7, 17.1, 18.7, 17.6, 18.3, 14.6, 16.7, 14.6]

#Definição das classes (intervalos)##
bins = np.arange(10,32, 2)  #De 10 a 30, com incremento de 2 

#Criando um Dataframe
ppj_series = pd.Series(ppj)

#(a) Distribuição de frequência 
freq, edges = np.histogram(ppj_series, bins=bins) 
print("Distribuição de frequência:") 
for i in range(len(freq)): 
    print(f"{edges[i]:.1f} - {edges[i+1]:.1f}: {freq[i]}")

# b. Mostre a distribuição de frequência relativa.
freq_rel = freq / sum(freq) 
print("\nDistribuição de frequência relativa:") 
for i in range(len(freq_rel)): print(f"{edges[i]:.1f} - {edges[i+1]:.1f}: {freq_rel[i]:.2f}")

# c. Distribuição de frequência percentual acumulada######
freq_perc_acum = np.cumsum(freq_rel) * 100 
print("\nDistribuição de frequência percentual acumulada:") 
for i in range(len(freq_perc_acum)): print(f"Até {edges[i+1]:.1f}: {freq_perc_acum[i]:.1f}%")

##d. Histograma
plt.hist(ppj_series, bins=bins, edgecolor='black', 
         alpha=0.7) 
plt.xlabel("Pontos por Jogo (PPJ)")
plt.ylabel("Frequência") 
plt.title("Histograma de Pontos por Jogo") 
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.show()

###e. Verificação de assimetria

if ppj_series.skew() > 0: 
    print("\nOs dados parecem estar positivamente distorcidos (assimetria à direita).") 
elif ppj_series.skew() < 0: 
    print("\nOs dados parecem estar negativamente distorcidos (assimetria à esquerda).")
else: 
    print("\nOs dados parecem estar simétricos.")    

## f.Percentual de jogadores com pelo menos 20 pontos por jogo

percent_20_plus = (ppj_series[ppj_series >= 20].count() / len(ppj_series)) * 100 
print(f"\nPorcentagem de jogadores com pelo menos 20 PPJ: {percent_20_plus:.2f}%")


#Exercicio 37
##Considere os seguintes dados em duas variáveis categorizadas. A primeira variável, x, pode assumir valores A, B, C ou D. 
# A segunda variável, y, pode assumir valores I ou II. A tabela a seguir fornece a frequência com a qual cada combinação ocorre.

#a. Construa um gráfico de barras lado a lado com x no eixo horizontal. 
import numpy as np 
import matplotlib.pyplot as plt

#Dados do exercicio 37
categorias = ['A', 'B', 'C', 'D']
valores1 = [143, 200, 321, 420]
valores2 = [857, 800, 679, 580]

#Posição das Barras
x = np.arange(len(categorias))
largura = 0.4 ####A largura da barras

###Criação do gráfico de barras lado a lado ###
fig,ax = plt.subplots()
ax.bar(x - largura/2, valores1, largura, label = 'Grupo 1')
ax.bar(x + largura/2, valores2, largura, label = 'Grupo 2')

#Colocar os rótulos e títulos no grafico
ax.set_xlabel('Categorias')
ax.set_ylabel('Valores')
ax.set_title('Gráfico de Barras Lado a Lado')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()

#Gerar o gráfico
plt.show()

###Exercicio 52
##a. Construa uma tabulação cruzada com Taxa de crescimento (%) como a variável linha e Tamanho como a variável coluna. 
# Use classes começando em −10 e terminando em 70 em gradações de 10 para a Taxa de crescimento (%).

import pandas as pd  

# Buscar planilha no Google Sheets  
sheet_id = "1khkuQT4BuLlgugOlp-FKkHp1Ep9GG6eYCyjgjWI3l7U"  
sheet_name = "Empresas"  

# Criar a URL para importar os dados como CSV  
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"  

print(url)  # Verifique se a URL está correta  
# Carregar os dados no pandas  
data = pd.read_csv(url)  

# Mostrar as primeiras linhas da planilha  
print(data.head())






